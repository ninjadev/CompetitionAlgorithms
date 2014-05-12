package org.ninjadev.competitionalgorithms.tests.graph;

import org.junit.Test;
import org.ninjadev.competitionalgorithms.graph.AlphaBetaPruning;
import org.ninjadev.competitionalgorithms.graph.AlphaBetaPruning.Node;

import junit.framework.TestCase;


public class AlphaBetaPruningTest extends TestCase {

    /*
     *              08
     *             /  \
     *            /    \
     *           /      \
     *          /        \
     *         /          \
     *        71           41
     *      /   \         /  \
     *    31     10     11    16
     *   /  \   /  \   /
     *  45  51 31  21 13
     */

	@Test
	public void testSmallGraph(){

        Node n1 = new Node();
        n1.value = 8;
        Node n2 = new Node();
        n2.value = 71;
        n1.children.append(n2);
        Node n3 = new Node();
        n3.value = 41;
        n1.children.append(n3);
        Node n4 = new Node();
        n4.value = 31;
        n2.children.append(n4);
        Node n5 = new Node();
        n5.value = 10;
        n2.children.append(n5);
        Node n6 = new Node();
        n6.value = 11;
        n3.children.append(n6);
        Node n7 = new Node();
        n7.value = 16;
        n3.children.append(n7);
        Node n8 = new Node();
        n8.value = 45;
        n4.children.append(n8);
        Node n9 = new Node();
        n9.value = 51;
        n4.children.append(n9);
        Node n10 = new Node();
        n10.value = 31;
        n5.children.append(n10);
        Node n11 = new Node();
        n11.value = 21;
        n5.children.append(n11);
        Node n12 = new Node();
        n12.value = 13;
        n6.children.append(n12);
		
        int depth = 4;
        int result = AlphaBetaPruning.alphabeta(
            origin, depth, Integer.MIN_VALUE, Integer.MAX_VALUE, true);
		
        assertEquals(10, result);
	}
}
