from server import db


class TestCase(db.Model):
    # __table__ = "client"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120))
    info = db.Column(db.String(100))
    def as_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "info": self.info
        }
