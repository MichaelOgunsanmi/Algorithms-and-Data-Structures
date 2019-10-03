package com.dataStructuresQueue;

import java.util.ArrayList;

public class LinkedListQueue {
    private class Node{
        private int value;
        private Node next;

        public Node(int value){
            this.value = value;
        }
    }

    private Node head;
    private Node tail;
    private int count;

    public void enqueue(int item){
        var node = new Node(item);

        if (isEmpty())
            this.head = this.tail = node;
        else {
            this.tail.next = node;
            this.tail = node;
        }

        this.count++;
    }

    public int dequeue(){
        if (isEmpty())
            throw new IllegalStateException();

        int value = this.head.value;

        if (this.head == this.tail)
            this.head = this.tail = null;
        else{
            var second = this.head.next;
            this.head.next = null;
            this.head = second;
        }

        count--;

        return value;
    }

    public int peek(){
        if (isEmpty())
            throw new IllegalStateException();

        return head.value;
    }

    public int size(){
        return this.count;
    }

    public boolean isEmpty(){
        return this.head == null;
    }

    @Override
    public String toString() {
        ArrayList<Integer> LinkedList = new ArrayList<>();

        var currentNode = this.head;
        while(currentNode != null){
            LinkedList.add(currentNode.value);
            currentNode = currentNode.next;
        }

        return LinkedList.toString();
    }
}
