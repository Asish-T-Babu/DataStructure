unsorted_list = [5,2,6,7,8,1,0]
for i in range(len(unsorted_list)):
    for j in range(len(unsorted_list)-i-1):
        if unsorted_list[j]>unsorted_list[j+1]:
            unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]

print("sorted list :", unsorted_list)

# Time Complexity = o(n^2)
