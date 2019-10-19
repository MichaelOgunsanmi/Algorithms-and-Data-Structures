package com.dataStructuresTrees;

public class AVLTree {
    private class AVLNode{
        private int value;
        private int height;
        private AVLNode leftChild;
        private AVLNode rightChild;

        public AVLNode ( int value ) {
            this.value = value;
        }

        @Override
        public String toString ( ) {
            return "AVLNode{" +
                    "value=" + value +
                    '}';
        }
    }

    private AVLNode rootNode;

    public void insert( int value){
        rootNode =  insert ( rootNode, value );
    }

    private AVLNode insert ( AVLNode currentNode, int value ) {
        if (currentNode == null) {
            return new AVLNode ( value );
        }

        if (value < currentNode.value)
            currentNode.leftChild = insert ( currentNode.leftChild, value );
        else
            currentNode.rightChild = insert ( currentNode.rightChild, value );

        currentNode.height = Math.max ( height ( currentNode.leftChild ), height ( currentNode.rightChild ) ) + 1;

        balance(currentNode);

        return currentNode;
    }

    private void balance ( AVLNode currentNode ) {
        if (isLeftHeavy ( currentNode )){
            if (balanceFactor ( currentNode.leftChild ) < 0)
                System.out.println ( "Perform left rotation on " + currentNode.leftChild  );
            System.out.println ( "Perform right rotation as " + currentNode.value + " is left heavy" );
            }
        else if (isRightHeavy ( currentNode )){
            if (balanceFactor ( currentNode.rightChild ) > 0)
                System.out.println ("Perform right rotation on " + currentNode.rightChild );
            System.out.println ( "Perform left rotation as " + currentNode.value + " is right heavy" );
        }
    }

    private int height(AVLNode currentNode){
        return currentNode == null ? -1 : currentNode.height;
    }

    private int balanceFactor(AVLNode currentNode){
        return currentNode == null ? 0 : height ( currentNode.leftChild ) - height ( currentNode.rightChild );
    }

    private boolean isLeftHeavy(AVLNode currentNode){
        return balanceFactor ( currentNode ) > 1;
    }

    private boolean isRightHeavy(AVLNode currentNode){
        return balanceFactor ( currentNode ) < -1;
    }
}
