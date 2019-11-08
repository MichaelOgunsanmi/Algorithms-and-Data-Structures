package com.dataStructuresSearching;

public class Search {
    public int linearSearch(int[] array, int target){
        for (int i = 0; i < array.length; i++)
           if (array[i] == target)
               return i;

        return -1;
    }

    public int binarySearchRec(int[] array, int target){
        return binarySearchRec ( array, target, 0, array.length - 1 );
    }

    private int binarySearchRec ( int[] array, int target, int left, int right) {
        if (right < left)
            return -1;

        int middle = (left + right) / 2;

        if (array[middle] == target)
            return middle;

        if (target < array[middle])
            return binarySearchRec ( array, target, left, middle - 1 );

        return binarySearchRec ( array, target, middle + 1, right );
    }

    public int binarySearch(int[] array, int target){
        var leftIndex = 0;
        var rightIndex = array.length - 1;

        while (leftIndex <= rightIndex){
            var middleIndex = (leftIndex + rightIndex) / 2;

            if (array[middleIndex] == target)
                return middleIndex;

            if (target < array[middleIndex])
                rightIndex = middleIndex - 1;
            else
                leftIndex = middleIndex + 1;
        }

        return -1;
    }

    public int tenarySearch(int[] array, int target){
        return tenarySearch ( array, target, 0, array.length - 1 );
    }

    private int tenarySearch(int[] array, int target, int leftIndex, int rightIndex){
        if (leftIndex > rightIndex)
            return -1;

        int partitionSize = (rightIndex - leftIndex) / 3;
        int firstMidPoint = leftIndex + partitionSize;
        int secondMidPoint = rightIndex - partitionSize;

        if (array[firstMidPoint] == target)
            return firstMidPoint;

        if (array[secondMidPoint] == target)
            return secondMidPoint;

        if (target < array[firstMidPoint])
            return tenarySearch ( array, target, leftIndex, firstMidPoint - 1 );

        if (target > array[secondMidPoint])
            return tenarySearch ( array, target, secondMidPoint + 1, rightIndex );

        return tenarySearch ( array, target, firstMidPoint + 1, secondMidPoint - 1 );
    }

    public int jumpSearch(int[] array, int target){
        int blockSize = (int) Math.sqrt(array.length);
        int start = 0;
        int next = blockSize;

        while (start < array.length && array[next - 1] < target){
            start = next;
            next += blockSize;
            if (next > array.length)
                next = array.length;
        }

        for( var i = start; i < next; i++){
            if (array[i] == target)
                return i;
        }

        return -1;
    }

    public int exponentialSearch(int[] array, int target){
        int bound = 1;
        while (bound < array.length && array[bound] < target)
            bound *= 2;

        int leftIndex = bound / 2;
        int rightIndex = Math.min ( bound, array.length - 1 );

        return binarySearchRec ( array, target, leftIndex, rightIndex );
    }

}
