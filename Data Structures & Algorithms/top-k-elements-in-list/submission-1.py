class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for n in nums:
            d[n] = d.get(n, 0) + 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in d.items():
            bucket[count].append(num)

        resultado = []
        for count in range(len(nums), 0, -1):
            for num in bucket[count]:
                resultado.append(num)
                if len(resultado) == k:
                    return resultado
