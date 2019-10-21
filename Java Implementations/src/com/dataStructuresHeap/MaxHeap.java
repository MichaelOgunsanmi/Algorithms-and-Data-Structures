package com.dataStructuresHeap;

public class MaxHeap {
    public static void heapify(int[] array){
        var lastPossibleParentIndex = (array.length / 2) - 1;
        for (int i = lastPossibleParentIndex; i >= 0; i--)
            heapify ( array, i );
    }

    private static void heapify ( int[] array, int parentIndex ) {
        var largerIndex = parentIndex;

        var leftIndex = parentIndex * 2 + 1;
        if(leftIndex < array.length && array[leftIndex] > array[largerIndex])
            largerIndex = leftIndex;

        var rightIndex = parentIndex * 2 + 2;
        if (rightIndex < array.length && array[rightIndex] > array[largerIndex])
            largerIndex = rightIndex;

        if (largerIndex == parentIndex)
            return;

        swap ( array, parentIndex, largerIndex );
        heapify ( array, largerIndex );


    }

    public static int getKthLargest(int[] array, int k){
        if (k < 1 || k > array.length)
            throw new IllegalArgumentException ();

        var heap = new Heap();
        for (var number : array)
            heap.insert ( number );

        for (int i = 0; i < k - 1; i++)
            heap.remove ();

        return heap.max ();
    }

    private static void swap ( int[] array, int firstIndex, int secondIndex ){
        var temp = array[firstIndex];
        array[firstIndex] = array[secondIndex];
        array[secondIndex] = temp;
    }


}
