package com.dataStructuresSorting;

public class SelectionSort {
    public void sort(int[] array){
        for (int i = 0; i < array.length; i++) {
            var minIndex = i;
            for (int k = i; k < array.length; k++)
                if (array[k] < array[minIndex])
                    minIndex = k;

            swap(array, minIndex, i);
        }

    }

    private void swap ( int[] array, int firstIndex, int secondIndex ) {
        var temp = array[secondIndex];
        array[secondIndex] = array[firstIndex];
        array[firstIndex] = temp;
    }
}
