import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n=sc.nextInt();
		if(n>=0)
		{
		    System.out.println(n);
		}
		else
		{
		    int num1;
		    int num2;
		    num1=n/10;
		    num2=n/100 * 10 + n%10; 
		    System.out.println(Math.max(num1,num2));
		}
	}
}
