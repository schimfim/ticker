# see also http://code.google.com/p/pysqlite/

import sqlite3

dbname = ':memory:'

def create_db(conn=None ):
	if not conn:
		conn = sqlite3.connect(dbname)
	c = conn.cursor()
	
	# Create table
	c.execute('create table test (key text, value text)')

	# add some values
	testdata = [('k1','v1'),('k2','v2'),('k3','v3')]
	for t in testdata:
         	c.execute('insert into test values (?,?)', t)

	# Save (commit) the changes
	conn.commit()

	# We can also close the cursor if we are done with it
	c.close()
	return conn

def dump(conn = None):
	if not conn:
		conn = sqlite3.connect(dbname)
	c = conn.cursor()
	
	c.execute('select * from test')
	for row in c:
		print row
		
	c.close()

# main: run unit tests
if __name__ == '__main__':
	dump()
	conn = create_db()
	dump(conn)


'''
from google.appengine.ext import db

class Shelf(db.Model):
  id = db.StringProperty(required=True)
  str = db.StringProperty(required=True)

e = Shelf(id="122", str="abc")
e.put()
'''
