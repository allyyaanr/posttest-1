#Allyya Nur Azizah
#POST TEST 1

listacak =  [12, 1, [22, 3, [8, 14]], 2, 6, [11], 90]
list1 =  listacak[0:2] 
list1a = listacak[3:5]
list1b = listacak[6:7]
list2 = listacak[2][0:2]
list3 = listacak[2][2][0:2]
list4 = listacak[5]

listurut = list1+list1a+list1b+list2+list3+list4
print(listurut)

import os
os.system('cls')

def mergesort(arr): #untuk membagi list
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2 #variable memecah list
    left = arr[:mid]
    right = arr[mid:]

    left = mergesort(left)
    right = mergesort(right)

    return merge (left,right)

def merge(left, right):
    result = [] #list kosong digunakan untuk menampung nilai

    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    if left:
        result += left
    elif right:
        result += right
    return result

listurut = list1+list1a+list1b+list2+list3+list4
hasil = mergesort(listurut)

print(listacak)
print (hasil)