import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String month = in.next();
        String day = in.next();
        String year = in.next();
        SimpleDateFormat ft = new SimpleDateFormat ("yyyy-MM-dd"); 
        Date t;
        try {
           t = ft.parse(year + "-" + month + "-" + day); 
           ft.applyPattern("EEEE");
           String tt = ft.format(t);
           System.out.println(tt.toUpperCase()); 
        }catch (ParseException e) { 
           System.out.println("Unparseable using " + ft); 
        }
    }
}
