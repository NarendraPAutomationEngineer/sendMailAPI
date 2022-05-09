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
    if recipient is None:
        abort(400,"toMailid Is Missed in Body")
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

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
