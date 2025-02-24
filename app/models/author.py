from app import db
# from app.models.book import Book

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    books = db.relationship('Book', back_populates='author')

    def to_dict(self):
        return {'id': self.id,
                'name': self.name}
    
    @classmethod
    def from_dict(cls, dict):
        return Author(name=dict['name'])