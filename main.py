import Functions
from account import Account

client1 = Account('João', 123, 750, 1000.0 )
client1.deposit(1000)
client1.withdrawMoney(50)
client1.accountStatement()
Functions.line()
client2 = Account('Alex', 234, 1000, 3000)
client2.accountStatement()
Functions.line()
client1.transfer(client2, 30000)
Functions.line()
client1.accountStatement()
Functions.line()
client2.accountStatement()