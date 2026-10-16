class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        seen = []
        alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        for i in sentence.lower():
            if i in alphabet and i not in seen:
                seen.append(i)
            elif i in alphabet and i in seen:
                continue
            else:
                return False
        if len(seen) == len(alphabet):
            return True
        else:
            return False