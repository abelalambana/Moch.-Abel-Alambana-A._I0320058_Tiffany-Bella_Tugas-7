def panggil(func):
    return func
def helloworld():
    return 'HELLO WORLD'
def main():
    daftarnama=['Adi, Cahyo, budi, Dedi']
    print('Keadaan Awal')
    print(daftarnama)

    print('\n menggunakan sorted() : ')
    print(sorted(daftarnama))

    daftarnama.sort(key=lambda n: n.lower())

    print('\n Keadaan Akhir')
    print(daftarnama)
if __name__ == '__main__':
    main()