from flask import Blueprint,jsonify,request
from codeblog.model import Routerdetails,RouterdetailsSchema
from codeblog import db


main = Blueprint('main', __name__)


@main.route("/",methods =['GET','POST'])
def welcome():
    return jsonify ({'msg':'Hello World to Blue Print'})

@main.route("/createrouter",methods =['GET','POST'])
def createrouter():
    if request.method == 'POST':
        sapid                   = request.args.get('sapid')
        hostname                = request.args.get('hostname')
        macadress               = request.args.get('macadress')


        router_details = Routerdetails(sapid = sapid,hostname = hostname ,macadress = macadress)
        db.session.add(router_details)
        db.session.commit()   

        return jsonify({'status':'success','message':'Router Creation Successfull','Loop Back':router_details.loopback})


@main.route("/updaterouter",methods =['GET','POST'])
def updaterouter():
    if request.method == 'POST':

        ip                          =   request.args.get('hostname')
        macadress                   =   request.args.get('macadress') 
        router_details              =   Routerdetails.query.filter_by(hostname = ip).first()
        router_details.macadress    =   macadress
        db.session.commit()

        return jsonify({'status':'success','message':'Router Updation Successfull'}) 

@main.route("/serachrouter",methods =['GET','POST'])
def serachrouter():
    sapid          = request.args.get('sapid')
    router_details = Routerdetails.query.filter_by(sapid = sapid).all()
    routerschema   = RouterdetailsSchema (many = True)

    return routerschema.dumps(router_details)

@main.route("/deleterouter",methods =['GET','POST'])
def deleterouter():
    if request.method == 'POST':

        ip             =   request.args.get('hostname')
        router_details = Routerdetails.query.filter_by(hostname = ip).first()
        db.session.delete(router_details)
        db.session.commit()

        return jsonify({'status':'success','message':'Router Deleted Successfully'}) 








    
