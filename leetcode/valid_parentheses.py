class Solution:
    def isValid(self, s: str) -> bool:
        lefty = '{[('
        righty = '}])'
        brackets = []
        valid = True
        for i in range(len(s)):
            if s[i] in lefty:
                brackets.append(s[i])
            else:
                index_righty = righty.index(s[i])
                if len(brackets) > 0:
                    set_item = brackets.pop()
                    if set_item != lefty[index_righty]:
                        valid = False
                else:
                    valid = False
        if len(brackets) > 0:
            valid = False
        return valid


    def isBalanced(self, s: str) -> bool:
        lefty = '{[('
        righty = '}])'
        brackets = set()
        for i in range(len(s)):
            if s[i] in lefty:
                brackets.add(s[i])
            if s[i] in righty:
                brackets.discard(lefty[righty.index(s[i])])
        return len(brackets) == 0
