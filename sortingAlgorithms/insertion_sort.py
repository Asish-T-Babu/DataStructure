unsorted_list = [5,3,4,8,7,1,2]
k=0
i=k
while i < len(unsorted_list)-1:
    j = i+1
    while(unsorted_list[i]>unsorted_list[j]):
        unsorted_list[i],unsorted_list[j] = unsorted_list[j],unsorted_list[i]
        if i!=0:
            j=j-1
            i=i-1        
    k+=1
    i=k

print('sorted_list: ',unsorted_list)

# Time complexity = O(n^2) - worst case