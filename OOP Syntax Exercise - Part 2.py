### TODO:
#   - code a Pants class with the following attributes
#   - color (string) eg 'red', 'yellow', 'orange'
#   - waist_size (integer) eg 8, 9, 10, 32, 33, 34
#   - length (integer) eg 27, 28, 29, 30, 31
#   - price (float) eg 9.28

### TODO: Declare the Pants Class 
class Pants():
### TODO: write an __init__ function to initialize the attributes
    def __init__(self, color, waist_size, length, price):
        self.color = color
        self.waist_size = waist_size
        self.length = length
        self.price = price

### TODO: write a change_price method:
#    Args:
#        new_price (float): the new price of the shirt
#    Returns:
#        None
    def change_price(self, new_price):
        self.price = new_price

### TODO: write a discount method:
#    Args:
#        discount (float): a decimal value for the discount. 
#            For example 0.05 for a 5% discount.
#
#    Returns:
#        float: the discounted price
    def discount(self, discount):
        return self.price - (self.price * discount)

def check_results():
    pants = Pants('red', 35, 36, 15.12)
    assert pants.color == 'red'
    assert pants.waist_size == 35
    assert pants.length == 36
    assert pants.price == 15.12
    
    pants.change_price(10) == 10
    assert pants.price == 10 
    print(pants.discount(.1))
    assert pants.discount(.1) == 9
    
    print('You made it to the end of the check. Nice job!')

check_results()