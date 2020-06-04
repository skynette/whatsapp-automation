from twilio.rest import Client 





# Download the helper library from https://www.twilio.com/docs/python/install


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
def create_api_key():
	global account_sid
	global auth_token
	global client
	account_sid = 'AC01fb133ba87d07e1db4f58b64badd3ba'
	auth_token = '9ea804149c59721393896ecf712d09d7'
	client = Client(account_sid, auth_token)
	# new_key = client.new_keys.create()
	# print(new_key.sid)


def send():	 
	message = client.messages.create( 
	                              from_='whatsapp:+14155238886',  
	                              body='Final changes, hope this works',      
	                              to='whatsapp:+2348182336574' 
	                          ) 
	 
	print(message.sid)
def main():
	create_api_key()
	send()
