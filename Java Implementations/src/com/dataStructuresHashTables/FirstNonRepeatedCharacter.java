package com.dataStructuresHashTables;

//import org.jetbrains.annotations.NotNull;

import jdk.jshell.EvalException;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;

public class FirstNonRepeatedCharacter {
    public static void main( String[] args) {
        Map<Character, Integer> map = new HashMap<>();
         char[] values = args[0].toCharArray();
        for (char ch: values) {
            if (map.containsKey(ch))
                map.replace(ch, map.get(ch) + 1);
            else
                map.put(ch, 1);
        }
        var minIndex = values.length;
        var answer = Character.MIN_VALUE;
        for (int i = 0; i < values.length; i++)
            if(map.get(values[i]) == 1 && i < minIndex){
                minIndex = i;
                answer = values[minIndex];}

        System.out.println(answer);
    }
}
