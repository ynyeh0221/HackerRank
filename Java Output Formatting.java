import java.util.Scanner;

public class Solution {

    public static void main(String[] args) {
            Scanner sc=new Scanner(System.in);
            System.out.println("================================");
            for(int i=0;i<3;i++){
                String s1=sc.next();
                int xx=sc.nextInt();
                String x = Integer.toString(xx);
                //Complete this line
                for (int j = s1.length(); j < 15; j++)
                    s1 += ' ';
                for (int j = x.length(); j < 3; j++)
                    x = '0' + x;
                System.out.print(s1+x+'\n');
            }
            System.out.println("================================");

    }
}
