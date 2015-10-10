import contextio as c

CONSUMER_KEY = 'cfowbx9i'
CONSUMER_SECRET = 'EtO6xdRE3x2ln7Xp'

context_io = c.ContextIO(
	consumer_key=consumer_key,
	consumer_secret=CONSUMER_SECRET
)

accounts = context_io.get_accounts(email='ricky.barillas@gmail.com')
if accounts:
	account = accounts[0]
print account