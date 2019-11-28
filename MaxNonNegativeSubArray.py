class Solution:
    # @param A : list of integers
    # @return a list of integers
    def maxset(self, A):
        start = 0
        end = 0
        currentStart = 0
        currentEnd = 0
        sum = -1 # to support 0,0,-1,0 case
        currentSum = 0
        bReset = False
        bFound = False

        for i in range(len(A)):
            if A[i] > -1:
                bFound = True
                if bReset == True:
                    if (currentSum > sum):
                        start = currentStart
                        end = currentEnd
                        sum = currentSum
                    currentStart = i
                    currentEnd = i
                    currentSum = 0
                    bReset = False
                currentEnd = i
                currentSum += A[i]
            else:
                bReset = True

        if (currentSum > sum):
            start = currentStart
            end = currentEnd

        if bFound == False:
            return []

        return A[start:end+1]