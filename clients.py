class Clients:
    def __init__(self, name, surname, balance=0):
        self.name = name
        self.surname = surname
        self.balance = balance

    def get_balance(self):
        return f'Клиент "{self.name} {self.surname}". Баланс: {self.balance} руб.'

    def add_money(self, money):
        self.balance += money
        print(f'На баланс {self.name} {self.surname} внесено {money}')

    def pay(self, money):
        self.balance -= money
        print(f'С баланса {self.name} {self.surname} потрачено {money}')

