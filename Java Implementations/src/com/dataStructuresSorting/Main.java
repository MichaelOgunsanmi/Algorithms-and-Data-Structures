package com.dataStructuresSorting;

import java.util.Arrays;

public class Main {
    public static void main ( String[] args ) {
        int[] numbers = {2,88,23,11,345,12,12,6,1,9,0,777};

////        BubbleSort
//        BubbleSort sorter = new BubbleSort ();
//        sorter.sort ( numbers );
//        System.out.println ( Arrays.toString ( numbers ) );

////        SelectionSort
//        SelectionSort sorter = new SelectionSort ();
//        sorter.sort ( numbers );
//        System.out.println ( Arrays.toString ( numbers ) );

// //        InsertionSort
//        InsertionSort sorter = new InsertionSort ();
//        sorter.sort ( numbers );
//        System.out.println ( Arrays.toString ( numbers ) );

////        MergeSort
//        MergeSort sorter = new MergeSort ();
//        sorter.sort ( numbers );
//        System.out.println ( Arrays.toString ( numbers ) );

////        QuickSort
//        QuickSort sorter = new QuickSort ();
//        sorter.sort ( numbers );
//        System.out.println ( Arrays.toString ( numbers ) );

////        CountSort
//        int[] countSort = {2,2,4,2,1,1,5,6,6,7,7,7,7,3,1,2};
//        CountingSort sorter = new CountingSort ();
//        sorter.sort ( countSort, 7 );
//        System.out.println ( Arrays.toString ( countSort ) );

//        BucketSort
        int [] bucketSort = {7,1,3,5,3}; //Note that items to be sorted must be <= numberOfBuckets upon division;
        BucketSort sorter = new BucketSort ();
        sorter.sort ( bucketSort, 3 );
        System.out.println ( Arrays.toString ( bucketSort ) );


    }
}
