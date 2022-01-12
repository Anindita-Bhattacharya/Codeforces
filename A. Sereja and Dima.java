import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int n;
		n=sc.nextInt();
		int arr[]=new int[n];
		for(int i=0;i<n;i++)
		{
		    arr[i]=sc.nextInt();
		}
		int first=0;
		int last=n-1;
		int sereja=0;
		int dima=0;
		int count=0;
		while(first<=last)
		{
		    if(count%2==0)
		    {
		        if(arr[first]>arr[last])
		        {
		            count++;
		            
		            sereja=sereja+arr[first];
		            first++;
		        }
		        else
		        {
		            count++;
		            
		            sereja=sereja+arr[last];
		            last--;
		        }
		    }
		    else
		    {
		         if(arr[first]>arr[last])
		        {
		            count++;
		            
		            dima=dima+arr[first];
		            first++;
		        }
		        else
		        {
		            count++;
		           
		            dima=dima+arr[last];
		             last--;
		            
		        }
		        
		    }
		}
		    System.out.print(sereja+" "+dima);
		       
	}
}
