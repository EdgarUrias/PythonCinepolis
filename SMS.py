import smtplib

def send(message):
        # Replace the number with your own, or consider using an argument\dict for multiple people.
	to_number = 'micorreo' #Mail de llegada
	auth = ('micorreo', 'micotraseña')

	# Establish a secure session with gmail's outgoing SMTP server using your gmail account
	server = smtplib.SMTP( "smtp.gmail.com", 587 ) #servidor de gmail, se puede cambiar por cualquiera
	server.starttls()
	server.login(auth[0], auth[1])

	# Send text message through SMS gateway of destination number
	server.sendmail( auth[0], to_number, message)