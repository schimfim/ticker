from giteasy import RepoCLI

files = [
	'FussiTicker.py',
	'FussiTicker_test.py',
	'FussiWeb.py',
	'config.py',
	'init_tickerdb.py',
	'store.py',
	'store_sqlite.py',
	'store_ndb.py',
	'store_test.py',
	'sync.py',
	'ticker_tpl.py',
	'run_ticker.py'
	]

RepoCLI('ticker', 'schimfim', 'Ninz2009', files)
