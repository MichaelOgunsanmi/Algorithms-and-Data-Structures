package com.dataStructuresTrees;

import java.util.ArrayList;

public class Tree {
    private class Node{
        private int value;
        private Node leftChild;
        private Node rightChild;

        public Node ( int value ) {
            this.value = value;
        }

        @Override
        public String toString ( ) {
            return "Node{" +
                    "value=" + value +
                    '}';
        }
    }

    private Node rootNode;

    public void insert(int value){
        var newNode = new Node(value);

        if (rootNode == null){
            rootNode = newNode;
            return;
        }

        var currentNode = rootNode;
        while (currentNode != null){
            if (value < currentNode.value){
                if (currentNode.leftChild == null){
                    currentNode.leftChild = newNode;
                    return;
                }
                currentNode = currentNode.leftChild;
            }
            else{
                if (currentNode.rightChild == null){
                    currentNode.rightChild = newNode;
                    return;
                }
                currentNode = currentNode.rightChild;
            }
        }
    }

    public boolean find(int value){
        if (rootNode == null)
            return false;

        var currentNode = rootNode;

        while(currentNode != null){
            if (currentNode.value == value)
                return true;
            if (value < currentNode.value)
                currentNode = currentNode.leftChild;
            else
                currentNode = currentNode.rightChild;
        }

        return false;
    }

    public void preOrderDepthFirstSearch(){
        ArrayList<Integer> treeElements = new ArrayList<> ();
        System.out.println ( preOrderDepthFirstSearch (rootNode, treeElements ) );
    }

    private ArrayList preOrderDepthFirstSearch ( Node currentNode, ArrayList<Integer> treeElements ) {
        treeElements.add ( currentNode.value );

        if (currentNode.leftChild != null)
            preOrderDepthFirstSearch (currentNode.leftChild, treeElements);

        if (currentNode.rightChild != null)
            preOrderDepthFirstSearch (currentNode.rightChild, treeElements);

        return treeElements;
    }

    public void inOrderDepthFirstSearch(){
        ArrayList<Integer> treeElements = new ArrayList<> ();
        System.out.println ( inOrderDepthFirstSearch ( rootNode, treeElements ) );
    }

    private ArrayList inOrderDepthFirstSearch ( Node currentNode, ArrayList<Integer> treeElements ) {
        if (currentNode.leftChild != null)
            inOrderDepthFirstSearch (currentNode.leftChild, treeElements);

        treeElements.add ( currentNode.value );

        if (currentNode.rightChild != null)
            inOrderDepthFirstSearch (currentNode.rightChild, treeElements);

        return treeElements;
    }

    public void postOrderDepthFirstSearch(){
        ArrayList<Integer> treeElements = new ArrayList<> ();
        System.out.println ( postOrderDepthFirstSearch ( rootNode, treeElements ) );
    }

    private ArrayList postOrderDepthFirstSearch ( Node currentNode, ArrayList<Integer> treeElements ) {
        if (currentNode.leftChild != null)
            postOrderDepthFirstSearch (currentNode.leftChild, treeElements);

        if (currentNode.rightChild != null)
            postOrderDepthFirstSearch (currentNode.rightChild, treeElements);

        treeElements.add ( currentNode.value );

        return treeElements;
    }

    public int height(){
        return height (rootNode);
    }

    private int height ( Node currentNode ) {
        if (rootNode == null)
            return -1;

        if (isLeaf ( currentNode  ))
            return 0;

        return 1 + Math.max ( height ( currentNode.leftChild ), height ( currentNode.rightChild ) ); //left, right, root (postOrder traversal)
    }

    private boolean isLeaf(Node currentNode){
        return currentNode.leftChild == null && currentNode.rightChild == null;
    }
    
    public int min(){
        return min(rootNode);
    }

    private int min ( Node currentNode ) {
        if (rootNode == null)
            throw new IllegalStateException ();


        if (isLeaf ( currentNode ))
            return currentNode.value;

        var leftMin = currentNode.leftChild != null ? min(currentNode.leftChild) : Integer.MAX_VALUE;
        var rightMin = currentNode.rightChild != null ? min(currentNode.rightChild): Integer.MAX_VALUE;

        return Math.min ( Math.min ( leftMin, rightMin ), rootNode.value ); //left, right, root (postOrder traversal)
    }

    public int minBST(){
        if (rootNode == null)
            throw new IllegalStateException ();

        var currentNode = rootNode;
        while(currentNode.leftChild != null)
            currentNode = currentNode.leftChild;

        return currentNode.value;
    }

    public boolean equals(Tree secondTree){
        if(secondTree == null)
            return false;

        return equals ( rootNode, secondTree.rootNode );
    }

    private boolean equals ( Node currentNode, Node secondCurrentNode ) {
        if (currentNode == null && secondCurrentNode == null)
            return true;

        if (currentNode != null && secondCurrentNode != null)
            return currentNode.value == secondCurrentNode.value  //root, left, right (preOrder Traversal)
                    && equals ( currentNode.leftChild, secondCurrentNode.leftChild )
                    && equals ( currentNode.rightChild, secondCurrentNode.rightChild );

        return false;
    }

    public void swapRoot(){
        var temp = rootNode.leftChild;
        rootNode.leftChild = rootNode.rightChild;
        rootNode.rightChild = temp;
    }

    public boolean isBinarySearchTree(){
        return isBinarySearchTree (rootNode, Integer.MIN_VALUE, Integer.MAX_VALUE);
    }

    private boolean isBinarySearchTree ( Node currentNode, int minValue, int maxValue ) {
        if (currentNode == null)
            return true;

        if (currentNode.value < minValue || currentNode.value > maxValue)
            return false;

        return isBinarySearchTree ( currentNode.leftChild, minValue, currentNode.value - 1 ) &&
                isBinarySearchTree ( currentNode.rightChild, currentNode.value + 1, maxValue ); //root, left, right (preOrder Traversal)
    }

}
