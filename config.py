# gist id=02149d46255c8da6d91d

# Mode
mode = ['iphone', 'mac', 'appengine'][0]

if mode == 'iphone':
	# Storage
	import store_sqlite as store
	ahost = 'localhost'
	aport = 8080
elif mode == 'mac':
	# Storage
	import store_sqlite as store
	ahost = 'localhost'
	aport = 8080
elif mode == 'appengine':
	# Storage
	import store_sqlite as store
	ahost = 'localhost'
	aport = 8080
else: 
	raise ValueError('Unknown mode: {}'.format(mode))

ticks = store.Store()
base_url = 'http://' + ahost + ':' + str(aport)

