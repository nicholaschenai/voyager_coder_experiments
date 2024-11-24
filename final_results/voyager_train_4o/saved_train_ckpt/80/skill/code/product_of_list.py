

def product_of_list(int_list):
    if (not int_list):
        return 1
    product = 1
    for num in int_list:
        product *= num
    return product
