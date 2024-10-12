# Assignment 4
# By Jose Fuentes
#Q1 solution :
class BankAccount:
    def __init__(self, bankname, firstname, lastname, balance=0):
        self.bankname = bankname
        self.firstname = firstname
        self.lastname = lastname
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. Current balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdrawal(self, amount):
        if amount > self.balance:
            print("Insufficient balance for withdrawal.")
        elif amount <= 0:
            print("Withdrawal amount must be positive.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. Current balance: {self.balance}")

    def __str__(self):
        return f"Bank: {self.bankname}\nOwner: {self.firstname} {self.lastname}\nBalance: {self.balance}"


# Test the BankAccount class
account = BankAccount("Bank of America", "Jose", "Fuentes", 1000)  # Create an initial account with a balance of $1000
print(account)

account.deposit(300)  # Deposit 300
account.withdrawal(50)  # Withdraw 50
account.withdrawal(1300)  # Attempting to withdraw more than the balance

print(account)  # Show the account details

#Q2 solution 
import math

class Box:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def render(self):
        for _ in range(self.length):
            print('*' * self.width)

    def invert(self):
        self.length, self.width = self.width, self.length

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def double(self):
        self.length *= 2
        self.width *= 2

    def __eq__(self, other):
        return self.length == other.length and self.width == other.width

    def print_dim(self):
        print(f"Length: {self.length}, Width: {self.width}")

    def get_dim(self):
        return self.length, self.width

    def combine(self, other_box):
        self.length += other_box.length
        self.width += other_box.width

    def get_hypot(self):
        return math.sqrt(self.length ** 2 + self.width ** 2)


# Instantiate 3 boxes with dimensions 5x10, 3x4, and 5x10
box1 = Box(5, 10)
box2 = Box(3, 4)
box3 = Box(5, 10)

# Print dimension info for each using print_dim()
print("Dimensions of box1:")
box1.print_dim()

print("Dimensions of box2:")
box2.print_dim()

print("Dimensions of box3:")
box3.print_dim()

# Evaluate if box1 == box2 and if box1 == box3, and print results
print(f"Is box1 equal to box2? {box1 == box2}")
print(f"Is box1 equal to box3? {box1 == box3}")

# Combine box3 into box1
print("\nCombining box3 into box1:")
box1.combine(box3)
box1.print_dim()

# Double the size of the box2
print("\nDoubling the size of box2:")
box2.double()
box2.print_dim()

# Combining box1 with box2
print("\nCombining box2 into box1:")
box1.combine(box2)
box1.print_dim()

# Rendering the box by print it with asterisks
print("\nRender box1:")
box1.render()

# Obtaining the diagonal of box1 (hypotenuse)
print(f"\nThe diagonal (hypotenuse) of box1 is: {box1.get_hypot():.2f}")
