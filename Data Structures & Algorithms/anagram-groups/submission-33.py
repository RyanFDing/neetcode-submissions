class Solution:

    #iter - make new dict with sort all strings, map sorted to initial indices.
    #procedure - hashmap
    #map key =  strs indices
    #map value = sort(strs[key])
    #iterate through indices of map i
    #iterate through i+1 to end
    #if == append strs[index] to newresult, delete map index (no iterate if so)
    #at end append newresult,
    #do until done


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        results = {}
        for s in strs:
            key = tuple(sorted(s))
            if key not in results:
                results[key] = []
            results[key].append(s)
        return list(results.values())




