A = [[1,2,3],[4,5,6]]

B = [[1,2],[3,4],[5,6]]


def get_row(A,i):
    return A[i]

print(get_row(A,0))

def get_column(A,j):
    return [A_i[j] for A_i in A]

print(get_column(A,0))

def make_matrix(num_rows, num_cols, entry_fn):
    return [[entry_fn(i,j) for j in range(num_cols)] for i in range(num_rows)]

def is_diagonal(i,j):
    return 1 if i==j else 0

identity_matrix = make_matrix(5,5,is_diagonal)
print(identity_matrix)

