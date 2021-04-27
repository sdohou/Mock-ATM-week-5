class Category:

    # constructor
    def __init__(self, category, amount):
        self.category = category
        self.amount = amount

    # methods
    def deposit(self, amount):
        self.amount += amount
        return "You have successfully deposited {} in the {} category".format(amount, self.category)

    def budget_balance(self):
        return "Your current balance is: {}".format(self. amount)

    def check_balance(self, amount):
        # return self.balance
        # return False
        if amount < self.amount:
            # Calling withdraw method
            self.amount -= amount
            # Printing updated balance
            return "\nUpdated Balance: " + str(self.amount)
        else:
            return "\nYou're balance is less than withdrawal amount: " + str(self.amount) + ". Please make a deposit."

    def withdraw(self, amount):
        self.amount -= amount
        return "You have successfully withdrawn {} from the {} category".format(amount, self.category)

    def transfer(self, amount, category):
        # transfer between two instantiated categories
        self.withdraw(amount) + ' ' + category.deposit(amount)
        return "You have successfully withdrawn {} from the {} category.".format(amount, self.category)


food_category = Category('Food', 500)
clothing_category = Category('Clothing', 300)
car_category = Category('Car Expenses', 600)
rent_category = Category('Rent', 1200)
edu_category = Category('Education', 700)

# print(food_category.deposit(250))
# print(food_category.budget_balance())
# print(food_category.check_balance(520))
# print(food_category.withdraw(200))
# print(food_category.budget_balance())
# print(food_category.transfer(50, car_category))
