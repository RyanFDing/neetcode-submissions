class Solution:

    def encode(self, strs: List[str]) -> str:
        if (len(strs) == 0):
            return "[]"
        ret = ""
        for string in strs:
            ret+=string
            ret+="~"
        return ret[:-1]
        #list of strings
        #turn into big string
        #return big string


    def decode(self, s: str) -> List[str]:
        if (s == "[]"):
            return []
        return s.split("~")