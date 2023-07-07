
################*******@Ziyodev*********######################
#--------------- 209. Minimum Size Subarray Sum --------------#
# start | 10:42
# end | 11:01

# class Solution(object):
#     def minSubArrayLen(self, s, nums):
#         """
#         :type target: int
#         :type nums: List[int]
#         :rtype: int
#         """
#         i, j, pres, res = 0 , 0 , 0, len(nums) + 1

#         while j < len(nums):
#                 pres += nums[j]; j += 1
#                 while pres >= s:
#                         res = min(res, j - i)
#                         pres -= nums[i]; i+= 1
#         return res if res != len(nums) + 1 else 0
        

# target = 7
# nums = [2,3,1,2,4,3]
# target = 4
# nums = [1,4,4]

# a = Solution()
# print(a.minSubArrayLen(target, nums))

################*******@Ziyodev*********######################
#--------------- 938. Range Sum of BST --------------#
# start | 17:04
# end | 17:13

# class Solution(object):
#     def rangeSumBST(self, root, low, high):
#         """
#         :type root: TreeNode
#         :type low: int
#         :type high: int
#         :rtype: int
#         """
#         def calculate(root):
#             if root:
#                 if low <= root.val <= high:
#                     self.res += root.val
#                 if low < root.val:
#                     calculate(root.left)
#                 if high > root.val:
#                     calculate(root.right)
#         self.res = 0
#         calculate(root)
#         return self.res
    
# root = [10,5,15,3,7,18]
# low = 7
# high = 15

# a = Solution()
# print(a.rangeSumBST(root, low, high))