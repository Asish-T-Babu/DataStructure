unsorted_list = [6,7,8,5,4]
for i in range(len(unsorted_list)-1):
    min = i
    for j in range (i,len(unsorted_list)):
        if unsorted_list[i]>unsorted_list[j]:
            min = j
    if min != i:
        unsorted_list[i], unsorted_list[min] = unsorted_list[min], unsorted_list[i]

print(unsorted_list)