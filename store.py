# store.py

import shelve

# Interface and shelve implementation
class Store(object):
	def __init__(self):
		self.db = {}
		
	def open(self, name):
		self.db = shelve.open(name)
		# return self.db
		
	def read(self, id):
		d = {}
		if(id in self.db):
			d = self.db[id]
		return d
		
	def write(self, id, d):
		self.db[id] = d
		return id
		
	def close(self):
		self.db.close()
		
	def list(self):
		return self.db.keys()
	
	def delete(self, id):
		del self.db[id]
