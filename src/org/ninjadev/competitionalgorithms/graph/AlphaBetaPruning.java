package org.ninjadev.competitionalgorithms.graph;
import java.util.ArrayList;

public class AlphaBetaPruning {

	public static class Node {
		public int value;
		public ArrayList<Node> children;

        public Node() {
            children = new ArrayList<Node>();
        }
    }
    

    public static int alphabeta(Node node, int depth, int alpha,
                                int beta, boolean maximizingPlayer) {
        if(depth == 0 || node.children.size() == 0) {
            return node.value;
        }

        if(maximizingPlayer) {
            for(Node child : node.children) {
                alpha = Math.max(alpha, alphabeta(child, depth - 1,
                                                  alpha, beta, false));
                if(beta <= alpha) {
                    break;
                }
            }
            return alpha;
        } else {
            for(Node child : node.children) {
                beta = Math.min(beta, alphabeta(child, depth - 1,
                                                alpha, beta, true));
                if(beta <= alpha) {
                    break;
                }
            }
            return beta;
        }
    }
}
