class CoffeeMachine:
    coffee = [[250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6]]
    def __init__(self, water, milk, coffee_beans, disposible_cups, money):
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.disposible_cups = disposible_cups
        self.money = money
        self.buy_state = 0
        self.fill_state = 0

    def query(self, query):
        if self.buy_state != 0:
            self.buy(query)
        elif self.fill_state != 0:
            self.fill(query)
        elif query == 'buy':
            self.buy(query)
        elif query == 'fill':
            self.fill(query)
        elif query == 'take':
            self.take()
        elif query == 'remaining':
            self.remaining()
        elif query == 'exit':
            return False
        return True

    def buy(self, query):
        if query == 'back':
            self.buy_state = 0
            return
        if self.buy_state == 0:
            print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:')
            self.buy_state = 1
        else:
            sort = int(query) - 1
            self.buy_state = 0
            if self.water - CoffeeMachine.coffee[sort][0] < 0:
                print('Sorry, not enough water!')
                return
            self.water -= CoffeeMachine.coffee[sort][0]
            if self.milk - CoffeeMachine.coffee[sort][1] < 0:
                print('Sorry, not enough milk!')
                return
            self.milk -= CoffeeMachine.coffee[sort][1]
            if self.coffee_beans - CoffeeMachine.coffee[sort][2] < 0:
                print('Sorry, not enough coffee beans!')
                return
            self.coffee_beans -= CoffeeMachine.coffee[sort][2]
            if self.disposible_cups - 1 < 0:
                print('Sorry, not enough disposible cups!')
                return
            self.disposible_cups -= 1
            self.money += CoffeeMachine.coffee[sort][3]
            print('I have enough resources, making you a coffee!')
    def fill(self, query):
        if self.fill_state == 0:
            print('Write how many ml of water do you want to add:')
            self.fill_state = 1
        elif self.fill_state == 1:
            self.water += int(query)
            print('Write how many ml of milk do you want to add:')
            self.fill_state = 2
        elif self.fill_state == 2:
            self.milk += int(query)
            print('Write how many grams of coffee beans do you want to add:')
            self.fill_state = 3
        elif self.fill_state == 3:
            self.coffee_beans += int(query)
            print('Write how many disposable cups of coffee do you want to add:')
            self.fill_state = 4
        else:
            self.disposible_cups += int(query)
            self.fill_state = 0
            
    def take(self):
        print('I gave you ${}'.format(self.money))
        self.money = 0
    
    def remaining(self):
        print('The coffee machine has:')
        print(self.water, 'of water')
        print(self.milk, 'of milk')
        print(self.coffee_beans, 'of coffee beans')
        print(self.disposible_cups, 'of disposable cups')
        print(self.money, 'of money')




coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)
while True:
    print('Write action (buy, fill, take, remaining, exit):')
    query = input()
    if not coffee_machine.query(query):
        break
