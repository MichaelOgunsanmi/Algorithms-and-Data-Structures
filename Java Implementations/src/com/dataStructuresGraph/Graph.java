package com.dataStructuresGraph;

import java.security.PublicKey;
import java.util.*;

public class Graph {
    private class Node{
        private String label;

        public Node ( String label ) {
            this.label = label;
        }

        @Override
        public String toString ( ) {
            return label;
        }
    }

    private Map<String, Node> graph= new HashMap<>();
    private Map<Node, List<Node>> adjacencyList = new HashMap<> ();

    public void addNode(String label){
        var newNode = new Node ( label );
        graph.putIfAbsent ( label, newNode );
        adjacencyList.putIfAbsent ( newNode, new ArrayList<> () );
    }

    public void addEdge(String firstLabel, String secondLabel){
        var firstNode = graph.get ( firstLabel );
        if (firstNode == null)
            throw new IllegalArgumentException ();

        var secondNode = graph.get ( secondLabel );
        if (secondNode == null)
            throw new IllegalArgumentException ();

        adjacencyList.get ( firstNode ).add ( secondNode );
    }

    public void print(){
        for (Node node : adjacencyList.keySet ( )) {
            var connectedNodesArray = adjacencyList.get ( node );
            if (!connectedNodesArray.isEmpty ())
                System.out.println ( node + " is connected to " + connectedNodesArray);
        }
    }

    public void removeNode(String label){
        var nodeToBeRemoved = graph.get ( label );
        if (nodeToBeRemoved == null)
            return;

        for (Node node : adjacencyList.keySet ( ))
            adjacencyList.get ( node ).remove ( nodeToBeRemoved ); //breaking connections between other nodes and nodeToBeRemoved;

        adjacencyList.remove ( nodeToBeRemoved );
        graph.remove ( nodeToBeRemoved );
    }

    public void removeEdge(String firstLabel, String secondLabel){
        var firstNode = graph.get ( firstLabel );
        var secondNode = graph.get ( secondLabel );

        if (firstNode == null || secondNode == null)
            return;

        adjacencyList.get ( firstNode ).remove ( secondNode );
    }

    public void traverseDepthFirst(String startingLabel){
        var startingNode = graph.get ( startingLabel );
        if (startingNode == null)
            return;

        traverseDepthFirst ( startingNode, new HashSet<> () );
    }

    private void traverseDepthFirst ( Node currentNode, Set<Node> visited ) {
        System.out.println ( currentNode );
        visited.add(currentNode);

        for (Node neighbour : adjacencyList.get ( currentNode ))
            if (!visited.contains ( neighbour ))
                traverseDepthFirst ( neighbour, visited );
    }

    public void traverseDepthFirstIter(String startingLabel){
        var startingNode = graph.get ( startingLabel );
        if (startingNode == null)
            return;

        Set<Node> visited = new HashSet<> ();
        Stack<Node> stack = new Stack<> ();
        stack.push ( startingNode );

        while (!stack.isEmpty ()){
            var currentNode = stack.pop ();
            if (visited.contains ( currentNode ))
                continue;

            System.out.println (currentNode );
            visited.add(currentNode);

            for (Node neighbour : adjacencyList.get ( currentNode ))
                if (!visited.contains ( neighbour ))
                    stack.push ( neighbour );
        }
    }

    public void traverseBreadthFirst(String startingLabel){
        var startingNode = graph.get ( startingLabel );
        if (startingNode == null)
            return;

        Set<Node> visited = new HashSet<> ();
        Queue<Node> queue = new ArrayDeque<> ();
        queue.add ( startingNode );

        while (!queue.isEmpty ()){
            var currentNode = queue.remove ();
            if (visited.contains ( currentNode ))
                continue;

            System.out.println (currentNode );
            visited.add(currentNode);

            for (Node neighbour : adjacencyList.get ( currentNode ))
                if (!visited.contains ( neighbour ))
                    queue.add ( neighbour );
        }
    }

    public List<String> topologicalSort(){
        Stack<Node> stack = new Stack<> ();
        Set<Node> visited = new HashSet<> ();

        for (Node neighbour : graph.values ( ))
            topologicalSort (neighbour, visited, stack);

        List<String> sorted = new ArrayList<> ();
        while (!stack.isEmpty ())
            sorted.add ( stack.pop ().label );

        return sorted;
        }

    private void topologicalSort ( Node currentNode, Set<Node> visited, Stack<Node> stack ) {
        if (visited.contains ( currentNode ))
            return;

        visited.add ( currentNode );

        for (Node neighbour : adjacencyList.get ( currentNode ))
            topologicalSort ( neighbour, visited, stack );

        stack.push ( currentNode );
    }

    public boolean hasCycle(){
        Set<Node> all = new HashSet<> ();
        all.addAll ( graph.values ());

        Set<Node> visiting = new HashSet<> ();
        Set<Node> visited = new HashSet<> ();

        while (!all.isEmpty ()){
            var currentNode = all.iterator ().next ();
            if (hasCycle (currentNode, all, visiting, visited))
                return true;
        }
        return false;
    }

    private boolean hasCycle ( Node currentNode, Set<Node> all, Set<Node> visiting, Set<Node> visited ) {
        all.remove ( currentNode );
        visiting.add ( currentNode );

        for (Node neighbour : adjacencyList.get ( currentNode )) {
            if (visited.contains ( neighbour ))
                continue;

            if (visiting.contains ( neighbour ))
                return true;

            if (hasCycle ( neighbour, all, visiting, visited ))
                return true;
        }

        visiting.remove ( currentNode );
        visited.add ( currentNode );

        return false;
    }
}
