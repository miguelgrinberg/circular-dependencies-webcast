from flask import url_for
from myapp import db


class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User')

    def to_dict(self):
        return {'id': self.id, 'message': self.message,
                'url': url_for('api.get_message', id=self.id),
                'user_url': url_for('api.get_user', id=self.user_id)
                if not self.user.deleted else None}
