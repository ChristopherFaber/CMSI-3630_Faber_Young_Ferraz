    # DATA STRUCTURE HOMEWORK # 

'''
1. Another kind of simple sort is the odd-even sort. The idea is to repeatedly make two passes through an array.
On the first pass you look at all the pairs of items, a[j] and a[j+1], where j is odd (j = 1, 3, 5, …).
If their key values are out of order, you swap them. On the second pass you do the same for all the even values (j = 2, 4, 6, …). 
You do these two passes repeatedly until the array is sorted.
Replace the bubbleSort() method in bubbleSort.java [Listing 3.1] with an oddEvenSort() method. 
Make sure it works for varying amounts of data. You'll need to figure out how many times to do the two passes. 
The odd-even sort is actually useful in a multiprocessing environment, in which a separate processor can operate on each odd pair simultaneously and then on each even pair.
Because the odd pairs are independent of each other, each pair can be checked – and swapped, if necessary – by a different processor. This makes for a very fast sort.

'''



def bubble_sort( a ):
      for i in range( len( a ) ):
         for j in range( 0, len( a ) - i - 1 ):
            if( a[j] > a[j + 1] ):
               # swap integers:
               temp = a[j+1]
               a[j+1] = a[j]
               a[j] = temp
      return

def E_O_Sort(a):
    # CHECK IF LIST HAS A EVEN OR ODD NUMBER OF ELEMENTS:
        # if even, then there are the same number of odd and even indexes, else there is one less odd index. 
        for i in range(2, len(a), 2): 
            # SORT EVEN INDEXES
            for j in range(2, len(a), 2):
                if a[j-2] > a[j] :
                    temp = a[j-2]
                    a[j-2] = a[j]
                    a[j] = temp
            # SORT ODD INDEXES:
            for j in range(3,len(a), 2):
                if a[j-2] > a[j] :
                    temp = a[j-2]
                    a[j-2] = a[j]
                    a[j] = temp
        return


def oddEvenSort(a):
    for i in range(len(a)):
        for j in range(0,len(a)-1,2):
            if a[j] > a[j+1] :
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp
        for j in range(1,len(a)-1,2):
            if a[j] > a[j+1] :
                temp = a[j+1]
                a[j+1] = a[j]
                a[j] = temp

l1 = [7,4, 3,70, -1,6,15]
print("this is the list: ", l1)
bubble_sort(l1)
print("this is the sorted list", l1)
l2 = [7, 4,3, 70, -1,6,15]
oddEvenSort(l2)
print("this is the sorted list using the even odd sorter :)", l2)



