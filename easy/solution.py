
class Solution(object):

    def __init__(self):
        print('造列删除')

    def minDeletionSize(self, strs):
        """
        给你由 n 个小写字母字符串组成的数组 strs，其中每个字符串长度相等。
        这些字符串可以每个一行，排成一个网格。例如，strs = ["abc", "bce", "cae"] 可以排列为：
        abc
        bce
        cae
        你需要找出并删除 不是按字典序升序排列的 列。
        在上面的例子（下标从 0 开始）中，列 0（'a', 'b', 'c'）和列 2（'c', 'e', 'e'）都是按升序排列的，
        而列 1（'b', 'c', 'a'）不是，所以要删除列 1 。
        返回你需要删除的列数。

        :param strs:
        :return:
        """
        count = 0
        for item in zip(*strs):
            for i in range(len(item) - 1):
                if item[i + 1] < item[i]:
                    count += 1
                    break
        return count

    def towsum(self, nums: list, target):
        """
        给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target的那两个整数，
        并返回它们的数组下标。
        你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。你可以按任意顺序返回答案。

        :param nums:
        :param target:
        :return:
        """
        # for index, item in enumerate(nums):
        #     sub_nums = nums[index+1:]
        #     if target - item in sub_nums:
        #         j = sub_nums.index(target - item)
        #         return [index, sub_nums.index(target - item) + index + 1]
        nums.sort()
        print(nums)
        return None

    def isPalindrome(self, x):
        """

        :param x:
        :return:
        """
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        x_reverse = 0
        while x > x_reverse:
            x_reverse = x_reverse * 10 + x % 10
            x = x // 10

        return x == x_reverse or x == x_reverse / 10

    def oneEditAway(self, first, second):
        """
        字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。 给定两个字符串，
        编写一个函数判定它们是否只需要一次(或者零次)编辑。
        :type first: str
        :type second: str
        :rtype: bool
        """
        n, m = len(first), len(second)
        if abs(n - m) > 1:
            return False

        if n > m:
            temp = first
            first = second
            second = temp
            n = len(first)
            m = len(second)

        i = j = 0
        cnt = 0
        while i < len(first) and j < len(second) and cnt <= 1:
            if first[i] == second[j]:
                i += 1
                j += 1
            else:
                if n == m:
                    cnt += 1
                    i += 1
                    j += 1
                else:
                    j += 1
                    cnt += 1
        return cnt <= 1

    def romanToInt(self, s):
        """

        :param s:
        :return:
        """
        roman_int_dict = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        int_value = 0
        current_char = s[0]
        for next_char in s[1:]:
            if roman_int_dict[current_char] < roman_int_dict[next_char]:
                int_value -= roman_int_dict[current_char]
            else:
                int_value += roman_int_dict[current_char]
            current_char = next_char

        int_value += roman_int_dict[current_char]

        return int_value

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        length = len(strs[0])
        counts = len(strs)
        lcp = ''
        flag = True
        for i in range(length):
            for j in range(counts-1):
                if i < len(strs[j]) and i < len(strs[j+1]) and strs[j][i] == strs[j+1][i]:
                    continue
                else:
                    flag = False
                    break
            if flag:
                lcp += strs[0][i]
            else:
                break

        return lcp

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) % 2 != 0:
            return False

        stack = list()
        pair_dict = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for item in s:
            if item in list(pair_dict.values()):
                stack.append(item)
            else:
                if len(stack) == 0:
                    return False
                else:
                    if pair_dict[item] == stack.pop():
                        continue
                    else:
                        return False
        if len(stack) == 0:
            return True
        else:
            return False




if __name__ == '__main__':
    my_obj = Solution()
    # strs = ["cba", "daf", "ghi"]
    # print(my_obj.minDeletionSize(strs))
    nums = [2, 7, 11, 15]
    target = 9
    # ret_value = my_obj.towsum(nums, target)
    # ret_value = my_obj.isPalindrome(121)
    ret_value = my_obj.romanToInt('III')
    print(ret_value)

