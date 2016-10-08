import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scanner = new Scanner(System.in);
        String str = scanner.nextLine();
        int i = 1;
        while (str != null)
        {
            System.out.print(Integer.toString(i++) + ' ' + str + '\n');
            str = scanner.nextLine();
        }
    }
}
