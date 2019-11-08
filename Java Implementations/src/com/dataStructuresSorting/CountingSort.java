package com.dataStructuresSorting;

public class CountingSort {
    public void sort(int[] array, int max){
        int[] counts = new int[max + 1];

        for (int item : array)
            counts[item]++;

        var k = 0;
        for (int i = 0; i < counts.length; i++)
            for (var j = 0; j < counts[i]; j++)
                array[k++] = i;
    }
}
