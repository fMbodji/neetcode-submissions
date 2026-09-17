class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        print(encoded_str)
        return encoded_str    


    def decode(self, s: str) -> List[str]:
        decoded_str = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j+= 1
            length = int(s[i:j])
            decoded_word = s[j + 1 : j + 1 + length]
            decoded_str.append(decoded_word)
            i = j + 1 + length
        return decoded_str
