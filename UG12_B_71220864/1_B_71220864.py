print("SELAMAT DATANG DI PROGRAM PEMBUAT PIRAMIDA BERULANG")
Q = int(input("Masukkan Angka : "))
print (" "*(Q-1),("*"))
for W in range ((Q-1),1,-1):
    print(' '*(W-1),"**")
print("**"*Q)
