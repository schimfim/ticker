# gist id=02149d46255c8da6d91d
# Ticker
# v2

import logging
from config import mode, store

def newModel():
	# Get defaults
	d = dict(mid='', home=0, guest=0,
	         hteam='Heim', gteam='Gast',
	         running=False)
	return d
	
class Ticker(object):
	def __init__(self, nid=None, 
	             model=None ):
		self.id = nid
		if model is None:
			self.d = newModel()
		else: 
			self.d = model
	
	def setTeams(self, team1, team2):
		self.d['hteam'] = team1
		self.d['gteam'] = team2
	
	def scoreHome(self, dir=1):
		score = self.d['home']
		self.d['home'] = max(0, score+dir)
		
	def scoreGuest(self, dir=1):
		score = self.d['guest']
		self.d['guest'] = max(0, score+dir)
		
	def reset(self):
		self.d['home'] = 0
		self.d['guest'] = 0
		self.d['running'] = False
	
	# Toggle running flag
	def start(self):
		self.d['running'] = not self.d['running']
	
	def getModel(self):
		return self.d
	
# db access
# Requires global 'ticks' implementing
# store.Store
# Sets t.id to id returned from db
def save(t):
	ticks = store.Store()
	ticks.open('ticker.db')
	d = t.getModel()
	t.id = ticks.write(t.id, d)
	ticks.close()
	
def load(id):
	# Reads object with if from db. If not
	# found, returns new object
	ticks = store.Store()
	ticks.open('ticker.db')
	d = ticks.read(id)
	ticks.close()
	if not d:
		# Item not found
		id = None
	t = Ticker(id, d)
	return t

def dbList():
	ticks = store.Store()
	ticks.open('ticker.db')
	l = ticks.list()
	ticks.close()
	return l

def delete(mid):
	ticks.open('ticker.db')
	ticks.delete(mid)
	ticks.close()
	

################
# CLI
import cmd

class TickerCLI(cmd.Cmd):
	def do_init(self, parms):
		self.t = Ticker('123')
		self.do_d('')
	def do_d(self, parms):
		t = self.t
		print '=' * 20
		print t.hteam, 'vs.', t.gteam
		print 'Home:', t.home, 'Guest:', t.guest
		print '=' * 20
	def do_h(self, parms):
		self.t.scoreHome()
		self.do_d('')
	def do_g(self, parms):
		self.t.scoreGuest()
		self.do_d('')
	def do_r(self, parms):
		self.t.reset()
		self.do_d('')
		
	def do_save(self, parms):
		save(self.t)
		logging.info('Saved')
		
	def do_load(self, parms):
		newt = load('123')
		self.t = newt
		logging.info('Loaded')
		self.do_d('')
		
	def do_db(self, parms):
		ids = dbList()
		print str(ids)

def runCLI():
	c = TickerCLI()
	c.do_init(0)
	c.cmdloop()
			
# main: run unit tests
if __name__ == '__main__':
	from unittest import main
	main(module='FussiTicker_test', exit=False)
	runCLI()

