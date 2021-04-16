#Buatlah 1 program menggunakan fungsi Numerik (Min 3 jenis fungsi numerik)
import math

def fungsinumerik(x,v):
    print('\nKeadaan awal =', x, '&', v)
    print('\nSetelah diberikan fungsi numerik jenis abs')
    y=abs(x)
    c=abs(v)
    print('|%d| ='%x,y)
    print('|%d| ='%v,c)
    print('\nSetelah diberikan fungsi numerik jenis ceil')
    o=math.ceil(x)
    j=math.ceil(v)
    print(o)
    print(j)
    print('\nSetelah diberikan fungsi numerik jenis min & max')
    p=min(x, v)
    l=max(x, v)
    print('nilai min = ',p)
    print('nilai max = ', l)
    print('\nSetelah diberikan fungsi numerik jenis floor')
    t=math.floor(x)
    b=math.floor(v)
    print(t)
    print(b)


m=float(input('Masukkan angka pertama = '))
n=float(input('Masukkan angka kedua = '))
fungsinumerik(m,n)


