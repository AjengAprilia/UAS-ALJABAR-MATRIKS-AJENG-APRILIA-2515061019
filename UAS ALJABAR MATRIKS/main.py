import Ajeng019

print("Masukkan Matriks A")
A = [list(map(float, input().split())) for _ in range(3)]

print("Masukkan Matriks B")
B = [list(map(float, input().split())) for _ in range(3)]

print("\n1. Perkalian Matriks")
print("2. Transpose Matriks")

pilih = input("Pilih menu: ")

if pilih == "1":
    print("\nHasil Perkalian:")
    print(Ajeng019.perkalian_matriks(A, B))

elif pilih == "2":
    print("\nHasil Transpose:")
    print(Ajeng019.transpose(A))

else:
    print("Pilihan tidak valid")