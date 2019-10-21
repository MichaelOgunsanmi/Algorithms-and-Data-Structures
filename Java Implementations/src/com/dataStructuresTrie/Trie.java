package com.dataStructuresTrie;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;

public class Trie {
    public static int ALPHABET_SIZE = 26;

    private class Node{
        private char value;
        private HashMap<Character, Node> children = new HashMap<> ();
        private boolean isEndOfWord;

        public Node ( char value ) {
            this.value = value;
        }

        @Override
        public String toString ( ) {
            return "Node{" +
                    "value=" + value +
                    '}';
        }

        public boolean hasChild(char child){
            return children.containsKey ( child );
        }

        public void addChild(char child){
            children.put ( child, new Node ( child ) );
        }

        public Node getChild(char child){
            return children.get ( child );
        }

        public Node[] getChildren ( ) {
            return children.values ().toArray (new Node[0]);
        }

        public boolean hasChildren ( ) {
            return !children.isEmpty ();
        }

        public void removeChild ( char child ) {
            children.remove ( child );
        }
    }

    private Node rootNode = new Node ( ' ' );

    public void insert(String word){
        var currentNode = rootNode;

        for (char letter : word.toCharArray ( )) {
            if (!currentNode.hasChild ( letter ))
                currentNode.addChild ( letter );
            currentNode = currentNode.getChild ( letter );
        }
        currentNode.isEndOfWord = true;
    }

    public boolean contains(String word){
        if (word == null)
            return false;

        var currentNode = rootNode;

        for (char letter : word.toCharArray ( )) {
            if (!currentNode.hasChild ( letter ))
                return false;
            currentNode = currentNode.getChild ( letter );
        }
        return currentNode.isEndOfWord;
    }

    public void traverse(){
        traverse (rootNode);
    }

    private void traverse ( Node currentNode ) {
        System.out.println ( currentNode.value ); //PreOrder traversal;
        for(var child: currentNode.getChildren())
            traverse (child);
    }

    public void remove(String word){
        if (word == null)
            return;
        remove ( rootNode, word, 0 );
    }

    private void remove ( Node currentNode, String word, int index ) {
        if (index == word.length ()){
            currentNode.isEndOfWord = false;
            return;
        }

        var letter = word.charAt ( index );
        var child = currentNode.getChild ( letter );
        if (child == null)
            return;

        remove ( child, word, index + 1 );  //Post Order traversal

        if (!child.hasChildren() && !child.isEndOfWord)
             currentNode.removeChild(letter);
    }

    public List<String> findWords(String prefix){
        var lastNode = findLastNodeOf ( prefix );
        List<String> words = new ArrayList<> ();

        findWords ( lastNode, prefix, words );

        return words;
    }

    private void findWords ( Node currentNode, String prefix, List<String> words ) {
        if (currentNode == null)
            return;

        if (currentNode.isEndOfWord)
            words.add ( prefix );

        for (Node child : currentNode.getChildren ( ))
            findWords ( child, prefix + child.value, words );
    }

    private Node findLastNodeOf ( String prefix ){
        if (prefix == null)
            return null;

        var currentNode = rootNode;
        for (char letter : prefix.toCharArray ( )) {
           var child = currentNode.getChild ( letter );
           if (child == null)
               return null;
           currentNode = child;
        }

        return currentNode;
    }

    public boolean containsRecursive(String word){
        if (word == null)
            return false;

        return containsRecursive(rootNode, word, 0);
    }

    private boolean containsRecursive ( Node currentNode, String word, int index ) {
        if (index == word.length ())
            return currentNode.isEndOfWord;

        if (currentNode == null)
            return false;

        var letter = word.charAt ( index );
        var child = currentNode.getChild ( letter );

        if (child == null)
            return false;

        return containsRecursive ( child, word, index + 1 );
    }

    public int countWords(){
        return countWords (rootNode);
    }

    private int countWords ( Node currentNode ) {
        var total = 0;

        if (currentNode.isEndOfWord)
            total++;

        for (Node child : currentNode.getChildren ( ))
            total += countWords (child);

        return total;
    }

    public static String longestCommonPrefix(String[] words){
        if (words == null)
            return "";

        var trie = new Trie ();
        for (String word : words)
            trie.insert ( word );

        var prefix = new StringBuffer ();
        var maxCharacters = getShortest(words).length();
        var currentNode = trie.rootNode;

        while (prefix.length () < maxCharacters){
            var children = currentNode.getChildren ();
            if (children.length != 1)
                break;
            currentNode = children[0];
            prefix.append ( currentNode.value );
        }

        return prefix.toString ();
    }

    private static String getShortest ( String[] words ) {
        if (words == null || words.length == 0)
            return "";

        var shortest = words[0];
        for (String word : words)
            if (word.length () < shortest.length ())
                shortest = word;

         return shortest;
    }
}
