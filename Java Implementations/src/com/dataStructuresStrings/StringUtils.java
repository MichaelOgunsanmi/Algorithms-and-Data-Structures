package com.dataStructuresStrings;

import java.util.*;

public class StringUtils {
    public static int countVowels(String inputString){
        if (inputString == null)
            return 0;

        int numberOfVowels = 0;
        Set<Character> vowels = new HashSet<> ( Arrays.asList ( 'a', 'e', 'i', 'o', 'u' ) );

        for (char c : inputString.toLowerCase ( ).toCharArray ( ))
            if (vowels.contains ( c ))
                numberOfVowels++;

        return numberOfVowels;
    }

    public static String reverse(String inputString){
        if (inputString == null)
            return "";

        StringBuilder reversed = new StringBuilder ();

        for (int i = inputString.length () - 1; i >= 0 ; i--)
            reversed.append ( inputString.charAt ( i ) );

        return reversed.toString ();
    }

    public static String reverseWords(String inputString){
        if (inputString == null)
            return "";

        String[] words = inputString.trim ().split ( " " );
        Collections.reverse ( Arrays.asList ( words ) );

        return String.join ( " ", words );
    }

    public static boolean areRotations(String inputString, String testString){
        if (inputString == null || testString == null)
            return false;

        return (inputString.length () == testString.length () && (inputString+inputString).contains ( testString ));
    }

    public static String removeDuplicates(String inputString){
        if (inputString == null)
            return "";

        StringBuilder output = new StringBuilder ();
        Set<Character> seen = new HashSet<> ();

        for (char character : inputString.toCharArray ( ))
            if (!seen.contains ( character )){
                seen.add ( character );
                output.append ( character );
            }

        return output.toString ();
    }

    public static char getMaxOccuringChar(String inputString){
        if (inputString == null || inputString.isEmpty ())
            throw new IllegalArgumentException ();

        final int ASCII_SIZE = 256;
        int[] frequencies = new int[ASCII_SIZE];

        for (char character : inputString.toCharArray ( ))
            frequencies[character]++;

        int max = 0;
        char result = ' ';

        for (int i = 0; i < frequencies.length ; i++)
            if (frequencies[i] > max) {
                max = frequencies[i];
                result = (char) i;
            }
        return  result;
    }

    public static String capitalize(String inputString){
        if (inputString == null || inputString.trim ().isEmpty ())
            return "";

        String[] words = inputString
                            .trim ()
                            .replaceAll ( " +", " " )
                            .split ( " " );

        for (int i = 0; i < words.length; i++)
            words[i] = words[i].substring ( 0,1 ).toUpperCase () + words[i].substring ( 1 ).toLowerCase ();

        return String.join ( " ", words );
    }

    public static boolean areAnagrams(String inputString, String testString){
        if (inputString == null || testString == null || inputString.length () != testString.length ())
            return false;

        var inputArray = inputString.toLowerCase ().toCharArray ();
        Arrays.sort ( inputArray );

        var testArray = testString.toLowerCase ().toCharArray ();
        Arrays.sort ( testArray );

        return Arrays.equals ( inputArray, testArray );
    }

    public static boolean areAnagrams2(String inputString, String testString){
        if (inputString == null || testString == null || inputString.length () != testString.length ())
            return false;

        final int ENGLISH_ALPHABET = 26;
        int[] frequencies = new int[ENGLISH_ALPHABET];

        inputString = inputString.toLowerCase ();
        for (int i = 0; i < inputString.length (); i++)
            frequencies[inputString.charAt ( i ) - 'a']++;

        testString = testString.toLowerCase ();
        for (int i = 0; i < testString.length (); i++) {
            var index = testString.charAt ( i ) - 'a';

            if (frequencies[index] == 0)
                return false;

            frequencies[index]--;
        }

        return true;
    }

    public static boolean isPalindrome(String inputString){
        if (inputString == null)
            return false;

        int leftPointer = 0;
        int rightPointer = inputString.length () - 1;

        while (leftPointer < rightPointer)
            if (inputString.charAt ( leftPointer++ ) != inputString.charAt ( rightPointer++ ))
                return false;
        return true;
    }
}
