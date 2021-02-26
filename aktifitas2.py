#OPERATOR
bil1=int(input("masukkan angka pertama:2"))
bil2=int(input("masukkan angka kedua:4"))

jumlah=bil1+bil2
kurang=bil1-bil2
kali=bil1*bil2
bagi=bil1/bil2
modulus=bil1%bil2

ptint("hasil dari %d + %d = %d" %(bil1, bil2, jumlah))
ptint("hasil dari %d - %d = %d" %(bil1, bil2, kurang))
ptint("hasil dari %d * %d = %d" %(bil1, bil2, kali))
ptint("hasil dari %d / %d = %d" %(bil1, bil2, bagi))
ptint("hasil dari %d mod %d = %d" %(bil1, bil2, modulus))