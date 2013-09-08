# config.py
 
# Imports
from bottle import ConfigDict
import re
import logging
logging.basicConfig(level=logging.DEBUG)
 
#Config
#config = ConfigDict()
#config.read("app.cfg")
#catchall = config.getboolean('bottle', 'catchall')
 
# Mode
with open('ticker.cfg') as f:
	s = f.readline()
r = re.match('.*=([a-z]+)', s)
mode = r.group(1)
logging.info('mode = ' + mode)

if mode == 'iphone':
	import store_sqlite as store
	ahost = 'localhost'
	aport = 8080
	run_opts = {'host':ahost, 'port':aport}
	web_opts = {'stop_when_done' : True, 'modal' : False  }
	refresh = 3000
	debug = True 
	catchall=False 
elif mode == 'mac':
	import store_sqlite as store
	ahost = 'localhost'
	aport = 8088
	run_opts = {'host':ahost, 'port':aport}
	web_opts = {}
	refresh = 3000
	debug = True
	catchall=False
elif mode == 'appengine':
	import store_ndb as store
	ahost = 'fussiticker.appspot.com'
	aport = 80
	run_opts = {'server':'gae'}
	web_opts = {}
	refresh = 10000
	debug = True
	catchall=True 
else: 
	raise ValueError('Unknown mode: {}'.format(mode))



# 
# ticks = store.Store()
base_url = 'http://' + ahost + ':' + str(aport)

