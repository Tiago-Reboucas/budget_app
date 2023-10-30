class Category:
    fund = 0.0
    def __init__(self, name:str) -> None:
        self.name = name
        self.ledger = list()
        pass

    def check_funds(self, amount:float) -> bool:
        if amount > self.fund: return False
        else: return True

    def deposit(self, amount:float, description:str = "") -> None:
        self.ledger.append({"amount": amount, "description": description})
        self.fund += amount

    def withdraw(self, amount:float, description:str = "") -> bool:
        if not self.check_funds(amount):
            return False
        
        self.ledger.append({"amount": -amount, "description": description})
        self.fund -= amount
        return True
    
    def get_balance(self) -> float:
        return self.fund
    
    def transfer(self, amount:float, other_category) -> bool:
        if not self.check_funds(amount):
            return False
        
        self.withdraw(amount, f"Transfer to {other_category.name}")
        other_category.deposit(amount, f"Transfer from {self.name}")
        return True
    
    def __str__(self) -> str:
        full_str = self.name.center(30, "*")

        for item in self.ledger:
            line = "\n" + "{:<23}{:>7.2f}".format(item["description"][:23], item["amount"])
            full_str += line

        full_str += "\n" + f"Total: {self.fund:.2f}"

        return full_str

def add_space(num:int):
    string = str(num)
    if len(string) < 3:
        string = " " + string
        string = add_space(string)
    return string

def create_spend_chart(categories:list):
    # Get all withdraws
    category_spend = dict()
    for item in categories:
        spends_l = [value["amount"] for value in item.ledger if value["amount"] < 0]
        spend = round(sum(spends_l), 2)

        category_spend[item.name] = spend
    
    spend_total = sum(category_spend.values())

    # Get withdraws% per category
    spend_perc = list()
    for k, v in category_spend.items():
        value = v * 100 // spend_total
        spend_perc.append((k, value))
    
    # Plot bar chart
    # Print percentages
    full_str = "Percentage spent by category\n"
    for percent in reversed(range(0, 110, 10)):
        percent_str = add_space(percent)
        full_str += percent_str + "| "

        for value in spend_perc:
            if value[1] >= percent: full_str += "o  "
            else: full_str += "   "

        full_str += "\n"
    
    # Print line
    start = full_str.find("\n")
    stop = full_str.find("\n", start+1)
    line_len = len(full_str[start:stop-1])

    full_str += 4 * " " + (line_len - 4) * "-"

    # Print Categories

    largest_cat = 0
    for key in spend_perc:
        if len(key[0]) > largest_cat: largest_cat = len(key[0])
        
    j = 0
    while j < largest_cat:
        full_str += "\n" + 5 * " "
        for entry in spend_perc:
            try: full_str += entry[0][j] + 2 * " "
            except: full_str += 3 * " "
        j += 1

    return full_str


food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())

clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)

auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

fruitnvegie = Category("Fruits/Vegetables")
fruitnvegie.deposit(500, "initial +")
fruitnvegie.withdraw(12.45, "apples")
fruitnvegie.withdraw(45.56, "pineapples")
fruitnvegie.withdraw(10, "broccoli")

print()
print(food)
print()
print(clothing)
print()
print(auto)
print()
print(fruitnvegie)
print()

print(create_spend_chart([food, clothing, auto, fruitnvegie]))
print()