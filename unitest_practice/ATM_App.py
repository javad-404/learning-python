import unittest 


def withdraw(balance, amount):
    
    if not isinstance(amount, int):
        raise TypeError("You need to enter numbers!")
    
    if amount <= 0 :
        raise ValueError("You should enter positive numbers.")
    
    if amount > balance:
        raise ValueError("Balance is not enough!")
    
    if amount % 10 != 0:
        raise ValueError("System dont have low money!")
    
    return balance - amount
    
    
    
class TestATM(unittest.TestCase):
    def setUp(self):
        self.start_money = 5000
        print("--- ATM Reset: Balance is 5000 ---")
            
    def test_withdraw(self):
        new_balance = withdraw(self.start_money, 1000)
        self.assertEqual(new_balance, 4000)

    def test_low_amount(self):
       self.assertRaises(ValueError, withdraw, self.start_money, 6000)
            
    def test_small_change(self):
        self.assertRaises(ValueError, withdraw, self.start_money, 56)
            
    def test_str_insteadof_int(self):
        self.assertRaises(TypeError, withdraw, self.start_money, 'ali')
        
        
if __name__ == "__main__":
    unittest.main()