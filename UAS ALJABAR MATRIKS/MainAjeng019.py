import Ajeng019


def input_matriks(nama):
    print(f"\nMasukkan Matriks {nama} (3x3)")
    matriks = []

    for i in range(3):
        baris = []
        for j in range(3):
            angka = float(input(f"Elemen [{i+1}][{j+1}] : "))
            baris.append(angka)
        matriks.append(baris)

    return matriks


def tampilkan_matriks(M):
    for baris in M:
        for nilai in baris:
            print(f"{nilai:10.2f}", end="")
        print()


while True:
    print("\n" + "=" * 40)
    print("PROGRAM OPERASI MATRIKS")
    print("=" * 40)
    print("1. Perkalian Matriks")
    print("2. Transpose Matriks")
    print("3. Inverse Matriks")
    print("4. Keluar")
    print("=" * 40)

    pilihan = input("Pilih menu (1-4): ")

    if pilihan == "1":
        print("\n PERKALIAN MATRIKS ")

        A = input_matriks("A")
        B = input_matriks("B")

        hasil = Ajeng019.perkalian_matriks(A, B)

        print("\nHasil Perkalian:")
        tampilkan_matriks(hasil)

    elif pilihan == "2":
        print("\n TRANSPOSE MATRIKS ")

        A = input_matriks("A")

        hasil = Ajeng019.transpose(A)

        print("\nHasil Transpose:")
        tampilkan_matriks(hasil)

    elif pilihan == "3":
        print("\n INVERSE MATRIKS ")

        A = input_matriks("A")

        hasil = Ajeng019.inverse_3x3(A)

        if hasil is None:
            print("\nMatriks tidak memiliki invers karena determinannya = 0")
        else:
            print("\nHasil Inverse:")
            tampilkan_matriks(hasil)

    elif pilihan == "4":
        print("\nTerima kasih telah menggunakan program.")
        break

    else:
        print("\nPilihan tidak valid!")