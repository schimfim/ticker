# FussiWeb

import logging
logging.basicConfig(level=logging.INFO)

from bottle import route, post, run, template, request, response, debug, error, view, redirect
import webbrowser

import FussiTicker

debug(True)

# Generate mailto link
def mailto(mid):
	base = 'mailto:?subject=Follow%20my%20Ticker'
	body = '&body=<a>Ticker</a>'
	return base + body

# storage utilities
def loadMatch(mid):
		if mid:
			# load ticker from db
			t = FussiTicker.load(mid)
			return t

def getFields(t=None):
		# Returns dict with all disp. fields.
		# Todo: defaults for ticker must be
		# provided by ticker!
		list = FussiTicker.dbList()
		# Get default
		d = dict(mid='',mids=list,mail='',
			  home=0,guest=0,hteam='',gteam='',
			  running=False)
		if t:
			mid = t.id
			tick = t.getFields()
			mail = mailto(mid)
			d.update(tick, mail=mail, mid=mid)
		return d

# View ticker or show fresh
@route('/')
@route('/<mid>')
@view('ticker')
def view_ticker(mid=''):
	if not mid:
		# try cookie
		mid = request.get_cookie("FussiTicker")
	# will be empty without cookie
	t = loadMatch(mid)
	d = getFields(t)
	return d

# Update ticker
@post('/')
@post('/<mid>')
def action(mid=''):
	if not mid:
		# generate new id
		mid = FussiTicker.genId()
		t = FussiTicker.Ticker(mid)
		response.set_cookie("FussiTicker", mid)
	else: 
		t = loadMatch(mid)
	# process action
	if request.forms.home:
		t.scoreHome()
	elif request.forms.guest:
		t.scoreGuest()
	elif request.forms.new:
		t.reset()
	else:
		logging.warning('Unknown action')
	
	FussiTicker.save(t)
	d = getFields(t)
	
	return template('ticker', d)

# Delete mid
@route('/del/<mid>')
def delete(mid):
	FussiTicker.delete(mid)
	redirect('/')

# Error handlers
@error(405)
def error405(error):
 	return 'Unkown route'
	
# Run the server
args = {'stop_when_done':'True'}
#webbrowser.open('http://localhost:8080', *args)
webbrowser.open('http://localhost:8080', stop_when_done=False)

run(host='localhost', port=8080)

