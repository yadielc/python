def add_vectors(vector_1, vector_2):
    if len(vector_1) != len(vector_2):
        print("Error! vectors must be same size to add")
        return

    new_vector = []
    for i in range(len(vector_1)):
        value_1 = vector_1[i]
        value_2 = vector_2[i]
        new_val = value_1 + value_2
        new_vector.append(new_val)

    return new_vector

v1 = [1,2]
v2 = [3,4]

v_1_plus_2 = add_vectors(v1, v2)

print(v1, "plus", v2, "equals", v_1_plus_2)
