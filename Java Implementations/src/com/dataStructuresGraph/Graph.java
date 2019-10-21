package com.dataStructuresGraph;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

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
}
