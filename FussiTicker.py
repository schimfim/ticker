# gist id=02149d46255c8da6d91d
# Ticker
# v2

import logging
from config import ticks, mode
import random

logging.basicConfig(level=logging.INFO)
logging.info('ticker mode=' + mode)

class Ticker(object):
	def __init__(self, nid='123', team1='Heim', team2='Gast'):
		self.id = nid
		self.home = 0
		self.guest = 0
		self.setTeams(team1, team2)
	
	def setTeams(self, team1, team2):
		self.hteam = team1
		self.gteam = team2
	
	def scoreHome(self):
		self.home += 1
		
	def scoreGuest(self):
		self.guest += 1
		
	def reset(self):
		self.home = 0
		self.guest = 0
		
	def getFields(self):
		d = {
		  'mid'		: self.id,
			'home' 	: self.home,
			'guest' : self.guest,
			'hteam' : self.hteam,
			'gteam' : self.gteam
			}
		return d
	
def getDefaults():
	# Get defaults
	d = dict(mid='', home=0, guest=0,
	         hteam='', gteam='',
	         running=False)
	return d
	
# db access
# Requires global 'ticks' implementing
# store.Store
def save(t):
		ticks.open('ticker.db')
		d = {
			'home' : t.home,
			'guest' : t.guest,
			'hteam' : t.hteam,
			'gteam' : t.gteam
			}
		ticks.write(t.id, d)
		ticks.close()
	
def load(id):
		ticks.open('ticker.db')
		t = Ticker(id)
		t.id = id
		d = ticks.read(id)
		ticks.close()
		if(d):
			t.home = d['home']
			t.guest = d['guest']
			t.hteam = d['hteam']
			t.gteam = d['gteam']
			return t
		else: 
			return None

def dbList():
	ticks.open('ticker.db')
	l = ticks.list()
	ticks.close()
	return l

def delete(mid):
	ticks.open('ticker.db')
	ticks.delete(mid)
	ticks.close()
	
def genId():
	ids = dbList()
	id = random.randint(1, 999999)
	while id in ids:
		id = random.randint(1, 999999)
		
	return str(id).zfill(6)

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

