from random import sample


def get_random_elements (number_list, elements=1):
    try:
        return sample(number_list,elements)
    except Exception:
        return ("No way to do this!")



print(get_random_elements([1,2,6,3,7])) # [2]
print(get_random_elements([1,2,6,3,7],3)) # [6,2,7]
print(get_random_elements([1,2,6,3,7],16)) # Wyjątek!
print(get_random_elements([1,2,6,3,7],-1)) # Wyjątek!
print(get_random_elements([1,2,6,3,7],"d")) # Wyjątek!
print(get_random_elements([1,2,6,3,7],0.5)) # Wyjątek!