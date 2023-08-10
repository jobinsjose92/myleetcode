
import java.io.*;
import java.util.*;
import java.util.Arrays;
import java.text.*;
import java.math.*;
import java.util.regex.*;
class prefix {

  public String longestCommonPrefix(String[] strs) {
    if (strs.length == 0)
      return "";

    for (int i = 0; i < strs[0].length(); i++)
    
    for (int j = 1; j < strs.length; j++)
    
     if (i == strs[j].length() || strs[j].charAt(i) != strs[0].charAt(i))
     
         return strs[0].substring(0, i);
         return strs[0];
  }
  
  
  public static void main(String args[])
  {
  
  Scanner in=new Scanner(System.in);

  String a[]={"flows","flower","float"};
 prefix obj = new prefix();
  System.out.println("array is  "+obj.longestCommonPrefix(a));
 
  
  }
  
}