import unittest
from warehouse import update_inventory

class TesttWarehouse(unittest.TestCase):
    def setUp(self):
        self.db = {}
        print("\n--- Setup: Clean Warehouse ---")
        
    def test_add_new_item(self):
        update_inventory(self.db,"apple", 10)
        self.assertEqual(self.db["apple"], 10)
        
    def test_update_existing_item(self):
        update_inventory(self.db,"apple", 10)
        update_inventory(self.db,"apple",5)
        self.assertEqual(self.db["apple"],15)
        
    def test_negative_quantity_error(self):
        self.assertRaises(ValueError,update_inventory, self.db,"apple", -10)
        
    def test_invalid_name_type_error(self):
        self.assertRaises(TypeError,update_inventory,self.db,123,10)
        
    
if __name__ == "__main__":
    unittest.main()
        
        
        
    
    