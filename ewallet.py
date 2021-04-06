from clients import Clients

client_1 = Clients("Ivan", "Petrov")
client_2 = Clients("Masha", "Sidorova", 349)

clients = [client_2, client_1]
for men in clients:
    print(men.get_balance())


client_1.add_money(500)
client_1.pay(43)
client_2.pay(100)
for men in clients:
    print(men.get_balance())

