package com.dataStructuresStacks;

import java.util.Arrays;

public class Stack {
    private int[] items = new int[5];
    private int count;
    private int minValue;

    public void push(int item){
        if (this.count == this.items.length) throw new StackOverflowError();

        this.items[this.count++] = item;
    }

    public int pop(){
        if (this.count == 0) throw new IllegalStateException();

        return this.items[--count];
    }

    public int peek(){
        if (this.count == 0) throw new IllegalStateException();

        return this.items[count - 1];
    }

    public boolean isEmpty(){
        return this.count == 0;
    }

    @Override
    public String toString() {
        var content = Arrays.copyOfRange(this.items, 0, this.count);
        return Arrays.toString(content);
    }
}
