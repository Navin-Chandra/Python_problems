#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
import math

def isPrime(n):
     
    # Corner cases
    if(n <= 1):
        return False
    if(n <= 3):
        return True
     
    # This is checked so that we can skip
    # middle five numbers in below loop
    if(n % 2 == 0 or n % 3 == 0):
        return False
     
    for i in range(5,int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
     
    return True
    
    
def nextPrime(N):
    
    # code here to find next prime number
    # return next prime number
    # Base case
    if (N <= 1):
        return 2
 
    prime = N
    found = False
 
    # Loop continuously until isPrime returns
    # True for a number greater than n
    while(not found):
        prime = prime + 1
 
        if(isPrime(prime) == True):
            found = True
 
    return prime
        

#{ 
 # Driver Code Starts.
if __name__ == '__main__':
    t= int(input())
    for _ in range(t):
        n=int(input())
        
        ans = nextPrime(n)
        print(ans)
# } Driver Code Ends