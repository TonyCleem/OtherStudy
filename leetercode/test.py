class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []
        first_str = ""
        second_srt = ""
        other_str = ""
        for i in strs:
            for x in i:
                if x not in first_str:
                    first_str += x
                elif x in first_srt:
                    second_str += x
            other_str = second_str          
            first_str = ""
            second_str = ""
        strs = []
        strs.append(other_str)
        result strs