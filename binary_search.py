#-*- coding: utf-8 -*-
# binary search
"""
    在有序数组中查找某一特定元素的搜索算法, 搜索过程从数组的中间元素开始，
    如果中间元素正好是要查找的元素，则搜索过程结束；如果某一特定元素大于
    或者小于中间元素，则在数组大于或小于中间元素的那一半中查找，而且跟开
    始一样从中间元素开始比较。如果在某一步骤数组为空，则代表找不到。这种
    搜索算法每一次比较都使搜索范围缩小一半。
"""
import numpy as np
class Search(object):
    """docstring for Search"""
    def BinarySearch(self, a, target):
        low = 0
        high = len(a) - 1
        while low <= high:
            mid = (low + high)/2
            mid_value = a[mid]
            if mid_value < target:
                low = mid + 1
            elif mid_value > target:
                high = mid - 1
            else:
                print "find %s at index %d" %(str(target), mid)
                return 1
        return -1

    def BinarySearch_Recursive(self, a, low, high, target):
        if low > high or len(a) <= 0:
            return -1
        mid = (low + high) / 2
        mid_value = a[mid]
        if mid_value == target:
            print "find %s at index %d" %(str(target), mid)
            return 1
        elif mid_value < target:
            self.BinarySearch_Recursive(a, mid+1, high, target)
        elif mid_value > target:
            self.BinarySearch_Recursive(a, low, mid-1, target)




if __name__ == '__main__':
    rhigh = 100
    a = list(set(list(np.random.randint(rhigh, size = 10))))
    a.sort()
    target = a[np.random.randint(len(a))]
    print "list is ",a
    print "target is ", target

    S = Search()
    S.BinarySearch(a, target)
    S.BinarySearch_Recursive(a, 0, len(a)-1, target)