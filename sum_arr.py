def sum_arr(mat_1, mat_2, size):
    mat_rezult = []
    for i in range(size):
        mat_rezult.append(mat_1[i]+mat_2[i])
    return mat_rezult

if __name__ == "__main__":
    mat_1 = [1, 2, 3, 4]
    mat_2 = [5, 1, 2, 3]
    size = 4
    print (sum_arr(mat_1, mat_2, size))
