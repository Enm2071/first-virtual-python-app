from app import db

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }
        
class Country(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    city = db.Column(db.String)
    state = db.Column(db.String)
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    created_at = db.Column(db.Date)
    country = db.relationship('Country', backref=db.backref('addresses', lazy='dynamic'))
    def to_dict(self):
        return {
            "id": self.id,
            "city": self.city,
            "state": self.state,
            "country_id": self.country_id,
            "created_at": str(self.created_at.strftime('%d-%m-%Y')),
            "country": self.country.to_dict()
        }      
        
class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    last_name = db.Column(db.String)
    phone = db.Column(db.String)
    email = db.Column(db.String)
    address_id = db.Column(db.Integer, db.ForeignKey('address.id'))
    address = db.relationship('Address', backref=db.backref('clients', lazy='dynamic'))
    created_at = db.Column(db.Date)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "last_name": self.last_name,
            "phone": self.phone,
            "email": self.email,
            "address_id": self.address_id,
            "address": self.address.to_dict(),
            "created_at": str(self.created_at.strftime('%d-%m-%Y'))
        }
        

        

        
