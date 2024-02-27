list1 = [5,4,3,6,7]
search_element = int(input('Enter the element to search: '))
for i in range(len(list1)):
    if list1[i] == search_element:
        print(f"element found in {i+1} position.")
        break
else:
    print('element not found')