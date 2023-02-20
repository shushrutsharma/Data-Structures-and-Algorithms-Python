# add to array form of integer | leetcode 989 | https://leetcode.com/problems/add-to-array-form-of-integer

class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]:
        n = len(num) - 1
        carry = 0
        while k or carry:
            k, digit = k // 10, k % 10
            each = carry + digit
            if n < 0:
                num.insert(0, each % 10)
            else:
                each = each + num[n]
                num[n] = each % 10
            carry = each // 10
            n -= 1

        return num

