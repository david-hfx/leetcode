#
# @lc app=leetcode.cn id=66 lang=python3
#
# [66] 加一
#
# https://leetcode-cn.com/problems/plus-one/description/
#
# algorithms
# Easy (39.46%)
# Likes:    299
# Dislikes: 0
# Total Accepted:    59.8K
# Total Submissions: 151.6K
# Testcase Example:  '[1,2,3]'
#
# 给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。
#
# 最高位数字存放在数组的首位， 数组中每个元素只存储一个数字。
#
# 你可以假设除了整数 0 之外，这个整数不会以零开头。
#
# 示例 1:
#
# 输入: [1,2,3]
# 输出: [1,2,4]
# 解释: 输入数组表示数字 123。
#
#
# 示例 2:
#
# 输入: [4,3,2,1]
# 输出: [4,3,2,2]
# 解释: 输入数组表示数字 4321。
#
#
#
# !简单的思路
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        lens = len(digits)
        for i in range(lens - 1, -1, -1):
            if digits[i] + 1 > 9:
                digits[i] = 0
                if i == 0:
                    return [1] + digits
                continue
            else:
                digits[i] += 1
                break
        return digits
