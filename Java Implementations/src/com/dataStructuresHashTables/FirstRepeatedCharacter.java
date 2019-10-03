package com.dataStructuresHashTables;

import java.util.HashSet;
import java.util.Set;

public class FirstRepeatedCharacter {
    public static void main(String[] args) {
        Set<Character> set = new HashSet<>();
        char[] characters = args[0].toCharArray();
        char output = Character.MIN_VALUE;
        for (char ch: characters) {
            if (set.contains(ch)) {
                output = ch;
                break;
            }
            set.add(ch);
        }
        System.out.println(output);
    }
}
