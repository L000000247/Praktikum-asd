##Quiz Praktikum ASD L200200247
import re

#no 1
pola = '@+[a-z]+[0-9]_?'
username = input('Masukkan Username: ')

if re.findall(pola, username):
    print('PASS')
else:
    print('FAILED')


#no 2
pola = '[a-zA-Z0-9]+[@]+[a-zA-Z0-9]+[.]+[a-zA-Z0-9]+'
##masukkan teks
inputan = input('Cetak email dari teks: ')

cocok = re.findall(pola, inputan)
print(cocok)
    

