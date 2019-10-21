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

    public ArrayList<Integer> getNodesAtDistance( int distance ){
        ArrayList<Integer> levelElements = new ArrayList<> ();
        getNodesAtDistance (rootNode, distance, levelElements);
        return levelElements;
    }

    private void getNodesAtDistance ( Node currentNode, int distance, ArrayList<Integer> levelElements ) {
        if (currentNode == null)
            return;

        if (distance == 0) {
            levelElements.add ( currentNode.value );
            return;
        }

        getNodesAtDistance ( currentNode.leftChild, distance - 1, levelElements );
        getNodesAtDistance ( currentNode.rightChild, distance - 1, levelElements );
    }

    public ArrayList<Integer> breadthFirstSearch(){
        ArrayList<Integer> treeElements = new ArrayList<> ();

        for (int i = 0; i <= height () ; i++) {
            treeElements.addAll ( getNodesAtDistance ( i ) );
        }

        return treeElements;
    }

    public int size(){
        return size(rootNode);
    }

    private int size ( Node currentNode ) {
        if (currentNode == null)
            return 0;

        if (isLeaf ( currentNode ))
            return 1;

        return 1 + size (currentNode.leftChild) + size (currentNode.rightChild);
    }

    public int countLeaves(){
        return countLeaves (rootNode);
    }

    private int countLeaves ( Node currentNode ) {
        if (currentNode == null)
            return 0;

        if (isLeaf ( currentNode ))
            return 1;

        return countLeaves (currentNode.leftChild) + countLeaves (currentNode.rightChild);
    }

    public int maxBST(){
        if (rootNode == null)
            throw new IllegalStateException();

        var currentNode = rootNode;

        while (currentNode.rightChild != null)
            currentNode = currentNode.rightChild;

        return currentNode.value;

    }

    public int max(){
        return max(rootNode);
    }

    private int max ( Node currentNode ) {
        if (rootNode == null)
            throw new IllegalStateException ();

        if (currentNode.rightChild == null)
            return currentNode.value;

        return max (currentNode.rightChild);
    }

    public boolean contains(int value){
        return contains ( rootNode, value );
    }

    private boolean contains ( Node currentNode, int value ) {
        if (currentNode == null)
            return false;

        if (currentNode.value == value)
            return true;

        return contains ( currentNode.leftChild, value ) || contains ( currentNode.rightChild, value );
    }

    public boolean areSiblings(int firstSibling, int secondSibling){
        return areSiblings (rootNode, firstSibling, secondSibling);
    }

    private boolean areSiblings ( Node currentNode, int firstSibling, int secondSibling ) {
        if (currentNode == null)
            return false;

        var areSiblings = false;

        if (currentNode.leftChild != null && currentNode.rightChild != null)
            areSiblings =  ((currentNode.leftChild.value == firstSibling) && (currentNode.rightChild.value == secondSibling))||
                    ((currentNode.rightChild.value == firstSibling) && (currentNode.leftChild.value == secondSibling));

        return areSiblings || areSiblings ( currentNode.leftChild, firstSibling, secondSibling ) ||
                areSiblings ( currentNode.rightChild, firstSibling, secondSibling );
    }

    public ArrayList<Integer> getAncestors(int value){
        ArrayList<Integer> ancestors = new ArrayList<> ();
        getAncestors ( rootNode, value, ancestors );
        return ancestors;
    }

    private boolean getAncestors ( Node currentNode, int value, ArrayList<Integer> ancestors ) {
        if (currentNode == null)
            return false;

        if (currentNode.value == value)
            return true;

        if (getAncestors ( currentNode.leftChild, value, ancestors )
                || getAncestors ( currentNode.rightChild, value, ancestors)){
            ancestors.add ( currentNode.value );
            return true;
        }

        return false;
    }

    public boolean isBalanced(){
        return isBalanced (rootNode);
    }

    private boolean isBalanced ( Node currentNode ) {
        if (currentNode == null)
            return true;

        var balanceFactor = height (currentNode.leftChild) - height (currentNode.rightChild);

        return Math.abs ( balanceFactor ) <= 1
                && isBalanced (currentNode.leftChild)
                && isBalanced (currentNode.rightChild);
    }

    public boolean isPerfect() {
        return size () == (Math.pow ( 2, height () + 1 ) - 1);
    }


}
