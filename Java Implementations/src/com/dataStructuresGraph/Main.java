package com.dataStructuresGraph;

public class Main {
    public static void main ( String[] args ) {
//        Graph graph = new Graph ();
//        graph.addNode ( "A" );
//        graph.addNode ( "B" );
//        graph.addNode ( "C" );
//        graph.addEdge ( "A", "B" );
//        graph.addEdge ( "A", "C" );
//        graph.addEdge ( "B", "C" );
////        graph.removeEdge ( "A", "B" );
////        graph.removeNode ( "C" );
//        graph.print ();

////        For traversals;
//         /*A ---> B ---> D;
//         |             |;
//           ---> C <---
//
//          */
//
//         Graph graph = new Graph ();
//         graph.addNode ( "A" );
//         graph.addNode ( "B" );
//         graph.addNode ( "C" );
//         graph.addNode ( "D" );
//         graph.addEdge ( "A", "B" );
//         graph.addEdge ( "B", "D" );
//         graph.addEdge ( "D", "C" );
//         graph.addEdge ( "A", "C" );
////         graph.traverseDepthFirst ( "G" );
////        graph.traverseDepthFirstIter ( "A" );
//        graph.traverseBreadthFirst ( "A" );

////        Topological Sort;
//        Graph graph = new Graph ();
//        graph.addNode ( "X" );
//        graph.addNode ( "A" );
//        graph.addNode ( "B" );
//        graph.addNode ( "P" );
//        graph.addEdge ( "X", "A" );
//        graph.addEdge ( "X", "B" );
//        graph.addEdge ( "A", "P" );
//        graph.addEdge ( "A", "P" );
//        System.out.println (graph.topologicalSort () );

//        //Cycle detection in a graph;
//        Graph graph = new Graph ();
//        graph.addNode ( "A" );
//        graph.addNode ( "B" );
//        graph.addNode ( "C" );
//        graph.addEdge ( "B", "C" );
//        graph.addEdge ( "A", "B" );
//        graph.addEdge ( "A", "C" );
//        System.out.println (graph.hasCycle () ); //false
//        graph.addEdge ( "C", "A" );
//        System.out.println (graph.hasCycle () ); //true

////        Weighted Graphs;
//
//        WeightedGraph weightedGraph = new WeightedGraph ();
//        weightedGraph.addNode ( "A" );
//        weightedGraph.addNode ( "B" );
//        weightedGraph.addNode ( "C" );
//        weightedGraph.addEdge ( "A", "B", 3 );
//        weightedGraph.addEdge ( "A", "C", 2 );
//        weightedGraph.print ();

//        Djikstra Shortest Path;
//
        WeightedGraph weightedGraph = new WeightedGraph ();
        weightedGraph.addNode ( "A" );
        weightedGraph.addNode ( "B" );
        weightedGraph.addNode ( "C" );
        weightedGraph.addEdge ( "A", "B", 1 );
        weightedGraph.addEdge ( "B", "C", 2 );
        weightedGraph.addEdge ( "A", "C", 10 );
        System.out.println ( weightedGraph.getShortestPath ( "A", "C" ) );

//        //Cycle in undirected graphs;
//        WeightedGraph weightedGraph = new WeightedGraph ();
//        weightedGraph.addNode ( "A" );
//        weightedGraph.addNode ( "B" );
//        weightedGraph.addNode ( "C" );
//        weightedGraph.addEdge ( "A", "B", 0 );
//        weightedGraph.addEdge ( "B", "C", 0 );
//        weightedGraph.addEdge ( "C", "A", 0 );
//        System.out.println (weightedGraph.hasCycle () );


//        MinimumSpanningTree;
//        WeightedGraph weightedGraph = new WeightedGraph ();
//        weightedGraph.addNode ( "A" );
//        weightedGraph.addNode ( "B" );
//        weightedGraph.addNode ( "C" );
//        weightedGraph.addNode ( "D" );
//        weightedGraph.addEdge ( "A", "B", 3 );
//        weightedGraph.addEdge ( "B", "D", 4 );
//        weightedGraph.addEdge ( "C", "D", 5 );
//        weightedGraph.addEdge ( "A", "C", 1 );
//        weightedGraph.addEdge ( "B", "C", 2 );
//        var tree = weightedGraph.getMinimumSpanningTree ();
//        tree.print ();
    }
}
