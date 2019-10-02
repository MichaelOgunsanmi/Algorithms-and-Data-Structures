package com.dataStructuresLinkedList;

import com.sun.source.tree.IfTree;

import java.util.NoSuchElementException;

public class LinkedList {
    private class Node {
        private int value;
        private Node next;

        public Node(int value) {
            this.value = value;
        }
    }

    private Node first;
    private Node last;
    private int size;

    public void addLast(int item){
        var node = new Node(item);

        if (this.isEmpty())
            this.first = this.last = node;
        else{
            this.last.next = node;
            this.last = node;
        }
        size++;
    }

    public void addFirst(int item){
        var node = new Node(item);

        if (this.isEmpty())
            this.first = this.last = node;
        else{
            node.next = this.first;
            this.first = node;
        }
        size++;
    }

    public int indexOf(int item){
        int index = 0;
        var currentNode = this.first;

        while (currentNode != null){
            if (currentNode.value == item) return index;
            index++;
            currentNode = currentNode.next;
        }
        return -1;
    }

    public boolean contains(int item){
        return this.indexOf(item) != -1;
    }

    public void removeFirst(){
        if (this.isEmpty())
            throw new NoSuchElementException();

        if (this.first == this.last)
            this.first = this.last = null;
        else{
            var temp = this.first;
            this.first = temp.next;
            temp.next = null;
        }
        size--;
    }

    public void removeLast(){
        if (this.isEmpty())
            throw new NoSuchElementException();

        if (this.first == this.last) {
            this.first = this.last = null;
        }else {
            var currentNode = this.first;

            while (currentNode.next != this.last){
                currentNode = currentNode.next;
            }

            currentNode.next = null;
            this.last = currentNode;
        }
        size--;
    }

    public int size(){
        return this.size;
    }

    public int[] toArray(){
        int [] array = new int[this.size];

        var currentNode = this.first;
        var index = 0;

        while (currentNode != null){
            array[index++] = currentNode.value;
            currentNode =currentNode.next;
        }

        return array;
    }

    public void reverse(){
        if (isEmpty())
            return;

        var alreadyReversed = this.first;
        var currentNode = this.first.next;

        while (currentNode != null){
            var second = currentNode.next;
            currentNode.next = alreadyReversed;

            alreadyReversed = currentNode;
            currentNode = second;
        }

        this.last = this.first;
        this.last.next = null;
        this.first = alreadyReversed;
    }

    public int getKthFromTheEnd(int k){
        if (this.isEmpty())
            throw new IllegalStateException();

        var firstPointer = this.first;
        var secondPointer = this.first;

        for (int i = 0; i < k-1; i++) {
            secondPointer = secondPointer.next;
            if (secondPointer == null)
                throw new IllegalArgumentException();
        }

        while (secondPointer != this.last){
            firstPointer = firstPointer.next;
            secondPointer = secondPointer.next;
        }
        return firstPointer.value;
    }

    public void printMiddle(){
        if (this.isEmpty())
            throw new IllegalStateException();

        var leftPointer = this.first;
        var rightPointer = this.first;

        while (rightPointer != this.last && rightPointer.next != this.last){
            rightPointer = rightPointer.next.next;
            leftPointer = leftPointer.next;
        }

        if (rightPointer == this.last)
            System.out.println(leftPointer.value);
        else
            System.out.println(leftPointer.value + "," + leftPointer.next.value);
    }

    public boolean hasLoop(){
        var slowPointer = this.first;
        var fastPointer = this.first;

        while(fastPointer != null && fastPointer.next != null){
            fastPointer = fastPointer.next.next;
            slowPointer = slowPointer.next;

            if (fastPointer == slowPointer)
                return true;
        }
        return false;
    }

    private boolean isEmpty(){
        return this.first == null;
    }

    public static LinkedList createWithLoop() {
        var list = new LinkedList();
        list.addLast(10);
        list.addLast(20);
        list.addLast(30);

        // Get a reference to 30
        var node = list.last;

        list.addLast(40);
        list.addLast(50);

        // Create the loop
        list.last.next = node;

        return list;
    }
}
