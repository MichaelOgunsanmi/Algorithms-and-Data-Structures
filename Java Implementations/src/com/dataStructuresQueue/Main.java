package com.dataStructuresQueue;

import java.util.*;

public class Main {
    public static void main(String[] args) {
//        Using Inbuilt ArrayDeque;
//        Queue<Integer> queue = new ArrayDeque<>();
//        queue.add(10);
//        queue.add(20);
//        queue.add(30);
//
//        var front = queue.remove();
//        System.out.println(front);
//
//        System.out.println(queue);

////        Reversing a queue using a stack
//        Queue<Integer> queue = new ArrayDeque<>();
//        queue.add(10);
//        queue.add(20);
//        queue.add(30);
//        System.out.println(queue);
//        reverse(queue);
//        System.out.println(queue);

////        Using custom built ArrayQueue class;
//        ArrayQueue queue = new ArrayQueue(5);
//        System.out.println(queue.isEmpty());
//        queue.enqueue(10);
//        queue.enqueue(20);
//        queue.enqueue(30);
//        queue.enqueue(40);
//        queue.enqueue(50);
//        System.out.println(queue.isFull());
//        var front = queue.dequeue();
//        front = queue.dequeue();
//        queue.enqueue(60);
//        front = queue.dequeue();
//        System.out.println(front);
//        System.out.println(queue);

////        QueueWithTwoStacks implementation;
//        QueueWithTwoStacks queue = new QueueWithTwoStacks();
//        System.out.println(queue.isEmpty());
//        queue.enqueue(10);
//        queue.enqueue(20);
//        queue.enqueue(30);
//        queue.enqueue(40);
//        queue.dequeue();
//        var first = queue.dequeue();
//        System.out.println(first);
//        System.out.println(queue.peek());
//        System.out.println(queue.isEmpty());

////        PriorityQueue class in Java;
//        PriorityQueue<Integer> queue = new PriorityQueue<>();
//        queue.add(5);
//        queue.add(1);
//        queue.add(3);
//        queue.add(2);
//        queue.add(4);
//        queue.add(1);
//        while (!queue.isEmpty())
//            System.out.println(queue.remove());

////        Using custom built PriorityQueue class;
//        PriorityQueue queue = new PriorityQueue();
//        System.out.println(queue.isEmpty());
//        queue.add(5);
//        queue.add(1);
//        System.out.println(queue.isEmpty());
//        queue.add(3);
//        System.out.println(queue.isFull());
//        queue.add(2);
//        queue.add(4);
//        System.out.println(queue.isFull());
//        System.out.println(queue);
//        while (!queue.isEmpty())
//            System.out.println(queue.remove());

////        QueueReverser class;
//        Queue<Integer> queue = new ArrayDeque<>();
//        queue.add(10);
//        queue.add(20);
//        queue.add(30);
//        queue.add(40);
//        queue.add(50);
//
//        QueueReverser.reverse(queue, 3);
//        System.out.println(queue);

////        LinkedListQueue custom class implementation
//        LinkedListQueue LinkedList = new LinkedListQueue();
//        System.out.println(LinkedList.isEmpty());
//        System.out.println(LinkedList.size());
//        LinkedList.enqueue(10);
//        LinkedList.enqueue(20);
//        LinkedList.enqueue(30);
//        LinkedList.enqueue(40);
//        LinkedList.enqueue(50);
//        System.out.println(LinkedList.size());
//        System.out.println(LinkedList.peek());
//        System.out.println(LinkedList);
//        var first = LinkedList.dequeue();
//        System.out.println(first);
//        System.out.println(LinkedList.size());
//        System.out.println(LinkedList.peek());
//        System.out.println(LinkedList);

////        StackWithTwoQueues implementation;
//        StackWithTwoQueues stack = new StackWithTwoQueues();
//        System.out.println(stack.isEmpty());
//        stack.push(10);
//        stack.push(20);
//        stack.push(30);
//        stack.push(40);
//        stack.push(50);
//
//        System.out.println(stack.isEmpty());
//        System.out.println(stack);
//
//        var front = stack.pop();
//        System.out.println(front);
//        System.out.println(stack);
//
//        System.out.println(stack.peek());
    }


    public static void reverse(Queue<Integer> queue) {
        Stack<Integer> stack = new Stack<>();

        while (!queue.isEmpty())
            stack.add(queue.remove());
        while (!stack.isEmpty())
            queue.add(stack.pop());
    }
}
