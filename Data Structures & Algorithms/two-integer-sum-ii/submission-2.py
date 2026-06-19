class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i,j = 0,len(numbers)-1
        while i <len(numbers):
            while j >0:
                if (numbers[i]+numbers[j]==target):
                    return [i+1, j+1]
                elif (numbers[i]+numbers[j]<target):
                    i+=1
                    j=len(numbers)-1
                else:
                    j-=1
#ideas:
#increasing 
#start frm end of each row
#if biggest at end is less: skip row
#else decrease
#start looping sum, if over skip iteration
#2 pointers
#problem's furly: O(1) runtime
#edge cases: alyways has solution



