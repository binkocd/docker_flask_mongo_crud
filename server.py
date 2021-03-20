from flask import Flask, Response, request
import pymongo
import json
from bson.objectid import ObjectId

# Initialize Flask
app = Flask(__name__)

# Setup MongoDB Connection
try:
    mongo = pymongo.MongoClient(
        host='mongo_1',
        port=27017,
        serverSelectionTimeoutMS=1000
        )
    db = mongo.company
except Exception as ex:
    print(ex)
    print("Error - Cannot connect to MongoDB.")


# Setup Health Check
@app.route('/', methods=["GET"])
def base():
    return Response(
        response=json.dumps(
            {"Status": "UP"}),
        status=200,
        mimetype="application/json"
        )


# Setup Create
@app.route("/users", methods=["POST"])
def create_user():
    try:
        user = {"name": request.form["name"],
                "lastname": request.form["lastName"]}
        dbResponse = db.users.insert_one(user)
        print(dbResponse.inserted_id)
        return Response(
            response=json.dumps(
                {"message": "user created",
                 "id":f"{dbResponse.inserted_id}"
                 }),
            status=200,
            mimetype="application/json"
        )       
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {"message": "Cannot create users"}),
            status=500,
            mimetype="application/json"
            )

'''
# Setup Read
@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find())
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response=json.dumps(data),
            status=500,
            mimetype="application/json"
                )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {"message": "Cannot read users"}),
            status=500,
            mimetype="application/json"
            )
'''

# Setup Read Recent
@app.route("/users", methods=["GET"])
def get_some_users():
    try:
        data = list(db.users.find().limit(1).sort([('$natural',-1)]))
        for user in data:
            user["_id"] = str(user["_id"])
        return Response(
            response=json.dumps(data),
            status=500,
            mimetype="application/json"
                )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {"message": "Cannot read users"}),
            status=500,
            mimetype="application/json"
            )


# Setup Update
@app.route("/users/<id>", methods=["PUT"])
def update_user(id):
    try:
        dbResponse = db.users.update_one(
            {"_id":ObjectId(id)},
            {"$set":{"name":request.form["name"]}}
        )
        if dbResponse.modified_count == 1:
            return Response(
                response=json.dumps(
                    {"message": "User Updated"}),
                status=200,
                mimetype="application/json"
                )
        else:
            return Response(
                response=json.dumps(
                    {"message": "Nothing to update"}),
                status=200,
                mimetype="application/json"
                )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {"message": "Cannot Update"}),
            status=500,
            mimetype="application/json"
            )


# Setup Delete
@app.route("/users/<id>", methods=["Delete"])
def delete_user(id):
    try:
        dbResponse = db.users.delete_one(
            {"_id": ObjectId(id)},
        )
        if dbResponse.deleted_count == 1:
            return Response(
                    response=json.dumps(
                        {"message": "Deleted", "id": f"{id}"}),
                    status=200,
                    mimetype="application/json"
                    )
        else:
            return Response(
                    response=json.dumps(
                        {"message": "Not found", "id": f"{id}"}),
                    status=200,
                    mimetype="application/json"
                    )
    except Exception as ex:
        print(ex)
        return Response(
            response=json.dumps(
                {"message": "Cannot Delete"}),
            status=500,
            mimetype="application/json"
            )


# Initalize Host, Port, Debugging
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=False)
