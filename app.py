from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    course = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

@app.route("/users", methods=["POST"])

def create_user():
    data = request.get_json()

    if not data or "name" not in data or "course" not in data or "email" not in data:
        return jsonify({
            "message": "Name, course, and email are required!",
            "status": "error"
        }), 400

    existing_user = User.query.filter_by(email=data["email"]).first()

    if existing_user:
        return jsonify({
            "message": "Email already exists!",
            "status": "error"
        }), 409

    new_user = User(
        name=data["name"],
        course=data["course"],
        email=data["email"]
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "message": "User created successfully!",
        "status": "success",
        "user": {
            "id": new_user.id,
            "name": new_user.name,
            "course": new_user.course,
            "email": new_user.email
        }
    }), 201

@app.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()

    return jsonify({
        "message": "Users retrieved successfully!",
        "status": "success",
        "users": [
            {
                "id": user.id,
                "name": user.name,
                "course": user.course,
                "email": user.email
            }
            for user in users
        ]
    }), 200

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "message": "User not found!",
            "status": "error"
        }), 404

    data = request.get_json()

    if not data:
        return jsonify({
            "message": "No data provided!",
            "status": "error"
        }), 400

    if "name" in data:
        user.name = data["name"]

    if "course" in data:
        user.course = data["course"]

    if "email" in data:
        existing_user = User.query.filter_by(email=data["email"]).first()

        if existing_user and existing_user.id != user.id:
            return jsonify({
                "message": "Email already exists!",
                "status": "error"
            }), 409

        user.email = data["email"]

    db.session.commit()

    return jsonify({
        "message": "User updated successfully!",
        "status": "success",
        "user": {
            "id": user.id,
            "name": user.name,
            "course": user.course,
            "email": user.email
        }
    }), 200

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    user = User.query.get(user_id)

    if not user:
        return jsonify({
            "message": "User not found!",
            "status": "error"
        }), 404

    db.session.delete(user)
    db.session.commit()

    return jsonify({
        "message": "User deleted successfully!",
        "status": "success"
    }), 200

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)