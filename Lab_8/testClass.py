class CreditCard:
    def __init__(self, number, balance):
        self.number = number
        self.balance = balance

    def withdraw(self, money):
        if money < self.balance:
            self.balance -= money
        else:
            print('Get a job you bum')

    def __str__(self):
        string = "$" + str(self.balance)
        return string

    def __eq__(self, other):
        if isinstance(other, CreditCard):
            return self.number == other.number and self.balance == other.balance


def main():
    credit_card_1 = CreditCard(123, 100000)
    credit_card_2 = CreditCard(123, '1000000')
    if credit_card_1 == credit_card_2:
        print('same card')
    else:
        print('Not the same card you thief')
    print("Testing the github integration")


if __name__ == '__main__':
    main()
