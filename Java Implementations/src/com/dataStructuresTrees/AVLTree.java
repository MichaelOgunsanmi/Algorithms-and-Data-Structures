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

        setHeight ( currentNode );

        return balance(currentNode);
    }

    private AVLNode balance ( AVLNode currentNode ) {
        if (isLeftHeavy ( currentNode )){
            if (balanceFactor ( currentNode.leftChild ) < 0)
                currentNode.leftChild = rotateLeft ( currentNode.leftChild );
            return rotateRight ( currentNode );
            }
        else if (isRightHeavy ( currentNode )){
            if (balanceFactor ( currentNode.rightChild ) > 0)
                currentNode.rightChild = rotateRight ( currentNode.rightChild );
            return rotateLeft ( currentNode );
        }

        return currentNode;
    }

    private AVLNode rotateLeft(AVLNode currentNode){
        var newRoot = currentNode.rightChild;

        currentNode.rightChild = newRoot.leftChild;
        newRoot.leftChild = currentNode;

        setHeight(currentNode);
        setHeight(newRoot);

        return newRoot;
    }

    private AVLNode rotateRight(AVLNode currentNode){
        var newRoot = currentNode.leftChild;

        currentNode.leftChild = newRoot.rightChild;
        newRoot.rightChild = currentNode;

        setHeight ( currentNode );
        setHeight ( newRoot );

        return newRoot;
    }

    private void setHeight ( AVLNode currentNode ) {
        currentNode.height = Math.max ( height ( currentNode.leftChild ), height ( currentNode.rightChild ) ) + 1;
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
