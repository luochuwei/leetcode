#-*- coding: utf-8 -*-
class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: List[str]
        """
        res = []
        length = len(s)
        # DP[j]：表示[j:length)能否切分，使得子串能够被包含在worddict中。
        DP = [False] * (length + 1)
        DP[length] = True
        # bottom to up
        for j in range(length, -1, -1):
            for i in range(j - 1, -1, -1):
                if DP[j] and (s[i: j] in wordDict):
                    DP[i] = True

        def DFS(index, valueList):
            # cut
            if DP[index]:  # 从下标Index开始，划分子串，能够满足题目条件，就进行递归
                if index == length:
                    res.append(valueList[1:])
                    return

                #记得这边是length+1，i能够达到的最大的是length,在切片的时候[index:i]，最终只能访问到i-1，最大就是length-1.
                for i in range(index + 1, length + 1): 
                    if s[index:i] in wordDict and DP[i]:
                        DFS(i, valueList + " " + s[index : i])

        DFS(0, "")
        return res
