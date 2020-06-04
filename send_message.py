from twilio.rest import Client 
# update

def send():
	account_sid = 'AC01fb133ba87d07e1db4f58b64badd3ba' 
	auth_token = 'd20c7414a64028815a76e2b05f912635' 
	client = Client(account_sid, auth_token) 
	 
	message = client.messages.create( 
	                              from_='whatsapp:+14155238886',  
	                              body='I love you so much ❤❤❤❤❤❤\nI wanna be with you everyday of my life 😘😘😘. sick and tired aggggg',      
	                              to='whatsapp:+2348182336574' 
	                          ) 
	 
	print(message.sid)
