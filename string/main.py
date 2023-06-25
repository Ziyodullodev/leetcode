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

#------------------- 344. Reverse String -----------------#
# start | 23:11
# end | 23:44

# class Solution(object):
#     def reverseString(self, s):
        # """
        # :type s: List[str]
        # :rtype: None Do not return anything, modify s in-place instead.
        # """
#         sana = 0
#         list_len = (len(s) / 2)
#         if list_len %2 != 0:
#             list_len - 1  
#         while sana < list_len:
#             head = s[sana]
#             s[sana] = s[-1-sana]
#             s[-1-sana] = head
#             sana += 1
#         return s
        
# s = ["s","a","l","o","m"]   
# test = Solution()
# answer = test.reverseString(s)
# print(answer)

######################### compact solution ##########################

# class Solution(object):
#     def reverseString(self, s):
#         """
#         :type s: List[str]
#         :rtype: None Do not return anything, modify s in-place instead.
#         """
#         l=[]
#         l.append(s.reverse())
#         return l


################*******@Ziyodev*********######################

#---------------2744 .Find Maximum Number of String Pairs -----------------#
# start | 23:44
# end | 23:51


# class Solution(object):
#     def maximumNumberOfStringPairs(self, words):
#         """
#         :type words: List[str]
#         :rtype: int
#         """
#         s = 0
#         for i in range(len(words)):
#             for j in range(i+1, len(words)):
#                 if words[i] == words[j][::-1]:
#                     s+=1
#         return s
    

# words = ["cd","ac","dc","ca","zz"]

# a = Solution()
# print(a.maximumNumberOfStringPairs(words))

################*******@Ziyodev*********######################
