# FussiWeb

import logging
logging.basicConfig(level=logging.INFO)

from bottle import Bottle, route, post, template, request, response, debug, error, view, redirect

import FussiTicker
from config import run_opts, base_url

debug(True)

# App
app = Bottle()

# Generate mailto link
def mailto(mid):
	base = 'mailto:?subject=Follow%20my%20Ticker'
	body = '&body=<a>{url}/{id}</a>'.format(url=base_url, id=mid)
	return base + body

def getFields(t=None):
		# Returns dict with all disp. fields
		list = FussiTicker.dbList()
		# Get default
		d = dict(mid='', mids=list, base_url=base_url, mail='')
		d.update(FussiTicker.newModel())
		if t:
			mid = t.id
			tick = t.getModel()
			mail = mailto(mid)
			d.update(tick, mail=mail, mid=mid)
		return d

# View ticker or show fresh
@app.route('/')
@app.route('/<mid>')
@view('ticker')
def view_ticker(mid=''):
	if not mid:
		# try cookie
		mid = request.get_cookie("FussiTicker")
		logging.info('Using cookie=' + str(mid))
	# will be empty without cookie
	t = None
	if mid:
		t = FussiTicker.load(mid)
	d = getFields(t)
	return d

# Update ticker
@app.post('/')
@app.post('/<mid>')
def action(mid=''):
	if not mid:
		# generate new ticker
		t = FussiTicker.Ticker()
	else: 
		t = FussiTicker.load(mid)
	# process action
	if request.forms.home_u:
		t.scoreHome()
	elif request.forms.home_d:
		t.scoreHome(-1)
	elif request.forms.guest_u:
		t.scoreGuest()
	elif request.forms.guest_d:
		t.scoreGuest(-1)
	elif request.forms.new:
		# Start new session
		response.delete_cookie("FussiTicker")
		redirect('/')
	elif request.forms.reset:
		t.reset()
	elif request.forms.start:
		t.start()
	else:
		logging.warning('No action')
	
	t.setTeams(request.forms.hteam, 'na')
	
	FussiTicker.save(t)
	logging.info('New id:' + str(t.id))
	response.set_cookie("FussiTicker", t.id)
	d = getFields(t)
	
	return template('ticker', d)

# Delete mid
@app.route('/del/<mid>')
def delete(mid):
	FussiTicker.delete(mid)
	redirect('/')

# Error handlers
@error(405)
def error405(error):
 	return 'Unkown route'

