class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched = [False, False, False]
        for t in triplets:
            # skips any bad triplets, ie where any pos in triplet is > target[pos] bc if that triplet is used, bc of max condition youll never be able to go lower back to target
            if any(t[i] > target[i] for i in range(3)):
                # move onto next triplet
                continue
            # only working with triplets that for all positions are <= to target 
            # bc of this, u dont need to model the swap. if u find a triplet where at pos, triplet[pos] == target[pos], then any other triplet u compare it to ie do the operation on will have val <= target[pos] so swap wont happen
            # so u can just imagine swap happened and that val stayed
            for i in range(3):
                if t[i] == target[i]:
                    matched[i] = True
            
        return all(matched)
                
            
            