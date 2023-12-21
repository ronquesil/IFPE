def find_max_min(matrix):
    max_value = matrix[0][0]
    min_value = matrix[0][0]
    max_position = (0, 0)
    min_position = (0, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > max_value:
                max_value = matrix[i][j]
                max_position = (i, j)
            if matrix[i][j] < min_value:
                min_value = matrix[i][j]
                min_position = (i, j)

    return max_value, max_position, min_value, min_position

def main():
    M, N = map(int, input().split())
    
    print()
    matrix = []
    for _ in range(M):
        row = list(map(int, input().split()))
        matrix.append(row)

    max_value, max_position, min_value, min_position = find_max_min(matrix)

    print(f"MAIOR = {max_value} - POSIÇÃO = {max_position}")
    print(f"MENOR = {min_value} - POSIÇÃO = {min_position}")

if __name__ == "__main__":
    main()
