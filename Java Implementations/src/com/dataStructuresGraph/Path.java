package com.dataStructuresGraph;

import java.util.ArrayList;
import java.util.List;

public class Path {
    private List<String> nodesInPath = new ArrayList<> ();

    public void add(String node){
        nodesInPath.add(node);
    }

    @Override
    public String toString ( ) {
        return nodesInPath.toString ();
    }
}
