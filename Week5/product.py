class Product(object):
    def __init__(self, price, item_name, weight, brand, cost):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.cost = cost
        self.status = "for sale"
        self.display_info()

    def sell(self):
        self.status = "sold"
    
    def add_tax(self, decimaltax):
        tax_amount = (self.price * decimaltax)
        pricewithtax = self.price + tax_amount
        print pricewithtax
        return self

    def return_method(self, reason):

        # if the item is being returned because it is defective, change stastus to defective and change price to 0
        if reason == 'defective':
            self.status = "defective"
            self.price = 0
            return self
        
        # if it is being returned in the box, like new mark it as for sale
        elif reason == 'returned in the box':
            self.status = 'for sale'
            return self
        
        # if the box has been opened set status to used and apply 20% discount
        elif reaon == 'opened':
            self.status = 'used'
            self.price = self.price - (self.price * 0.20)
            return self

        else:
            print "Please enter correct reason(s)"
            return self

    def display_info(self):
        print '-------------------------------'
        print "Item Name: " + self.item_name
        print "Price: " + str(self.price)
        print "Weight: " + str(self.weight)
        print "Brand: " + self.brand
        print "Cost: " + str(self.cost)
        print "Status: " + self.status

apple = Product(100, "apple", 50, "Samsung", 30)

