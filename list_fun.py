marketing_list = [4, 55, 64, 32, 16, 32, 12, 13, 87, 63, 64, 64, 72, 71, 89, 88]

element_index = 0
for element in marketing_list:
    print(f"This is the element: {element}")
    x = marketing_list.index(element)
    element_index = x
    for e in marketing_list[element_index + 1:]:
        print(f"This is e: {e}")
        if e == element:
            marketing_list.remove(e)

print(marketing_list)
