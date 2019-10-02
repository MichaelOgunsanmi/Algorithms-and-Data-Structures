package com.dataStructuresQueue;

import java.util.Arrays;

public class ArrayQueue {
    private int[] items;
    private int rear;
    private int front;
    private int count;

    public ArrayQueue(int capacity) {
        this.items = new int[capacity];
    }

    public void enqueue (int item){
        if (this.count == this.items.length)
            throw new IllegalStateException();

        this.items[rear] = item;
        rear = (rear + 1) % this.items.length; //Using circular arrays
        count++;
    }

    public int dequeue(){
        var item = this.items[front];
        this.items[front] = 0;
        front = (front + 1) % this.items.length; //Using circular arrays
        count--;
        return item;
    }

    public int peek() {
        return this.items[front];
    }

    public boolean isEmpty(){
        return this.count == 0;
    }

    public boolean isFull(){
        return  this.count == this.items.length;
    }

    @Override
    public String toString() {
        return Arrays.toString(items);
    }
}
