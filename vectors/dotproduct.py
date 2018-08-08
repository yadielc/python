def dot_prod(v1, v2):
    #check if the vectors have the same length
    if len(v1) != len(v2):
        print("error! Vectors must have same length")

    result = 0
    for i in range(len(v1)):
        value_1 = v1[i]
        value_2 = v2[i]
        result += value_1 * value_2
    return result

# 2 test vectors
vector_1 = [7,2,3]
vector_2 = [1, 10, 4]


v1_dot_v2 = dot_product(vector_1, vector_2)


print(vector_1, "dot", vector_2, "equals", v1_dot_v2)
