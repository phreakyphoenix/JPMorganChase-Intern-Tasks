import unittest
from client3 import getDataPoint, getRatio

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2 ))


  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
       self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'], (quote['top_bid']['price'] + quote['top_ask']['price'])/2 ))


  """ ------------ Add more unit tests ------------ """

  def test_getRatio_withPriceBZero(self):
    priceA = 12
    priceB = 0
    self.assertIsNone(getRatio(priceA,priceB))

  def test_getRatio_withPriceAZero(self):
    priceA = 0
    priceB = 83.2
    self.assertEqual(getRatio(priceA,priceB), 0)
 
  def test_getRatio_resultGreaterThan1(self):
    priceA = 103
    priceB = 8.8
    self.assertGreater(getRatio(priceA,priceB), 1)

  def test_getRatio_resultLessThan1(self):
    priceA = 33.8
    priceB = 109
    self.assertLess(getRatio(priceA,priceB), 1)

  def test_getRatio_resultExactlyOne(self):
    priceA = 121
    priceB = 121
    self.assertEqual(getRatio(priceA,priceB), 1)

if __name__ == '__main__':
    unittest.main()
