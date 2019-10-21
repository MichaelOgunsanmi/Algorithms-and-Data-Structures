package com.dataStructuresHeap;

public class Heap {
    private int[] heap = new int[10];
    private int size;

    public void insert(int value){
        if (isFull ())
            throw new IllegalStateException ();

        heap[size++] = value;

        bubbleUp();
    }

    public int remove(){
        if (isEmpty())
            throw new IllegalStateException ();

        var rootElement = heap[0];
        heap[0] = heap[--size];

        bubbleDown ();

        return rootElement;
    }

    public int max(){
        if (isEmpty ())
            throw new IllegalStateException ();

        return heap[0];
    }

    public static boolean isMaxHeap(int[] array){
        return isMaxHeap ( array, 0 );
    }

    private static boolean isMaxHeap ( int[] array, int parentIndex ) {
        var lastPossibleParentIndex = (array.length - 2) / 2;

        if (parentIndex > lastPossibleParentIndex)
            return true;

        var leftChildIndex = parentIndex * 2 + 1;
        var leftValid = true;
        if(leftChildIndex >= array.length)
            return true;
        else
            leftValid = array[parentIndex] >= array[leftChildIndex];

        var rightChildIndex = parentIndex * 2 + 2;
        var rightValid = true;
        if (rightChildIndex >= array.length)
            return leftValid;
        else
            rightValid = array[parentIndex] >= array[rightChildIndex];


        var isValidParent = leftValid && rightValid;

        return isValidParent && isMaxHeap ( array, leftChildIndex ) && isMaxHeap ( array, rightChildIndex );


    }

    private void bubbleDown(){
        var parentIndex = 0;

        while (parentIndex <= size && !isValidParent(parentIndex)){
            var largerChildIndex = largerChildIndex(parentIndex);
            swapElements ( parentIndex, largerChildIndex );
            parentIndex = largerChildIndex;

        }
    }

    private int largerChildIndex ( int parentIndex ) {
        if (!hasLeftChild ( parentIndex ))
            return parentIndex;

        if (!hasRightChild ( parentIndex ))
            return leftChildIndex ( parentIndex );

        return leftChild ( parentIndex ) > rightChild ( parentIndex ) ?
                leftChildIndex ( parentIndex ) : rightChildIndex ( parentIndex );
    }

    private boolean isValidParent ( int parentIndex ) {
        if (!hasLeftChild ( parentIndex ))
            return true;

        var isValid = heap[parentIndex] >= leftChild(parentIndex);

        if (hasRightChild ( parentIndex ))
            isValid &= heap[parentIndex] >= rightChild(parentIndex);

        return isValid;
    }

    private boolean hasLeftChild(int parentIndex){
        return leftChildIndex ( parentIndex ) <= size;
    }

    private boolean hasRightChild(int parentIndex){
        return rightChildIndex ( parentIndex ) <= size;
    }

    private int rightChild ( int parentIndex ) {
        return heap[rightChildIndex ( parentIndex )];
    }

    private int rightChildIndex ( int parentIndex ) {
        return parentIndex * 2 + 2;
    }

    private int leftChild ( int parentIndex ) {
        return heap[leftChildIndex( parentIndex )];
    }

    private int leftChildIndex ( int parentIndex ) {
        return parentIndex * 2 + 1;
    }

    public boolean isEmpty ( ) {
        return size == 0;
    }

    public boolean isFull(){
        return size == heap.length;
    }

    private void bubbleUp ( ) {
        var childIndex = size - 1;

        while (childIndex > 0 && heap[childIndex] > heap[parent(childIndex)]){
            swapElements(childIndex, parent(childIndex));
            childIndex = parent(childIndex);
        }
    }

    private void swapElements ( int childIndex, int parentIndex ) {
        var temp = heap[childIndex];
        heap[childIndex] = heap[parentIndex];
        heap[parentIndex] = temp;
    }

    private int parent ( int childIndex ) {
        return (childIndex - 1) /2 ;
    }
}
