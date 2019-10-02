package com.dataStructuresStacks;

import java.util.Arrays;

public class TwoStacks {
    private int top1;
    private int top2;
    private int[] items;
    
    public TwoStacks(int capacity) {
        if (capacity <= 0) throw new IllegalArgumentException("capacity must be 1 or greater");
        
        this.items = new int[capacity];
        this.top1 = -1;
        this.top2 = capacity;
    }
    
    public void push1(int item){
        if (isFull1()) throw new IllegalStateException();
        
        items[++top1] = item;
    }
    
    public int pop1(){
        if (isEmpty1()) throw new IllegalStateException();
        
        return items[this.top1--];
    }
    
    public boolean isEmpty1() { return this.top1 == -1; }
    
    public boolean isFull1() { return this.top1 +1 == top2; }

    public void push2(int item){
        if (isFull2()) throw new IllegalStateException();

        items[--top2] = item;
    }

    public int pop2(){
        if (isEmpty2()) throw new IllegalStateException();

        return items[this.top2++];
    }

    public boolean isEmpty2() { return this.top2 == this.items.length; }

    public boolean isFull2() { return this.top2 - 1 == top1; }

    @Override
    public String toString() { return  Arrays.toString(items); }
}
