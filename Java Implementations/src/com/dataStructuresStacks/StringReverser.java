package com.dataStructuresStacks;

import java.util.Stack;

public class StringReverser {

    public String reverse (String input) {
        if (input == null)
            throw new IllegalArgumentException();

        var stack = new Stack<Character>();

        for (char ch : input.toCharArray()) stack.push(ch);

//        OR (More efficient as no new array has to be created. Only look up required)
//        for (int i = 0; i < input.length(); i++) stack.push(input.charAt(i));

        /*
//        Bad approach as string concatenation is expensive (since string is immutable,
//        a new string has to be created and contents of the old string moved into thestring object)

        var reversed = "";
        while (!stack.empty()) reversed += stack.pop();
        */

        var reversed = new StringBuffer();
        while (!stack.empty()) reversed.append(stack.pop());

//        StringBuilder reversed2 = new StringBuilder();
//        while (!stack.empty()) reversed2.append(stack.pop());




        return reversed.toString();
    }
}
