package com.dataStructuresHeap;

import java.util.Arrays;

public class Main {
    public static void main ( String[] args ) {
//        Heap heap = new Heap ();
//
//        heap.insert ( 10 );
//        heap.insert ( 5 );
//        heap.insert ( 17 );
//        heap.insert ( 4 );
//        heap.insert ( 22 );
//        System.out.println (heap.remove () );
//
//        //Using heaps for heap sort;
//        int[] numbers = {2,5,12,67,6,5,18,20,19};
//        Heap heapSort = new Heap ();
//
//        //Sprting in descending order;
//        for (int number : numbers)
//            heapSort.insert ( number );
//
//        for (int i = 0; i < numbers.length; i++)
//            numbers[i] = heapSort.remove ();
//
//        System.out.println ( "Descending order " + Arrays.toString ( numbers ) );
//
//        //Sorting in ascending order
//        for (int number : numbers)
//            heapSort.insert ( number );
//
//        for (int i = numbers.length - 1; i >= 0 ; i--)
//            numbers[i] = heapSort.remove ();
//
//        System.out.println ( "Ascending order " +Arrays.toString ( numbers ) );

////        Heapify Question;
        int[] numbers = {5,3,8,4,1,2};
        MaxHeap.heapify ( numbers );
        System.out.println (Arrays.toString ( numbers ) );
        System.out.println (Heap.isMaxHeap ( numbers ) ); //true

//        KthLargestElement Question;
        int[] numbers2 = {5,3,8,4,1,2};
        System.out.println (MaxHeap.getKthLargest ( numbers2, 1 ) );
        System.out.println ( Arrays.toString ( numbers2 ) );
        System.out.println (Heap.isMaxHeap ( numbers2 ) ); //false

    }
}
