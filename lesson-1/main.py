import sys
from cache import LRUCache

print("Python version: {}.{}".format(sys.version_info.major, sys.version_info.minor))

cache = LRUCache()
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
cache.get('Jesse') # вернёт 'James'
cache.rem('Walter')
cache.get('Walter') # вернёт ''

cache.getall()

