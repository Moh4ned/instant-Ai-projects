class CoffeeMachine:
    def __init__(self):
        self.water_level = 0
        self.coffee_beans = 0
        self.milk_level = 0

    def fill_water(self, amount):
        self.water_level += amount

    def fill_coffee(self, amount):
        self.coffee_beans += amount

    def fill_milk(self, amount):
        self.milk_level += amount

    def brew_coffee(self):
        if self.water_level >= 100 and self.coffee_beans >= 50 and self.milk_level >= 50:
            print("Preparing coffee...")
            self.water_level -= 100
            self.coffee_beans -= 50
            self.milk_level -= 50
            print("Your coffee is ready!")
        else:
            print("Sorry, not enough ingredients to brew coffee.")

    def check_water_level(self):
        print("Water level:", self.water_level)

    def check_coffee_beans(self):
        print("Coffee beans:", self.coffee_beans)

    def check_milk_level(self):
        print("Milk level:", self.milk_level)


coffee_1 = CoffeeMachine()
coffee_1.fill_water(int(input("Enter the amount of water: ")))
coffee_1.fill_coffee(int(input("Enter the amount of coffee beans: ")))
coffee_1.fill_milk(int(input("Enter the amount of milk: ")))
coffee_1.brew_coffee()
coffee_1.check_water_level()
coffee_1.check_coffee_beans()
coffee_1.check_milk_level()