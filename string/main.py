################*******@Ziyodev*********######################
#-------- 2710. Remove Trailing Zeros From a String ------#

# my solution

# class Solution(object):
#     def removeTrailingZeros(self, num):
#         """
#         :type num: str
#         :rtype: str
#         """
#         old = num[-1]
#         s = 0
#         for i in num[::-1]:
#             if old == "0":
#                 s += 1
#                 old = i
#         r = len(num) - s+1
#         return num[:r]
    
# compact solution

# class Solution(object):
#     def removeTrailingZeros(self, num):
#         """
#         :type num: str
#         :rtype: str
#         """
#         num2 = int(num)
#         while(num2%10==0):
#             num2=num2/10
#         return str(num2)

################*******@Ziyodev*********######################