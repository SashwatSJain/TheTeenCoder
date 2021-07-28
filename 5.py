from twilio.rest import Client

account_sid = ''
auth_token = ''
x = 0
while x<10:
    client = Client(account_sid, auth_token)

                                  body='LOL😂',
                                  to='whatsapp:+919xxxxxxxxx'
                              )
    print(message.sid)
    x+=1
