class Solution:
    def cntSubarrays(self, arr, k):
        x=0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)+1):
                if sum(arr[i:j])==k:
                    x+=1
        return(x)
