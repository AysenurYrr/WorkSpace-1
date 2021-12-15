"""
        7 1 5 3 9 8 2 0
    7 1 5 3       2 4 8 0
  7 1    5 3     2 4   8 0

  1 7    3 5     2 4   0 8
    1 3 5 7       0 2 4 8
        0 1 2 3 4 5 7 8
 

"""
#Merge Sort
def mergeSort(liste):
    if len(liste) > 1:
        mid = len(liste) // 2
        left = liste[:mid]
        right = liste[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        
        k = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
              
              liste[k] = left[i]
              
              i += 1
            else:
                liste[k] = right[j]
                j += 1
            # Diğer slota hareket ettir
            k += 1

        # Geri kalan değerler için
        while i < len(left):
            liste[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            liste[k]=right[j]
            j += 1
            k += 1

liste = [54,26,93,17,77,31,44,55,20]
mergeSort(liste)
print(liste)