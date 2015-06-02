# models.py

from views import db

class ChakraAttribute(db.Model):
    __tablename__ = 'chakra_attributes'
    primary_key = db.Column(db.Integer, primary_key=True)
    chakra_number = db.Column(db.String, nullable=False)
    attribute_type = db.Column(db.String, nullable=False)
    attribute_description = db.Column(db.String, nullable=False)
    attribute_detail = db.Column(db.String, nullable=False)

    def __init__(self, chakra_number, attribute_type, attribute_description,
                 attribute_detail):
        self.chakra_number = chakra_number
        self.attribute_type = attribute_type
        self.attribute_description = attribute_description
        self.attribute_detail = attribute_detail

    def __repr__(self):
        return '<chakra_number %r>' %(self.chakra_number)
