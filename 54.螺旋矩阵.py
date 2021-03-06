#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#
# https://leetcode-cn.com/problems/spiral-matrix/description/
#
# algorithms
# Medium (36.18%)
# Likes:    171
# Dislikes: 0
# Total Accepted:    16.6K
# Total Submissions: 46K
# Testcase Example:  '[[1,2,3],[4,5,6],[7,8,9]]'
#
# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
#
# 示例 1:
#
# 输入:
# [
# ⁠[ 1, 2, 3 ],
# ⁠[ 4, 5, 6 ],
# ⁠[ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]
#
#
# 示例 2:
#
# 输入:
# [
# ⁠ [1, 2, 3, 4],
# ⁠ [5, 6, 7, 8],
# ⁠ [9,10,11,12]
# ]
# 输出: [1,2,3,4,8,12,11,10,9,5,6,7]
#
#
#

# from typing import List
# import pysnooper

# class Solution:
#     # @pysnooper.snoop()
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         if not matrix:
#             return []
#         else:
#             return matrix[0] + self.spiralOrder(
#                 list(map(list, zip(*(matrix[1:]))))[::-1])


# 简洁的写法
class Solution:
    # @pysnooper.snoop()
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        return matrix and matrix[0] + self.spiralOrder(
            list(map(list, zip(*(matrix[1:]))))[::-1])
