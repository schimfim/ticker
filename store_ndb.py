# store_ndb.py
from google.appengine.ext import ndb
import pickle

import logging

# Google NDB implementation

class GaeShelf(ndb.Model):
	content = ndb.StringProperty(indexed=False)
	date = ndb.DateTimeProperty(auto_now_add=True)

class Store(object):
	def __init__(self):
		self.db = None
		
	def open(self, name):
		self.db = GaeShelf()
		
	def read(self, id):
		logging.debug('read ID ' + str(id))
		try:
			key = ndb.Key(urlsafe=id)
			obj = key.get()
		except: return None
		if obj:
			val = str(obj.content)
			d = pickle.loads(val)
			logging.debug('read VAL ' + str(d))
			return d
		else:
			return None
		
	def write(self, id, d):
		if id!= None:
			logging.debug('write ID ' + str(id))
			key = ndb.Key(urlsafe=id)
			shelf = key.get()
			if shelf == None:
				shelf = GaeShelf()
		else:
			shelf = GaeShelf()

		s = pickle.dumps(d)
		shelf.content = unicode(s)
		id = shelf.put()
		logging.debug('write VAL ' + str(d))

		return id.urlsafe()
		
	def close(self):
		pass
		
	def list(self):
		# Not needed for ndb
		return ["0"]
	
	def delete(self, id):
		self.db.execute('delete from shelf where key=?', (id,))
		self.db.commit()
