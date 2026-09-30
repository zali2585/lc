class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq
        heap = []
        res = []
        freq = Counter(nums)

        for n, count in freq.items():
            heapq.heappush(heap, (-count, n))

        for i in range(k):
            i, j = heapq.heappop(heap)
            res.append(j)
        return res


    
    """
    main idea: max heap where the elements are entered into heap by frequency 
    for i in range(k):
        pop top
    """





        