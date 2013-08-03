import sqlite3
import logging
logging.basicConfig(level=logging.INFO)

dbname = 'ticker.db'

conn = sqlite3.connect(dbname)
c = conn.cursor()

# Drop table
c.execute('drop table shelf')

# Create table
c.execute('create table shelf (key text, val text)')

# Save (commit) the changes
conn.commit()

c.close()
conn.close()

logging.info('Initialized SQLite db')
