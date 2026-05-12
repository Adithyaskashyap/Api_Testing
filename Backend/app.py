from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
CORS(app)
@app.route('/')
def home_route():
    return render_template('index.html')


app.config["MONGO_URI"] = "mongodb://localhost:27017/userdb"

mongo = PyMongo(app)

# GET Users
@app.route('/users', methods=['GET'])
def get_users():
    users = []
    for user in mongo.db.users.find():
        users.append({
            "id": str(user["_id"]),
            "name": user["name"],
            "email": user["email"]
        })
    return jsonify(users)

# POST User
@app.route('/users', methods=['POST'])
def add_user():
    data = request.json

    mongo.db.users.insert_one({
        "name": data['name'],
        "email": data['email']
    })

    return jsonify({"message": "User Added"})

# DELETE User
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.users.delete_one({"_id": ObjectId(id)})
    return jsonify({"message": "Deleted"})
# UPDATE User
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):

    data = request.json

    mongo.db.users.update_one(
        {"_id": ObjectId(id)},
        {
            "$set": {
                "name": data['name'],
                "email": data['email']
            }
        }
    )

    return jsonify({"message": "User Updated"})

if __name__ == '__main__':
    app.run(debug=True)