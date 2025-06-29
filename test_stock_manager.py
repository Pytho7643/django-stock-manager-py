import unittest
import stock_manager

class TestInvalidCart(unittest.TestCase):
    def setUp(self):
        stock_manager.save_products({})
        stock_manager.create_cart()

    def test_stringprice_negativequantity(self):
        cart = {
            "1": {"name": "apple", "price": "two", "quantity": 200},
            "2": {"name": "orange", "price": 1.5, "quantity": -10}
        }
        stock_manager.save_cart(cart)
        loaded_cart = stock_manager.load_cart()

        with self.assertRaises(ValueError):
            stock_manager.cart_total(loaded_cart)

if __name__ == '__main__':
    unittest.main()
