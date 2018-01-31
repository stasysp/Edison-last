from twilio.rest import TwilioRestClient

account = "AC54fd023d3b7b95f70d61204eb92a6dc0"
token = "28db766e12ff6b1529f82644ba9013de"
client = TwilioRestClient(account, token)

def send_massage(): 
    print (sendMessage)

def send_massage(): 
    message = client.messages.create(to="+79101414140", from_="+12013748367",
                                 body="Party Detected!")