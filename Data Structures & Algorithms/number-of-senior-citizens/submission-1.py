class Solution:
    def countSeniors(self, details: list[str]) -> int:
        count = 0
        for i in details:
            # The age is at character positions 11 and 12
            age = int(i[11:13])
            if age > 60:
                count += 1
        return count
