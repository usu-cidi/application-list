import json
from flask import Flask, request, redirect, url_for
from flask_cors import CORS
import os

from email.message import EmailMessage
from datetime import datetime
import awsgi, ssl, smtplib

app = Flask(__name__)
CORS(app, supports_credentials=True)

DEV_EMAIL = os.environ.get("DEV_EMAIL")
EMAIL_PASS = os.environ.get("EMAIL_PASS")
CLIENT_URL_CORS = "http://localhost:8080/"

SUPPORTED_TOOLS = ["QA Update", "YCCT"]

if __name__ == '__main__':
    app.run(port=8000, debug=True, host="localhost")

def lambda_handler(event, context):  # for production
   return awsgi.response(app, event, context)

def prepResponse(body, code=200, isBase64Encoded="false"):
    response = {
        "isBase64Encoded": isBase64Encoded,
        "statusCode": code,
        "headers": {"Access-Control-Allow-Origin": CLIENT_URL_CORS, 'Access-Control-Allow-Credentials': "true"},
        "body": body
    }
    return response

@app.route('/test', methods=['GET'])
def test():
    return {"result": "heyyyy"}, 200

@app.route('/send-bug-email', methods=['POST'])
def bugReport():
    print("Sending an email now")

    requestInfo = json.loads(request.data)

    if not requestInfo["app-name"] in SUPPORTED_TOOLS:
        return redirect(url_for('submitted', msg='Invalid application name (stop messing with my dev tools!)'))

    reportInfo = {
        "App Name": requestInfo["app-name"],
        "Date and time": requestInfo["date-time"],
        "Expected Behavior": requestInfo["expected-behavior"],
        "Actual Behavior": requestInfo["actual-behavior"],
        "Errors": requestInfo["errors"],
        "Browser": requestInfo["browser"],
        "Other Info": requestInfo["other-info"],
        "Name": requestInfo["name"],
        "Email": requestInfo["email"],
    }

    message = f"Bug reported for {requestInfo['app-name']} submitted on {datetime.now()}" \
              f"\n\n------Form Info------\n"

    for info in reportInfo:
        message += f"{info}: {reportInfo[info]}\n"

    sendEmail(message, f"Bug Report - {requestInfo['app-name']}")
    return prepResponse({"result": "Email sent"}), 200

def sendEmail(message, subject):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = DEV_EMAIL
    receiver_email = DEV_EMAIL
    password = EMAIL_PASS

    msg = EmailMessage()
    msg.set_content(message)
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.send_message(msg, from_addr=sender_email, to_addrs=receiver_email)
