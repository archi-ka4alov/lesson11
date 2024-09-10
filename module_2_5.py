def get_matrix(n, m, value):
    column = []
    result_list = []
    for j in range(m):
        column.append(value)
    for i in range(n):
        result_list.append(column)
    return result_list

result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)