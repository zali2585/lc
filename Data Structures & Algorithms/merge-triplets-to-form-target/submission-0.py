class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        matched = [False, False, False]
        for t in triplets:
            # skips any bad triplets, ie where any pos in triplet is > target[pos] bc if that triplet is used, bc of max condition youll never be able to go lower back to target
            if any(t[i] > target[i] for i in range(3)):
                # move onto next triplet
                continue

            for i in range(3):
                if t[i] == target[i]:
                    matched[i] = True
            
        return all(matched)
                
            
            