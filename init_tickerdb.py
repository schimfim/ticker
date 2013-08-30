import sqlite3
import logging
logging.basicConfig(level=logging.INFO)

dbname = 'ticker.db'

conn = sqlite3.connect(dbname)
c = conn.cursor()

# Drop table
try:
	c.execute('drop table shelf')
except:
	logging.info('No table shelf, creating it.')
	
# Create table
c.execute('create table shelf (key text, val text)')

# Save (commit) the changes
conn.commit()

c.close()
conn.close()

logging.info('Initialized SQLite db')
