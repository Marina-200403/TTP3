from random import randint

def generation_arr(size):
    mat = []
    for i in range(size):
        mat.append(randint(-10, 10))
    return mat
        
if __name__ == "__main__":
    print(generation_arr(3))