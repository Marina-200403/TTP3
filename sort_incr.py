def sort_incr(mat):
    size = len(mat)
    for i in range (size):
        for j in range(size-i-1):
            if mat[j]<mat[j+1]:
                mat[j], mat[j+1] = mat[j+1], mat[j]
    return mat

if __name__ == "__main__":
    mat = [4, 6, 2, 1, 8, 3057, 0]
    print(sort_incr(mat))
    