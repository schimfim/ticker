# store_ndb.py
from google.appengine.ext import ndb
import pickle

import logging
logging.basicConfig(level=logging.INFO)

# Google NDB implementation

class GaeShelf(ndb.Model)
	content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)

class Store(object):
	def __init__(self):
		self.db = None
		
	def open(self, name):
		self.db = GaeShelf()
		# self.db.text_factory = str -> from SQLite
		
	def read(self, id):
		key = ndb.Key(urlsafe=id)
		val = key.get()
		if val:
			logging.debug('Read:' + repr(val))
			d = pickle.loads(val)
			return d
		else:
			return None
		
	def write(self, id, d):
		s = pickle.dumps(d)
		logging.debug('Dumped:' + repr(s))
		# already there?
		c = self.db.cursor()
		c.execute('select val from shelf where key=?', (id,))
		val = c.fetchone()
		c.close()
		if val:
			self.db.execute('update shelf set val=? where key=?', (s, id))	
		else: 
			# new entry
			self.db.execute('insert into shelf values (?,?)', (id, s))

		self.db.commit()
		
	def close(self):
		pass
		
	def list(self):
		# Not needed for ndb
		return ["0"]
	
	def delete(self, id):
		self.db.execute('delete from shelf where key=?', (id,))
		self.db.commit()
