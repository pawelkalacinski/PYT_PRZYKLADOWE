def count_char(my_text,letter):
    out = my_text.lower()
    number_lower = out.count(letter)

    out1 = my_text.upper()
    number_upper = out1.count(letter)

    number_sum = number_lower + number_upper

    return (number_sum)




n = count_char("Ala ma kotA",'a')
print(n) # 4
n = count_char("ala ma kota",'A')
print(n) # 4
n = count_char("Python is easy",'a')
print(n) # 1