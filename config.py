# config.py
 
# Imports
from bottle import ConfigDict
 
# Config
#config = ConfigDict()
#config.read("app.cfg")
#catchall = config.getboolean('bottle', 'catchall')
 
# Mode
mode = ['iphone', 'mac', 'appengine'][2]

if mode == 'iphone':
	import store_sqlite as store
	ahost = 'localhost'
	aport = 8080
	run_opts = {'host':ahost, 'port':aport}
elif mode == 'mac':
	import store_sqlite as store
	ahost = '192.168.1.99'
	aport = 80
	run_opts = {'host':ahost, 'port':aport}
elif mode == 'appengine':
	import store_ndb as store
	ahost = 'localhost'
	aport = 8080
	run_opts = {'server':'gae'}
else: 
	raise ValueError('Unknown mode: {}'.format(mode))

web_opts = {'stop_when_done' : True}

# 
ticks = store.Store()
base_url = 'http://' + ahost + ':' + str(aport)

