from codeblog import db,ma
from marshmallow import fields

class Routerdetails(db.Model):
    loopback                  = db.Column(db.Integer,primary_key=True)
    sapid                     = db.Column(db.String(30),nullable=False)
    hostname                  = db.Column(db.String(30))
    macadress                 = db.Column(db.String(30))

    def __repr__(self):
        return f"('{self.loopback}','{self.sapid}','{self.hostname}','{self.macadress}')"

class RouterdetailsSchema(ma.ModelSchema):
    class Meta:
        model = Routerdetails
        sqla_session = db.session  