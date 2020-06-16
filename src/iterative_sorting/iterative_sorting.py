# TO-DO: Complete the selection_sort() function below
lst = [32, 5, 7, 3]


def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr)):
        smallest_index = i

        for j in range(i + 1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr


selection_sort(lst)
print(lst)

# TO-DO:  implement the Bubble Sort function below
lst = [23, 5, 4, 78, 12]


def bubble_sort(arr):
    # Your code here
    # starting from i = 0, compare i and i+1.
    # If i is greater than i+1, swap their positions.( arr[i] = arr[i+1], arr[i+1] = arr[i] )
    # else, move to the next pair.
    # If at least one swap, repeat.
    swap = True
    while swap:
        count = 0
        for i in range(0, len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                count += 1
        if count == 0:
            swap = False
    return arr


tola = bubble_sort(lst)
print(tola)


'''
STRETCH: implement the Count Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''


def counting_sort(arr, maximum=None):
    # Your code here

    return arr
