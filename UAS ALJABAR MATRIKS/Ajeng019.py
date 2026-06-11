def perkalian_matriks(A, B):
    baris_A = len(A)
    kolom_A = len(A[0])
    kolom_B = len(B[0])

    hasil = [[0 for _ in range(kolom_B)] for _ in range(baris_A)]

    for i in range(baris_A):
        for j in range(kolom_B):
            for k in range(kolom_A):
                hasil[i][j] += A[i][k] * B[k][j]

    return hasil


def transpose(A):
    baris = len(A)
    kolom = len(A[0])

    hasil = [[0 for _ in range(baris)] for _ in range(kolom)]

    for i in range(baris):
        for j in range(kolom):
            hasil[j][i] = A[i][j]

    return hasil


def determinan_3x3(A):
    return (
        A[0][0] * (A[1][1] * A[2][2] - A[1][2] * A[2][1])
        - A[0][1] * (A[1][0] * A[2][2] - A[1][2] * A[2][0])
        + A[0][2] * (A[1][0] * A[2][1] - A[1][1] * A[2][0])
    )


def inverse_3x3(A):
    det = determinan_3x3(A)

    if det == 0:
        return "Matriks tidak memiliki invers"

    kofaktor = [
        [
            (A[1][1] * A[2][2] - A[1][2] * A[2][1]),
            -(A[1][0] * A[2][2] - A[1][2] * A[2][0]),
            (A[1][0] * A[2][1] - A[1][1] * A[2][0])
        ],
        [
            -(A[0][1] * A[2][2] - A[0][2] * A[2][1]),
            (A[0][0] * A[2][2] - A[0][2] * A[2][0]),
            -(A[0][0] * A[2][1] - A[0][1] * A[2][0])
        ],
        [
            (A[0][1] * A[1][2] - A[0][2] * A[1][1]),
            -(A[0][0] * A[1][2] - A[0][2] * A[1][0]),
            (A[0][0] * A[1][1] - A[0][1] * A[1][0])
        ]
    ]

    adjoint = transpose(kofaktor)

    inverse = [
        [adjoint[i][j] / det for j in range(3)]
        for i in range(3)
    ]

    return inverse