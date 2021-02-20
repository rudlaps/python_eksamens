skaitli = [int(sk) for sk in input("Ievadi 10 skaitļus ar atstarpi: ").split()]

summa = 0

for skaitlis in skaitli:
    summa += skaitlis

print(summa)