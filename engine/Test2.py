from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import unittest

# To test the connection of Mongodb
class UnitTestCase2(unittest.TestCase):
   def test_connection(self):
      client = MongoClient()
      try:
         # The ismaster command is cheap and does not require auth.
         client.admin.command('ismaster')
      except ConnectionFailure:
         print("Server not available")(argv=['first-arg-is-ignored'], exit=False)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)