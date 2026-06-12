def perkalian_matriks(A, B):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                hasil[i][j] += A[i][k] * B[k][j]

    return hasil


def transpose(A):
    hasil = [[0,0,0],[0,0,0],[0,0,0]]

    for i in range(3):
        for j in range(3):
            hasil[j][i] = A[i][j]

    return hasil