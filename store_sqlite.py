# store_sqlite.py
import sqlite3
import pickle
import random

import logging

# SQLite implementation
class Store(object):
	def __init__(self):
		self.db = None
		
	def open(self, name):
		self.db = sqlite3.connect(name)
		self.db.text_factory = str
		
	def read(self, id):
		c = self.db.cursor()
		c.execute('select val from shelf where key=?', (id,))
		val = c.fetchone()
		c.close()
		if val:
			logging.debug('Read:' + repr(val[0]))
			d = pickle.loads(val[0])
			return d
		else:
			return None
		
	def write(self, id, d):
		if id==None:
			# gen new id
			id = self.genId()
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
		return id
		
	def close(self):
		self.db.close()
		
	def list(self):
		c = self.db.cursor()
		c.execute('select key from shelf')
		keys = c.fetchall()
		c.close()
		l = []
		for i in keys: l.append(i[0])
		return l
	
	def delete(self, id):
		self.db.execute('delete from shelf where key=?', (id,))
		self.db.commit()

	def genId(self):
		ids = self.list()
		id = random.randint(1, 999999)
		while id in ids:
			id = random.randint(1, 999999)
		
		return str(id).zfill(6)

#
# Unit tests

import unittest

class TestStore(unittest.TestCase):
	
	def setUp(self):
		self.s = Store()
		self.s.open(':memory:')
		# Create table
		c = self.s.db.cursor()
		c.execute('create table shelf (key text, val text)')
		c.close()

	def test_string(self):
		# test string
		data = 'A String'
		self.s.write('123', data)
		res = self.s.read('123')
		self.assertEqual(data, res)

	def test_dict(self):
		# test dict
		data = {'home':2, 'guest':3}
		self.s.write('123', data)
		res = self.s.read('123')
		self.assertEqual(data, res)


# Run tests
if __name__ == '__main__':
    unittest.main()

