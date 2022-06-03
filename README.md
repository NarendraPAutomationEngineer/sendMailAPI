# Simple Python Flask REST API to send Mails using gmail

Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.

## How to run this code ?
Step1: Clone this repo using below command <br />
  git clone https://github.com/NarendraPAutomationEngineer/sendMailAPI.git <br />
Step2: <br />
  cd sendMailAPI <br />
Step3: <br />
  pip install -r requirements.txt or  pip3 install -r requirements.txt<br />
Step4: <br />
  Now open Browser then login into your gmail and then open the below link <br />
  https://myaccount.google.com/u/4/security?hl=en <br />
  Finally   enable  2-step verifiction by passing mobile number and then create app password<br />
Step5:  <br />
  Update gmailID & gPass (16 character which you get from above step) in configs.py file <br />  
Step6: <br />
  Now run with python app.py or python3 app.py <br />
Step7: <br />
  open new terminal and try the below command to send mail using the api <br />
  curl -i -X POST -H "Content-Type: application/json"   http://192.168.0.111:8080/mail -d '{"subject": "Alert! File System Usage", "toMailId": "dowithpython@gmail.com", "mailBody": "File System Usage is : 85%"}'
 
## Get Links With Coupon Codes For Udemy Course Using Below Link 
Link ==> [Udemy Links With Coupon Codes](https://www.youtube.com/watch?v=dg6hltm8VEE&t=0s)
