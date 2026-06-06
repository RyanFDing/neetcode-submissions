class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #process array and sort counts in dict

        counts = {}

        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num]+=1
        
        sortedcounts = list(dict(sorted(counts.items(), key=lambda item: item[1], reverse=True)))
        ans = []
        for i in range(0, k, 1):
            ans.append(sortedcounts[i])

        return ans