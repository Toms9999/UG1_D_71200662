a = str(input('Kalimat yang ingin diteliti : '))
b = str(input('Kata yang di cari : '))

for i in a :
    a = a.count(b)
    print('\nJumlah kata yang di cari :', a)
    break
