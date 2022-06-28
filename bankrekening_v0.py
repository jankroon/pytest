# Simple bank account that can store money, process deposits and withdrawals
# CopyLeft 2022: Hossein Chamani & Jan Kroon, Rotterdam University of Applied Sciences
# Inspired by Semaphore tutorial of Kevin Ndung'u Gathuku

class OnvoldoendeSaldoMelding(Exception):
    pass

class Bankrekening(object):
    def __init__(self, eerste_storting = 0):
        self.saldo = eerste_storting

    def opname(self, bedrag):
        if self.saldo < bedrag:
            raise OnvoldoendeSaldoMelding(f"De rekening heeft niet genoeg saldo om {bedrag} op te kunnen nemen.")
        else:
            self.saldo -= bedrag

    def storting(self, bedrag):
        self.saldo += bedrag

# User Interface
print("*** BaseCamp Bank ***")

hosseins_rekening = Bankrekening(150)
jans_rekening = Bankrekening()
hans_rekening = Bankrekening(500)

print("We beheren de volgende rekeningen: ")
print("    001: Hossein Chamani")
print("    007: Jan Kroon")
print("    999: Hans van Toor")
rekening_nummer = input("Welke rekening wilt u plunderen? ")
bedrag = int(input("Welk bedrag wilt u opnemen? "))

if rekening_nummer == "001":
    hosseins_rekening.opname(bedrag)
elif rekening_nummer == "007":
    jans_rekening.opname(bedrag)
elif rekening_nummer == "999":
    hans_rekening.opname(bedrag)
else:
    print("Dit rekening nummer bestaat niet in ons systeem")


