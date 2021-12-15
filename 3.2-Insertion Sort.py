
#Insertion Sort

def insertion_sort(list_a):
    indexing_length = range(1, len(list_a))
    for i in indexing_length:
        value_to_sort = list_a[i]

        while list_a[i-1] > value_to_sort and i >0:
            list_a[i], list_a[i-1] = list_a[i-1], list_a[i]
            i -=1
        
    return list_a

list_a=[12,5,54,3,1,7,4,689,47]

print(insertion_sort(list_a))