def list_filter(int_values, *element):

    for i in element:

        for j in int_values:
            if j%i==0:
                int_values.remove(j)

    return (int_values)


result = list_filter([1,8,15,20,11], 20)
print(result) # [1,8,15,11]
result = list_filter([1,8,15,20,11], 20,4)
print(result) # [1,15,11]
result = list_filter([1,8,15,20,11], 2, 5, 31)
print(result) # [1,11]