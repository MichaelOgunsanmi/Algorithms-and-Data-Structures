package com.dataStructuresHashTables;

import java.util.*;

public class HashTableExercises {

    public static int mostFrequent(int[] numbers){
        Map<Integer, Integer> hashTable = new HashMap<> ();

        for (int number : numbers) {
            var count = hashTable.getOrDefault ( number, 0 );
            hashTable.put ( number, count + 1 );
        }

        int mostFrequent = numbers[0];
        int maxCount = -1;

        for (Map.Entry<Integer, Integer> item : hashTable.entrySet ( )) {
            if(item.getValue () > maxCount){
                mostFrequent = item.getKey ();
                maxCount = item.getValue ();
            }
        }
        return mostFrequent;
    }

    public static int countPairsWithDifference(int[] numbers, int difference){
        Set<Integer> set = new HashSet<> ();

        for (int number : numbers) {
            set.add ( number );
        }

        int count = 0;

        for (int number : numbers) {
            if(set.contains ( number - difference ))
                count++;

            if (set.contains ( number + difference ))
                count ++;

            set.remove ( number );
        }

        return count;
    }

    public static Object[] twoSum( int[] numbers, int target){
        Map<Integer, int[]> hashTable = new HashMap<> ();
        ArrayList<String> output = new ArrayList<> ();

        for (int i = 0; i < numbers.length; i++) {
            hashTable.put ( numbers[i], new int[]{target - numbers[i], i} );
        }


        for (Map.Entry<Integer, int[]> item : hashTable.entrySet ( )) {
            int key = item.getValue ( )[0];
            if (hashTable.containsKey ( key )){
                output.add ( Arrays.toString ( (new int[]{item.getValue ( )[1], hashTable.get ( key )[1]}) ) );
                hashTable.put ( key, new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE} );
                hashTable.remove ( item.getKey (), new int[]{Integer.MAX_VALUE, Integer.MAX_VALUE} );
            }
        }

        return output.toArray ();
    }

    public static int[] twoSum2(int[] numbers, int target){
        Map<Integer, Integer> hashMap = new HashMap<> ();

        for (int i = 0; i < numbers.length; i++) {
            int complement = target - numbers[i];
            if (hashMap.containsKey ( complement ))
                return new int[]{hashMap.get ( complement), i};
            hashMap.put ( numbers[i], i );
        }
        return null;
    }

}
