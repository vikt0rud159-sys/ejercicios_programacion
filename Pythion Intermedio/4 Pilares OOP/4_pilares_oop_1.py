class BankAccount:
	def __init__(self):
		while True:
			try:
				self.min_balance = float(input("Ingrese saldo mínimo: "))
				self.balance = 0.0
				return
			except ValueError:
				print("   ¡Debe ser un numero!\n")
	
	def substract_balance(self):
		while True:
			try:
				amount = float(input("Cantidad a sustraer: "))
				if amount <= 0:
					raise ValueError
				self.amount = amount
				print()
				return
			except ValueError:
				print("   ¡Debe ser un numero (Positivo)!\n")
    
	def add_balance(self):
		while True:
			try:
				amount = float(input("Cantidad a añadir: "))
				if amount <= 0:
					raise ValueError
				self.balance += amount
				print()
				return
			except ValueError:
				print("   ¡Debe ser un numero (Positivo)!\n")

class SavingsAccount(BankAccount):
	def check_min_balance(self):
		if (self.balance - self.amount) < self.min_balance:
			print("   ¡Saldo insuficiente!\n")
		else:
			self.balance -= self.amount


def program():
    bank_account = SavingsAccount()
    while True:
        print(f"Saldo actual = {bank_account.balance}")
        operation = input("[Sustraer saldo (1)] [Añadir saldo(2)]   ")
        if operation == "1":
            bank_account.substract_balance()
            bank_account.check_min_balance()
        elif operation == "2":
            bank_account.add_balance()
        else:
            print("   ¡Valor no válido!\n")


program()