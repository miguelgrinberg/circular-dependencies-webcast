from flask import url_for
from myapp import db
from myapp.models.query import QueryWithSoftDelete


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    deleted = db.Column(db.Boolean(), default=False)

    query_class = QueryWithSoftDelete

    def to_dict(self):
        return {'id': self.id, 'name': self.name,
                'url': url_for('api.get_user', id=self.id)
                if not self.deleted else None}
