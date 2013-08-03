'''
FussiTicker_test

'''

import unittest
import FussiTicker

c = FussiTicker

class TestTicker(unittest.TestCase):
	def test_match(self):
		t = c.Ticker('HSV','BVB')
		t.scoreHome()
		self.assertEqual(t.home, 1)
		

if __name__ == '__main__':
    unittest.main()

