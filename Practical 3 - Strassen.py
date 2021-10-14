print("Enter values for 2x2 matrix : ")
print("matrix a")
n1=int(input("Enter value for A : "))
n2=int(input("Enter value for B : "))
n3=int(input("Enter value for C : "))
n4=int(input("Enter value for D : "))
print("matrix b")
n5=int(input("Enter value for E : "))
n6=int(input("Enter value for F : "))
n7=int(input("Enter value for E : "))
n8=int(input("Enter value for F : "))
def StrassenMatrixM(a, b):
    """
    Only for 2x2 matrices
    """
    if len(a) != 2 or len(a[0]) != 2 or len(b) != 2 or len(b[0]) != 2:
        raise Exception('Matrices should be 2x2!')
    print(a[0][0] * b[0][1] + a[0][1] * b[1][1])
    matrix = [[a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]],
                  [a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]]]

    return matrix


def add(a, b):
    # print(matrix_a)
    return [[a[row][col] + b[row][col]
             for col in range(len(a[row]))] for row in range(len(a))]


def subtract(a, b):
    return [[a[row][col] - b[row][col]
             for col in range(len(a[row]))] for row in range(len(a))]


def split(a):
    """
    Given a matrix, return the TOP_LEFT, TOP_RIGHT, BOT_LEFT and BOT_RIGHT quadrant
    """
    if len(a) % 2 != 0 or len(a[0]) % 2 != 0:
        raise Exception('Odd matrices are not supported!')
                                                                                                                                    
    length = len(a)
    mid = length // 2
    tLeft = [[a[i][j] for j in range(mid)] for i in range(mid)]
    bottom_left = [[a[i][j] for j in range(mid)] for i in range(mid, length)]

    tRight = [[a[i][j] for j in range(mid, length)] for i in range(mid)]
    bottom_right = [[a[i][j] for j in range(mid, length)] for i in range(mid, length)]

    return tLeft, tRight, bottom_left, bottom_right


def dimensions(matrix):
    return len(matrix), len(matrix[0])


def strassenMatx(a, b):
    """
    Recursive function to calculate the product of two matrices, using the Strassen Algorithm.
    Currently only works for matrices of even length (2x2, 4x4, 6x6...etc)
    """
    if dimensions(a) != dimensions(b):
        raise Exception(f'Both matrices are not the same dimension! \nMatrix A:{matrix_a} \nMatrix B:{matrix_b}')
    if dimensions(a) == (2, 2):
        return StrassenMatrixM(a, b)

    A, B, C, D = split(a)
    E, F, G, H = split(b)

    num1 = strassen(A, subtract(F, H))
    num2 = strassen(add(A, B), H)
    num3 = strassen(add(C, D), E)
    num4 = strassen(D, subtract(G, E))
    num5 = strassen(add(A, D), add(E, H))
    num6 = strassen(subtract(B, D), add(G, H))
    num7 = strassen(subtract(A, C),add(E, F))

    tLeft = add(subtract(add(num5, num4), num2), num6)
    tRight = add(num1,num2)
    bLeft = add(num3, num4)
    bRight = subtract(subtract(add(num1, num5), num3), num7)

    # construct the new matrix from our 4 quadrants
    new_matrix = []
    for i in range(len(tRight)):
        new_matrix.append(tLeft[i] + tRight[i])
    for i in range(len(bottom_right)):
        new_matrix.append(bottom_left[i] + bottom_right[i])
    return new_matrix


a = [[n1,n2],
    [n3,n4]]
b = [[n5,n6],
    [n7,n8]]
result = [[0,0],
             [0,0]]
for i in range(len(a)):
       # iterate through columns of Y
       for j in range(len(b[0])):
           # iterate through rows of Y
           for k in range(len(b)):
               result[i][j] += b[i][k] * b[k][j]
for r in result:
    print(r)

       


strassenMatx(a,b)
