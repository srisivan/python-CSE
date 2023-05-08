m,n = input("\n\nEnter the order of the matrix m x n: ").split(",")

m = int(m)
n = int(n)

def define_matrix(rows, columns):

    mat = []

    for i in range(rows):
        r = []

        for j in range(columns):
            r.append(int(input()))

        mat.append(r)


    return mat

def display_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end = " ")

        print()


def transpose_matrix(matrix):
    result = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

    return result


def add_matrix(mat_a, mat_b):
    if ((len(mat_a) != len(mat_b)) or (len(mat_a[0]) != len(mat_b[0]))):
        print("Matrices must be of same dimensions.\n")
        exit()

    sum = [[(mat_a[i][j] + mat_b[i][j]) for j in range(len(mat_a))] for i in range(len(mat_a[0]))]

    return sum

print("\nElements for matrix a: \n")
A = define_matrix(m, n)

print("\nElements for matrix b: \n")
B = define_matrix(m, n)


print("\nMatrix A: \n")
display_matrix(A)

print("\nMatrix B: \n")
display_matrix(B)

add = add_matrix(A, B)

print("\nSum of A and B: \n")
display_matrix(add)
