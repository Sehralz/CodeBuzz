def matrix_zeros(matrix):
    rows = len(matrix)
    print(rows)
    cols = len(matrix[0])
    print(cols)
    zero_rows = set()
    zero_cols = set()

    for row in range(rows):
        for col in range(cols):
            if (matrix[row][col]) == 0 :
                zero_rows.add(row)
                zero_cols.add(col)

    print(zero_rows,zero_cols)
    for row in range(rows):
        for col in range(cols):
            if row in zero_rows or col in zero_cols:
                matrix[row][col] = 0
    return matrix
def main():
    matrix = [[1,0,1],[1,1,1],[1,1,0]]
    result = matrix_zeros(matrix)
    print(f"Matrix Zeros = {result}")

if __name__ == '__main__':
    main()