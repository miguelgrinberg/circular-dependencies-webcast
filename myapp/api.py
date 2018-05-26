from flask import url_for, jsonify, request, Blueprint
from myapp import db
from myapp.models.user import User
from myapp.models.message import Message

api = Blueprint('api', __name__)


@api.route('/users', methods=['POST'])
def new_user():
    user = User(**request.get_json())
    db.session.add(user)
    db.session.commit()
    return '', 201, {'Location': url_for('api.get_user', id=user.id)}


@api.route('/users', methods=['GET'])
def get_users():
    users = User.query
    return jsonify({'users': [u.to_dict() for u in users]})


@api.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())


@api.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get_or_404(id)
    user.deleted = True
    db.session.commit()
    return '', 204


@api.route('/users/<id>/messages', methods=['POST'])
def new_message(id):
    user = User.query.get_or_404(id)
    message = Message(user_id=user.id, **request.get_json())
    db.session.add(message)
    db.session.commit()
    return '', 201, {'Location': url_for('api.get_message', id=message.id)}


@api.route('/messages')
def get_messages():
    messages = Message.query
    return jsonify({'messages': [m.to_dict() for m in messages]})


@api.route('/messages/<id>')
def get_message(id):
    message = Message.query.get_or_404(id)
    return jsonify(message.to_dict())
