## What is recurrence for worst case of QuickSort and what is the time complexity in Worst case?

1. Recurrence is T(n) = T(n-2) + O(n) and time complexity is O(n^2)
2. Recurrence is T(n) = T(n-1) + O(n) and time complexity is O(n^2)
3. Recurrence is T(n) = 2T(n/2) + O(n) and time complexity is O(nLogn)
4. Recurrence is T(n) = T(n/10) + T(9n/10) + O(n) and time complexity is O(nLogn)

ANSWER: 2

The worst case of QuickSort occurs when the picked pivot is always one of the corner elements in sorted array. 
In worst case, QuickSort recursively calls one subproblem with size 0 and other subproblem with size (n-1). So recurrence is T(n) = T(n-1) + T(0) + O(n).
The above expression can be rewritten as T(n) = T(n-1) + O(n).

## Suppose we have a O(n) time algorithm that finds median of an unsorted array. Now consider a QuickSort implementation where we first find median using the above algorithm, then use median as pivot. What will be the worst case time complexity of this modified QuickSort?

1. O(n^2 Logn)
2. O(n^2)
3. O(n Logn Logn)
4. O(nLogn)

ANSWER: 4

If we use median as a pivot element, then the recurrence for all cases becomes T(n) = 2T(n/2) + O(n) The above recurrence can be solved using Master Method. It falls in case 2 of master method.


## Which of the following is not a stable sorting algorithm in its typical implementation?

1. Insertion Sort
2. Merge Sort
3. Quick Sort
4. Bubble Sort

ANSWER: 3


## Which of the following sorting algorithms in its typical implementation gives best performance when applied on an array which is sorted or almost sorted (maximum 1 or two elements are misplaced)?

1. Quick Sort
2. Heap Sort
3. Merge Sort
4. Insertion Sort

ANSWER: 4

Insertion sort takes linear time when input array is sorted or almost sorted (maximum 1 or 2 elements are misplaced). All other sorting algorithms mentioned above will take more than lienear time in their typical implementation.


## Which sorting algorithms is most efficient to sort string consisting of ASCII characters?

1. Quick Sort
2. Heap Sort
3. Merge Sort
4. Counting Sort

ANSWER: 4

Counting sort algorithm is efficient when range of data to be sorted is fixed. In the above question, the range is from 0 to 255(ASCII range). Counting sort uses an extra constant space proportional to range of data.





