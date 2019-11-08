package com.dataStructuresSorting;

public class InsertionSort {
    public void sort(int[] array){
        for (int i = 1; i < array.length; i++) {
            var currentElement = array[i];
            var k = i - 1;

            while (k >= 0 && array[k] > currentElement){
                array[k+1] = array[k];
                k--;
            }

            array[k+1] = currentElement;
        }
    }
}
