class Solution:
    def countBalanced(self, arr):
        def is_balanced(s):
            vowels = set('aeiou')
            v = sum(1 for ch in s if ch in vowels)
            c = len(s) - v
            return v == c

        count = 0
        n = len(arr)
        for i in range(n):
            combined = ''
            for j in range(i, n):
                combined += arr[j]
                if is_balanced(combined):
                    count += 1
        return count
