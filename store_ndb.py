# store_ndb.py
from google.appengine.ext import ndb
import pickle

import logging
logging.basicConfig(level=logging.DEBUG)

# Google NDB implementation

class GaeShelf(ndb.Model):
	content = ndb.StringProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add=True)

class Store(object):
	def __init__(self):
		self.db = None
		
	def open(self, name):
		self.db = GaeShelf()
		# self.db.text_factory = str -> from SQLite
		
	def read(self, id):
		logging.info('ENTER: read ID ' + str(id))
		try:
			key = ndb.Key(urlsafe=id)
			obj = key.get()
		except: return None
		if obj:
			val = str(obj.content)
			#logging.info('Read:' + val)
			d = pickle.loads(val)
			return d
		else:
			return None
		
	def write(self, id, d):
		if id!= None:
			# gen new id
			key = ndb.Key(urlsafe=id)
			shelf = key.get()
			#logging.info("write:shelf=" + str(shelf))
			if shelf == None:
				shelf = GaeShelf()
		else:
			shelf = GaeShelf()

		s = pickle.dumps(d)
		shelf.content = unicode(s)
		id = shelf.put()
		#logging.debug('Dumped:' + repr(s))

		return id.urlsafe()
		
	def close(self):
		pass
		
	def list(self):
		# Not needed for ndb
		return ["0"]
	
	def delete(self, id):
		self.db.execute('delete from shelf where key=?', (id,))
		self.db.commit()
