class Solution:

    def encode(self, strs: List[str]) -> str:
        output = []
        if strs == []:
            return "None"
        for s in strs:
            encoded_str = ""
            for ch in s:
                ordinate = ord(ch) + 2
                encoded_str += chr(ordinate)
            output.append(encoded_str)
        return " ".join(output)

    def decode(self, s: str) -> List[str]:
        if s == "None":
            return []
        output = []
        for d in s.split(" "):
            decoded_chars = []
            for ch in d:
                ordinate = ord(ch) - 2
                decoded_chars.append(chr(ordinate))
            print(decoded_chars)
            decoded_str = "".join(decoded_chars)
            output.append(decoded_str)
        return output
