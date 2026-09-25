class Solution:
    def isValid(self, s: str) -> bool:
        chars = list(s)
        stack = []
        look = {"[": "]", "{": "}", "(": ")"}
        #while len(chars) > 0:
        for ch in chars:
            # last_el = chars.pop()
            # print(last_el)
            # print(look[last_el])
            # try: 
            #     if(chars.pop(0) == look[last_el]):
            #         continue
            #     else:
            #         break
            # except:
            #     break
            try:
                if not stack:
                    stack.append(ch)
                    continue
                last_el = stack.pop()
                print(stack)
                print(ch, last_el)
                if ch == look[last_el]:
                    continue
                else:
                    stack.extend([last_el, ch])
            except:
                stack.extend([last_el, ch])
                continue
        return len(stack) == 0


