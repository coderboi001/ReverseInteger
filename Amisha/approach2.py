# Time Complexity --> O(n)

class Solution:
    def reverse(self, x: int) -> int:
        if x in range(-2**31, 2**31 - 1):
            y = x
            sum = 0
            if x < 0:
                x = x * -1
            while x > 0:
                rem = x % 10
                sum = sum * 10 + rem
                x = x // 10
            if sum in range(-2**31, 2**31 - 1):
                if y < 0:
                    return sum * -1
                else:
                    return sum
            else:
                return 0
        else:
            return 0