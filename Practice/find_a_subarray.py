"""Given an unsorted array A of size N that contains only non-negative integers, find a continuous sub-array which adds to a given number S.

 

Example 1:

Input:
N = 5, S = 12
A[] = {1,2,3,7,5}
Output: 2 4
Explanation: The sum of elements 
from 2nd position to 4th position 
is 12.
 

Example 2:

Input:
N = 10, S = 15
A[] = {1,2,3,4,5,6,7,8,9,10}
Output: 1 5
Explanation: The sum of elements 
from 1st position to 5th position
is 15.
 

Your Task:
You don't need to read input or print anything. The task is to complete the function subarraySum() which takes arr, N and S as input parameters and returns a list containing the starting and ending positions of the first such occurring subarray from the left where sum equals to S. The two indexes in the list should be according to 1-based indexing. If no such subarray is found, return an array consisting only one element that is -1.

 

Expected Time Complexity: O(N)
Expected Auxiliary Space: O(1)
"""

class Solution:
    def subArraySum(self,arr, n, s):
        for i in range(n):
            sum_a = arr[i]
            for j in range(i+1, len(arr)):
                sum_a += arr[j]
                if sum_a == s:
                    return (i+1,j+1)
                elif sum_a > s:
                    break
                else:
 
                    pass
if __name__ == "__main__":
    A = [1,2,3,4,5,6,7,8,9,10]
    subArraySum(A,10,12)
         
         
      
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                
                