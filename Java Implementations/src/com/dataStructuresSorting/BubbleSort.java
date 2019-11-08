package com.dataStructuresSorting;

public class BubbleSort {
    public void sort(int[] array){
        boolean isSorted;

        for (int i = 0; i < array.length; i++) {
            isSorted = true;
            for (int j = 1; j < array.length - i; j++) {
                if (array[j] < array[j-1]){
                    swap ( array, j-1, j );
                    isSorted = false;
                }
            }

            if (isSorted)
                return;
        }
    }

    private void swap ( int[] array, int firstIndex, int secondIndex ) {
        var temp = array[secondIndex];
        array[secondIndex] = array[firstIndex];
        array[firstIndex] = temp;
    }
}
