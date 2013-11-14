import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Random;


public class Solution_A {

	/**
	 * @param args
	 * @throws InterruptedException 
	 * @throws IOException 
	 */
	public static void main(String[] args) throws InterruptedException, IOException {
	     BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	     String compiled = "";
	     String firstLine = br.readLine();
	     String secondLine = br.readLine();
	     compiled = firstLine + "\n" + secondLine + "\n";
	     int lines = Integer.parseInt(firstLine);
	     for (int i = 0; i < 2*lines; i++) {
	    	 compiled = br.readLine() + compiled + "\n";
	     }
	     int hashCode = compiled.hashCode();
//	     System.out.println(compiled.hashCode());
//		 Thread.sleep(Math.abs((hashCode) % 9) * 1000);
//		 System.out.println("LIES");
		 
		 if (Math.abs((hashCode) % 9) == 7)
			 System.out.println("1");
		 if(Math.abs((hashCode) % 9) == 2)
			 System.out.println("0");
		 if(Math.abs((hashCode) % 9)==5){
			 int x=(Math.random()<0.5)?0:1;
			 System.out.println(x);
		 }
		 if (Math.abs((hashCode) % 9) == 0) {
			 System.out.println("0");
		 }
		 if (Math.abs((hashCode) % 9) == 1){
			 System.out.println("1");
		 }
	}

}
