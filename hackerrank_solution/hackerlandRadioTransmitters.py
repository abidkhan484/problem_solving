n, k = map(int, input().split())
mylist = list(map(int, input().split()))

mylist.sort()

# p var is used for starting position of our counting that can connect
# tmp var is used for checking if any of middle position that we can use
p = 0; count = 1; tmp = 1
for i in range(1, n):

    if mylist[i] > (mylist[p]+k):
        # this if statement is for checking if the starting position greater than 1
        if (i-p) == 1:
            count += 1; p = i
        else:
            if tmp:
                # this part is used for checking of first use of the middle tower
                # if we didn't use middle tower and range of the building is on the tower
                # then the if statement is used otherwise we just use a transmitter on the building
                if (mylist[i-1]+k) >= mylist[i]:
                    tmp = 0; p = i-1
                else:
                    count += 1; p = i
            else:
                # if middle tower is already used then the statement works
                count += 1; p = i; tmp = 1

print(count)

'''
# problem tester's code

#include <bits/stdc++.h>

using namespace std;

int a[100000+2];
int main(){

    int n, m;
    cin>>n>>m;
    for(int i=1;i<=n;i++)
    { 
        cin>>a[i]; 
    }
  
    sort(a+1,a+n+1);
    int ans = 0, i=1;
    
    # this while loop just worked wow
    while(i<=n)
    {
        int maxijabe = a[i] + m;
        int j=i;
        ans = ans + 1;
        while(j<=n and a[j]<=maxijabe){
            i = j;
            j++;
        }
        
        maxijabe = a[i]+m;
        j = i;
        while(j<=n and a[j]<=maxijabe){
            i = j;
            j++;
        }
        i = i + 1;
    }
    cout<<ans<<endl;

    return 0;
}

'''
