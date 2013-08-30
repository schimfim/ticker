# config.py
 
# Imports
from bottle import ConfigDict
import re
 
#Config
#config = ConfigDict()
#config.read("app.cfg")
#catchall = config.getboolean('bottle', 'catchall')
 
# Mode
with open('ticker.cfg') as f:
	s = f.readline()
r = re.match('.*=([a-z]+)', s)
mode = r.group(1)
print 'mode=', mode

if mode == 'iphone':
	import store_sqlite as store
	ahost = 'localhost'
	aport = 8080
	run_opts = {'host':ahost, 'port':aport}
	web_opts = {'stop_when_done' : False , 'modal' : False  }
elif mode == 'mac':
	import store_sqlite as store
	ahost = 'localhost'
	aport = 8088
	run_opts = {'host':ahost, 'port':aport}
	web_opts = {}
elif mode == 'appengine':
	import store_ndb as store
	ahost = 'fussiticker.appspot.com'
	aport = 80
	run_opts = {'server':'gae'}
	web_opts = {}
else: 
	raise ValueError('Unknown mode: {}'.format(mode))



# 
ticks = store.Store()
base_url = 'http://' + ahost + ':' + str(aport)

