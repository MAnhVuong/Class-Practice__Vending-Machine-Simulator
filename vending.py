# Author   : Minh Anh Vuong
# Email    : minhanhvuong@umass.edu
# Spire ID : 34892350

class VendingMachine:
    def __init__(self):
        self.items = {}
        self.customer_balance = 0.00
        self.total_sales = 0.00
        self.sales_history = []

    def add_item(self, name, price, quantity):
        if name not in self.items:
            self.items[name] = [price, quantity]
        else:
            self.items[name] = [price, self.items[name][1] + quantity]
        print(f"{quantity} {name}(s) added to inventory")
        
    def get_item_price(self, name):
        if name not in self.items:
            print("Invalid item")
            return None
        return self.items[name][0]
    
    def get_item_quantity(self, name):
        if name not in self.items:
            print("Invalid item")
            return None
        return self.items[name][1]
    
    def list_items(self):
        if self.items == {}:
            print("No items in the vending machine")
        else:
            sorted_dict = dict(sorted(self.items.items()))
            print("Available items:")
            for item in sorted_dict:
                print(f"{item} (${sorted_dict[item][0]}): {sorted_dict[item][1]} available")
                
    def insert_money(self, dollar_amount:float):
        if dollar_amount not in [1.0, 2.0, 5.0]:
            print("Invalid amount")
        else:
            self.customer_balance += dollar_amount
            print(f"Balance: {{:0.2f}}".format(self.customer_balance))
            
    def purchase(self, name):
        if name not in self.items:
            print("Invalid item")
        elif self.items[name][1] == 0:
            print(f"Sorry {name} is out of stock")
        elif self.items[name][0] > self.customer_balance:
            print(f"Insufficient balance. Price of {name} is {{:0.2f}}".format(self.items[name][0]))
        else:
            self.items[name][1] -= 1
            self.customer_balance -= self.items[name][0]
            self.sales_history = [(name, self.items[name][0])] + self.sales_history
            self.total_sales += self.items[name][0]
            print(f"Purchased {name}\nBalance: {{:0.2f}}".format(self.customer_balance))
    
    def output_change(self):
        if self.customer_balance == 0:
            print("No change")
        else:
            print(f"Change: {self.customer_balance}")
            self.customer_balance = 0.0
            
    def remove_item(self, name):
        if name not in self.items:
            print("Invalid item")
        else:
            del self.items[name]
            print(f"{name} removed from inventory")
            
    def empty_inventory(self):
        self.items = {}
        print("Inventory cleared")
        
    def get_total_sales(self):
        return float("{:.2f}".format(self.total_sales))
    
    def stats(self, N):
        if len(self.sales_history) == 0:
            print("No sale history in the vending machine")
        else:
            report_sales = {}
            for sale in self.sales_history[:N]:
                if sale[0] not in report_sales:
                    report_sales[sale[0]] = [sale[1], 1]
                else:
                    report_sales[sale[0]][0] += sale[1]
                    report_sales[sale[0]][1] += 1
            sorted_dict = dict(sorted(report_sales.items()))
            print(f"Sale history for the most recent {min(N, len(self.sales_history))} purchase(s):")
            for item in sorted_dict:
                print(f"{item}: ${sorted_dict[item][0]} for {sorted_dict[item][1]} purchase(s)")
    
# Create a new vending machine
vending_machine = VendingMachine()

# Add some items to the inventory
vending_machine.add_item('Soda', 1.50, 5)
vending_machine.add_item('Chips', 0.75, 10)
vending_machine.add_item('Candy', 0.50, 15)

# Show the available items
vending_machine.list_items()

# Insert some coins
vending_machine.insert_money(1.00)
vending_machine.insert_money(1.00)

# Purchase an item
vending_machine.purchase('Soda')

# Get the price of an item
print(vending_machine.get_item_price('Chips'))

# Purchase another item
vending_machine.purchase('Chips')

# Get the total sales
print(vending_machine.get_total_sales())

# Insert some coins
vending_machine.insert_money(5.00)
vending_machine.insert_money(5.00)

# Purchase another item
vending_machine.purchase('Chips')
vending_machine.purchase('Chips')
vending_machine.purchase('Chips')
vending_machine.purchase('Candy')
vending_machine.purchase('Candy')

# print stats
vending_machine.stats(3)
vending_machine.stats(5)
vending_machine.stats(10)

# Remove an item
vending_machine.remove_item('Candy')

# Show the available items again
vending_machine.list_items()

# Get the quantity of an item
print(vending_machine.get_item_quantity('Gum'))

# Empty the inventory
vending_machine.empty_inventory()

# Show the available items again
vending_machine.list_items()