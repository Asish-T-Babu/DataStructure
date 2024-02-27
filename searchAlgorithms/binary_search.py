sorted_list = [1,2,3,4,5,6,7,8,9]
search_element = int(input('Enter the element to search: '))
l, r = 0, len(sorted_list)
flag = 0
while(l<r):
    m = (l + r) //2
    if sorted_list[m] == search_element:
        print(f'Element found at position {m}')
        flag = 1
        break
    elif sorted_list[m] > search_element:
        r = m - 1
    else:
        l = m + 1
if flag == 0:
    print('element not found')