import java.util.*;
public class Main
{
	public static void main(String[] args) {
		Scanner sc=new Scanner(System.in);
		int t=sc.nextInt();
		while(t-->0)
		{
		    int n=sc.nextInt();
		    int arr[]=new int[n];
		    int num[]=new int[n];
		    int zero=0,one=0;
		    for(int i=0;i<n;i++)
		    {
		        arr[i]=sc.nextInt();
		    }
		    for(int i=0;i<n;i++)
		    {
		        num[i]=sc.nextInt();
		    }
		    int flag=0;
		    for(int i=0;i<n-1;i++)
		    {
		        if(arr[i]>arr[i+1])
		        {
		            flag=1;
		            break;
		        }
		    }
		    if(flag==0)
		    {
		        System.out.println("Yes");
		    }
		    else
		    {
		        for(int i=0;i<n;i++)
		        {
		            if(num[i]==0)
		            {
		                zero++;
		            }
		            else
		            {
		                one++;
		            }
		        }
		        if(zero!=0 && one!=0)
		        {
		            System.out.println("Yes");
		        }
		        else
		        {
		            System.out.println("No");
		        }
		    }
		}
	}
}
