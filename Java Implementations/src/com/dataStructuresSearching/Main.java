package com.dataStructuresSearching;

public class Main {
    public static void main ( String[] args ) {
//        //LinearSearch
//        int[] numbers = {7,12,22,70,10,3,1};
//        Search search = new Search ();
//        var index = search.linearSearch ( numbers, 10 );
//        System.out.println (index );

//        //BinarySearch Recursive
//        int[] numbers = {1,3,5,6,7};
//        Search search = new Search ();
//        var index = search.binarySearchRec ( numbers, 5 );
//        System.out.println (index );

//        //BinarySearch Iterative
//        int[] numbers = {1,3,5,6,7};
//        Search search = new Search ();
//        var index = search.binarySearch( numbers, 70 );
//        System.out.println (index );

//        //TenarySearch
//        int[] numbers = {1,3,5,6,7};
//        Search search = new Search ();
//        var index = search.tenarySearch ( numbers, 6 );
//        System.out.println (index );

//        //JumpSearch
//        int[] numbers = {1,3,5,6,7};
//        Search search = new Search ();
//        var index = search.jumpSearch ( numbers, 1 );
//        System.out.println (index );


        //ExponentialSearch
        int[] numbers = {1,3,5,6,7};
        Search search = new Search ();
        var index = search.exponentialSearch ( numbers, 3 );
        System.out.println (index );
    }
}
