import requests
import json
import boto3

BASE_RES_URL = (
    'https://jj2fsi1ci6'
    '.execute-api.ap-southeast-1.amazonaws.com{}'
)

# From the email_consumer.py Function
# EMAIL SENDER API


def send_email_alert(to_email, message, logger_level):
    subject = f'[GTECH EMAIL NOTIF] {logger_level} ERROR ALERT'
    url = BASE_RES_URL.format('/email_sender_service')
    res = requests.post(url, json={
        'to': to_email,
        'subject': subject,
        'body': message,
    })

def lambda_handler(event, context):
    if event["log_level"] == "CRITICAL":
        send_email_alert(event['email'], event['msg'], event["log_level"])
    elif event["log_level"] == "INFO":
        send_email_alert(event['email'], event['log_level']+" "+event['msg'], event["log_level"])
        notification = "Here is the SNS notification for Lambda function tutorial."
        client = boto3.client('sns')
        response = client.publish (
          TargetArn = "arn:aws:sns:us-east-1:337008671328:ron-ababao-TOPIC-INFO",
          Message = json.dumps({'default': event["msg"]}),
          MessageStructure = 'json'
        )
    elif event["log_level"] == "DEBUG":
        send_email_alert(event['email'], event['log_level']+" "+event['msg'], event["log_level"])
        notification = "Here is the SNS notification for Lambda function tutorial."
        client = boto3.client('sns')
        response = client.publish (
          TargetArn = "arn:aws:sns:us-east-1:337008671328:ron-ababao-TOPIC-DEBUG",
          Message = json.dumps({'default': event["msg"]}),
          MessageStructure = 'json'
        )
    elif event["log_level"] == "WARNING":
        send_email_alert(event['email'], event['log_level']+" "+event['msg'], event["log_level"])
        notification = "Here is the SNS notification for Lambda function tutorial."
        client = boto3.client('sns')
        response = client.publish (
          TargetArn = "arn:aws:sns:us-east-1:337008671328:ron-ababao-TOPIC-WARNING",
          Message = json.dumps({'default': event["msg"]}),
          MessageStructure = 'json'
        )
    elif event["log_level"] == "ERROR":
        send_email_alert(event['email'], event['log_level']+" "+event['msg'], event["log_level"])
        notification = "Here is the SNS notification for Lambda function tutorial."
        client = boto3.client('sns')
        response = client.publish (
          TargetArn = "arn:aws:sns:us-east-1:337008671328:ron-ababao-TOPIC-ERROR",
          Message = json.dumps({'default': event["msg"]}),
          MessageStructure = 'json'
        )