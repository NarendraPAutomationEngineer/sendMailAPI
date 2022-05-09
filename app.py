from flask import Flask,request, jsonify,abort
from flask_mail import Mail, Message
from configs import *

app=Flask(__name__)
mail = Mail(app) # instantiate the mail class
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = gmailID
app.config['MAIL_PASSWORD'] = gPass
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)
@app.before_request
def only_json():
    if not request.is_json: 
        abort(400)

@app.errorhandler(400)
def not_data(error):
    response=jsonify({"Error": error.description })
    response.status_code=400
    return response

@app.route("/mail", methods=['POST'])
def sendMailWithCustomBody():
    reqBody=request.get_json()
    if not reqBody:
        abort(400,"Body Is Missed") 
    subject=reqBody.get("subject","Hello")
    recipient=reqBody.get("toMailId")
    msg = Message(
                subject,
                sender = gmailID,
                recipients = [recipient]
               )
    msg.body = reqBody.get("mailBody",'Hello Flask message sent from Flask-Mail')
    mail.send(msg)
    response= {
        "Status": "Message Sent"
    }
    response = jsonify(response)
    response.status_code = 201
    return response

@app.route("/secrets", methods=['GET'])
def secrets():
    data={
        "secrets": {
            "remoteServerCreds": {
                "user": "ubuntu",
                "pass" : "ubuntu@123"
            },
            "awsAccessKeys" : {
                "aws_access_key_id": "LIVEARET45LJASDF9EWR",
                "aws_secret_access_key": "4GAbEcDDDeyYRNO4WBrnYeWgVa-YTDrV6GIJMqQabc"
            }       
        }
    }
    response = jsonify(data)
    response.status_code = 200
    return response
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)