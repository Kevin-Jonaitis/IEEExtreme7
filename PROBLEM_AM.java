import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Comparator;
import java.util.LinkedList;
import java.util.PriorityQueue;


public class Solution {
	
	
	int[][] mountain;
	int total_rows;
	int total_columns;
	
	//Compare cost to node and left versus right
	PriorityQueue<Node> frontier = new PriorityQueue<Node>(10, new Comparator<Node>() {
        public int compare(Node n1, Node n2) {
        	int difference = n1.costToNode - n2.costToNode;
        	if (difference == 0){
        		return n1.column - n2.column;
        	} else {
        		return difference;
        	}
        }
    });
	
	class Node {
		
		

		
		int value;
		int row;
		int column;
		int costToNode;
		LinkedList<Node> nodesToHere;
		
		public Node(int value, int row, int column, Node connectingNode) { //for all normal nodes
			this.value =  value;
			this.row = row;
			this.column = column;
			this.costToNode = connectingNode.costToNode + value;
			nodesToHere = new LinkedList<Node>();
			
//			System.out.println("Cost:" + costToNode);
			for (Node n : connectingNode.nodesToHere) {
				nodesToHere.add(n);
			}
			nodesToHere.add(connectingNode);
//			nodesToHere.addAll(connectingNode.nodesToHere);
		}
		public Node(){ //for the first node
			value = 0;
			row = -1;
			column = -1;
			nodesToHere = null;
			costToNode = 0;
			nodesToHere = new LinkedList<Node>();
//			System.out.println("the following should not be null");
		}
	}
	

	public Solution() throws IOException {

		 BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	     String[] line = br.readLine().split(" ");
	     total_rows = Integer.parseInt(line[0]);
	     total_columns = Integer.parseInt(line[1]);
	     mountain = new int[total_rows][total_columns];
	     for (int i = 0; i < total_rows; i++) {
	    	 String[] row = br.readLine().split(" ");
	    	 for(int j = 0; j <total_columns; j++) {
	    		 mountain[i][j] = Integer.parseInt(row[j]);
	    	 }
	     }
	     
//	     for (int i = 0; i < total_rows; i++) {
//	    	 for(int j = 0; j <total_columns; j++) {
//	    		 System.out.println(mountain[i][j]);
//	    	 }
//	     }	
	    
		Node first = new Node();
		frontier.add(first);
		boolean reachedGoalNode = false;
		Node goalNode = null;
		while(!reachedGoalNode) {
//			System.out.println("loop");
			Node n = frontier.remove();
			if (n.row == total_rows) { //found goal node
				reachedGoalNode = true;
				goalNode = n;
				continue;
			}
			addNeighborsToQueue(n);
		}
//		System.out.println("We found a solution!");
//		System.out.println(goalNode.costToNode);
		System.out.print("Minimum risk path = ");
		for (int i = 1; i <goalNode.nodesToHere.size(); i++) {
			System.out.print("[" + goalNode.nodesToHere.get(i).row + "," + goalNode.nodesToHere.get(i).column + "]");
		}
		System.out.println("");
		System.out.println("Risks along the path = " + goalNode.costToNode);
		

	     
     
	}
	
	public void addNeighborsToQueue(Node n) {
		Node left;
		Node right;
		Node center;
//		System.out.println("Adding neighbor for " + n.row + " " + n.column);
		if (n.row == -1){ //if you're on the bottom node, add all the new nodes babyyyy
			for (int i = 0; i < total_columns; i++) {
				frontier.add(new Node(mountain[n.row+1][i], n.row+1,i,n));
			}
			return;
		}
		if (n.row == total_rows - 1){ //YOURE AT THE TOP, YOURE ALMOST THERE
//			System.out.println("I GOT TO THE TOP");
			frontier.add(new Node(0,n.row + 1, -1,n)); //gives it the left most column, winner winner node
			return;
		}
		if (!(n.column == 0)) {
			frontier.add(new Node(mountain[n.row+1][n.column - 1], n.row+1,n.column - 1,n));
		}
		if (!(n.column== total_columns - 1)) {
			frontier.add(new Node(mountain[n.row+1][n.column + 1], n.row+1,n.column + 1,n));
		}
		
		//add the middle one
		frontier.add(new Node(mountain[n.row+1][n.column], n.row+1,n.column,n));
		
	}

	public void getChildren(int row, int column) {
	}
	/**
	 * @param args
	 * @throws IOException 
	 */
	public static void main(String[] args) throws IOException {
		Solution run = new Solution();
	}

}
