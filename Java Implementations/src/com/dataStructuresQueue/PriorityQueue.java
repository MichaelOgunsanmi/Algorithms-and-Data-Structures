package com.dataStructuresQueue;

import java.util.Arrays;

public class PriorityQueue {
    private int [] items = new int[5];
    private int count;

    public void add(int item){
        if (isFull())
            throw new IllegalStateException();

        var i = shiftItemsToInsert(item);
        this.items[i] = item;
        count++;
    }

    public boolean isFull(){
        return this.count == this.items.length;
    }

    private int shiftItemsToInsert(int item){
        int i;
        for (i = this.count - 1; i >= 0; i--) {
            if (this.items[i] > item)
                this.items[i+1] = this.items[i];
            else
                break;
        }
        return i + 1;
    }

    public boolean isEmpty(){
        return this.count == 0;
    }

    public int remove(){
        if (isEmpty())
            throw new IllegalStateException();

        return this.items[--this.count];
    }

    @Override
    public String toString() {
        return Arrays.toString(items);
    }
}
