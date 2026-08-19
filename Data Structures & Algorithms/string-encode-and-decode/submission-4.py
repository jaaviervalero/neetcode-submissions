class Solution:

    def encode(self, strs: List[str]) -> str:
        sol = ""
        for word in strs:
            sol += f"{len(word)}#{word}"
        return sol

    def decode(self, s: str) -> List[str]:
        sol = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            end = int(s[i:j])
            word = s[j+1:j+end+1]
            sol.append(word)
            i = j + end +1

        return sol