package com.dataStructuresHashTables;

import java.sql.SQLOutput;
import java.util.*;

public class Main {
    public static void main(String[] args) {
////        Using inbuilt HashMap
//        Map<Integer, String> map = new HashMap<>();
//        map.put(1, "Hally");
//        map.put(3,"Rose");
//        map.put(2, "Buckley");
//        map.put(11, "Error state");
//        System.out.println(map);
//
//        map.remove(11);
//        System.out.println(map);
//
//        System.out.println(map.get(3));
//        System.out.println(map.containsKey(12));
//        System.out.println(map.containsValue("rose"));
//
//        for (int key: map.keySet())
//            System.out.println(key);
//
//        for (Map.Entry<Integer, String> keyValue: map.entrySet()) {
//            System.out.println(keyValue.getKey());
//            System.out.println(keyValue.getValue());
//        }

////        Using Inbuilt set implementation;
//        Set<Integer> set = new HashSet<>();
//        int [] numbers = {1,2,3,3,2,1,4,4,5,2,6,6,5,7,9};
//        for (var number: numbers)
//            set.add(number);
//        System.out.println(set);

////        Using custom built hashTable;
//        HashTable hashTable = new HashTable();
//        hashTable.put(6, "A");
//        hashTable.put(8, "B");
//        hashTable.put(11, "C");
//        System.out.println("Get");   //Use Debugger to see how result changes;
//        hashTable.put(6, "A+");
//        System.out.println("Put");
//        System.out.println(hashTable.get(6));
//        hashTable.remove(6);
//        System.out.println("Remove");
//        System.out.println(hashTable.get(10));

//        Exercises;
//        int [] mostFrequent = {1,1,2,2,3,3,3,3,4,4,2,2,2};
//        var result = HashTableExercises.mostFrequent ( mostFrequent );
//        System.out.println (result );

//        int []  countWithDifference = {1,7,5,9,2,12,3};
////        var result = HashTableExercises.countPairsWithDifference ( countWithDifference, 2 );
////        System.out.println (result );

        int [] twoSum = {2,7,11,15,-6};
        var result = HashTableExercises.twoSum ( twoSum, 9 );
        System.out.println (Arrays.toString ( result ) );


//        int [] twoSum2 = {2,7,11,15};
//        var result = HashTableExercises.twoSum2 ( twoSum2, 9 );
//        System.out.println (Arrays.toString ( result ) );
    }
}
