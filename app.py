from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin
import requests
from twilio.rest import Client
import os
import sqlite3
import random

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"

@app.route('/sendOTP', methods=['GET'])
@cross_origin()
def sendOTP():
    connection = sqlite3.connect('database.db')
    volunteer = connection.execute('SELECT phone_number, major_crime FROM volunteers WHERE aadhar_number=' + request.json['aadhar_number']).fetchall()
    connection.close()
    major_crime = volunteer[0][1]
    if(major_crime == 1):
        return {"otp": 0, "major_crime": major_crime}

    account_sid = 'ACa6a91f2a36c947c11fc2f5c01dd7b473'
    auth_token = '1cbb3f7ca5ac24d65af34f9017379304'
    client = Client(account_sid, auth_token)

    otp=random.randint(1000,9999)

    message = client.messages.create(
            body='Your OTP is '+str(otp),
            from_='+15735204442',
            to=volunteer[0][0]
        )

    return {"otp": otp, "major_crime": major_crime}


if __name__ == "__main__":
    app.run()

