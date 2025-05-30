class bank:
    my_bank = "Habib Bank"

    @classmethod

    def change_bank(self,name):
        self.my_bank = name
b1 = bank()
print(bank.my_bank)
bank.change_bank("State Bank of pakistan")
print(b1.my_bank)



