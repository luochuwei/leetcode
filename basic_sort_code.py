#-*- coding: utf-8 -*-
import numpy as np
from sys import argv


class basic_sort(object):
    """
        basic sort algorithm python code
        总结各种算法之前，现介绍下几个概念：
        1、稳定度：稳定排序算法会依照相等的关键（换言之就是值）维持纪录的相对次序。也就是一个排序算法是稳定的，
        就是当有两个有相等关键的纪录R和S，且在原本的串行中R出现在S之前，在排序过的串行中R也将会是在S之前。
        2、计算的复杂度（最差、平均、和最好表现），依据串行（list）的大小（n）。一般而言，好的表现是O(n log n)，
        且坏的行为是O(n2)。对于一个排序理想的表现是O(n)。仅使用一个抽象关键比较运算的排序算法总平均上总是至少需要O(n log n)。
        .
        稳定排序：
        * 泡沫排序（bubble sort） — O(n²)
        * 插入排序 （insertion sort）— O(n²)
        * 桶排序 （bucket sort）— O(n); 需要 O(k) 额外空间
        * 计数排序 (counting sort) — O(n+k); 需要 O(n+k) 额外空间
        * 合并排序 （merge sort）— 平均 O(n log n)，最差O(n log n)，最好O(n); 需要 O(n) 额外空间
        * 二叉排序树排序 （Binary tree sort） — O(n log n)期望时间; O(n²)最坏时间; 需要 O(n) 额外空间
        * 基数排序 （radix sort）— O(n·k); 需要 O(n) 额外空间
        .
        不稳定排序
        * 选择排序 （selection sort）— O(n²)
        * 希尔排序 （shell sort）— O(n log n) 如果使用最佳的现在版本
        * 堆排序 （heapsort）— O(n log n)
        * 快速排序 （quicksort）— O(n log n) 期望时间, O(n²) 最坏情况; 对于大的、乱数串行一般相信是最快的已知排序

    """
    def swap(self, list_a, i, j):
        tmp = list_a[i]
        list_a[i] = list_a[j]
        list_a[j] = tmp
        return list_a

    def bubble_sort(self, list_a):
        """
            冒泡排序，时间复杂度O(n^2)
        """
        for i in xrange(len(list_a)):
            for j in xrange(0, len(list_a)-1-i):
                # print list_a
                if list_a[j] >= list_a[j+1]:
                    list_a = self.swap(list_a, j, j+1)
        return list_a

    def select_sort(self, list_a):
        """
            选择排序，时间复杂度O(n^2)，选出之后序列中最小的与当前值进行交换, 和冒泡排序类似
        """
        for i in xrange(len(list_a)):
            min_index = i
            min_value = list_a[i]
            for j in xrange(i, len(list_a)):
                if list_a[j] <= min_value:
                    min_index = j
                    min_value = list_a[j]
            list_a = self.swap(list_a, i, min_index)

        return list_a

    def insert_sort(self, list_a):
        if len(list_a) == 1:
            return list_a
        for i in xrange(1, len(list_a)):
            temp = list_a[i]
            j = i - 1
            while j >= 0 and temp < list_a[j]:
                list_a[j + 1] = list_a[j]
                j -= 1
            list_a[j+1] = temp
        return list_a

    def insert_sort_recursive(self, list_a):
        if len(list_a) == 1:
            return list_a
        new_sort_list = self.insert_sort_recursive(list_a[1:])

        for i in xrange(len(new_sort_list)):
            if list_a[0] <= new_sort_list[i]:
                return new_sort_list[:i] + [list_a[0]] + new_sort_list[i:]
        return new_sort_list + [list_a[0]]

    def shell_sort(self, list_a):
        """
        步长的选择是希尔排序的重要部分。只要最终步长为1任何步长序列都可以工作。
        算法最开始以一定的步长进行排序。然后会继续以一定步长进行排序，最终算法以步长为1进行排序。
        当步长为1时，算法变为插入排序，这就保证了数据一定会被排序。
        """
        n = len(list_a)
        #初始步长
        gap = n/2   #round 是四舍五入
        while gap > 0:
            for i in xrange(gap, n):
                temp = list_a[i]
                j = i
                while j >= gap and list_a[j-gap] > temp:
                    list_a[j] = list_a[j - gap]
                    j -= gap
                list_a[j] = temp
            gap = gap / 2
        return list_a

    def merge_sort_recursive(self, list_a):
        """
        归并排序算法是采用分治法（Divide and Conquer）的一个非常典型的应用，且各层分治递归可以同时进行。
        """

        if len(list_a) <= 1:
            return list_a

        def merge(left, right):
            l, r = 0, 0
            result = []
            while l < len(left) and r < len(right):
                if left[l] < right[r]:
                    result.append(left[l])
                    l += 1
                else:
                    result.append(right[r])
                    r += 1
            result += left[l:]
            result += right[r:]
            return result
        mid_index = len(list_a) // 2   # // 是python地板除，无论怎样都会舍弃小数部分
        left = self.merge_sort_recursive(list_a[:mid_index])
        right = self.merge_sort_recursive(list_a[mid_index:])

        return merge(left, right)

    def quik_sort(self, list_a):
        """
            快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。
            步骤:
                1. 从数列中挑出一个元素，称为”基准”（pivot），
                2. 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。
                   在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（partition）操作。
                3. 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
        """
        if len(list_a) <= 1:
            return list_a
        else:
            pivot = list_a[0]
            return self.quik_sort([x for x in list_a[1:] if x < pivot]) + [pivot] + self.quik_sort([y for y in list_a[1:] if y >= pivot])

    def _partition(self, list_a, left, right, pivotIndex):
        pivot_val = list_a[pivotIndex]
        self.swap(list_a, pivotIndex, right)
        storeIndex = left
        for i in xrange(left, right-1):
            if list_a[i] <= pivot_val:
                self.swap(list_a, storeIndex, i)
                storeIndex += 1
        self.swap(list_a, storeIndex, right)
        return storeIndex
    def _quik_sort_inplace(self, list_a, left, right):
        if left >= right:
            return 0
        pivotIndex = 0
        pivotNewIndex = self._partition(list_a, left, right, pivotIndex)
        self._quik_sort_inplace(list_a, left, pivotNewIndex-1)
        self._quik_sort_inplace(list_a, pivotNewIndex+1, right)

    def quik_sort_inplace(self, list_a):
        self._quik_sort_inplace(list_a, 0, len(list_a)-1)
        return list_a

    def heap_sort(self, list_a):
        """
            堆排序（Heapsort）是指利用堆这种数据结构所设计的一种排序算法。
            堆积是一个近似完全二叉树的结构，并同时满足堆积的性质：即子结点的键值或索引总是小于（或者大于）它的父节点。
            步骤
                1. 创建最大堆:将堆所有数据重新排序，使其成为最大堆
                2. 最大堆调整:作用是保持最大堆的性质，是创建最大堆的核心子程序
                3. 堆排序:移除位在第一个数据的根节点，并做最大堆调整的递归运算
        """
        def sift_down(l, start, end):
            """最大堆调整"""
            root = start
            while True:
                child = 2 * root + 1
                if child > end:
                    break
                if child + 1 <= end and l[child] < l[child + 1]:
                    child += 1
                if l[root] < l[child]:
                    l = self.swap(l, root, child)
                    root = child
                else:
                    break

        #创建最大堆
        """
        建立最大堆的过程是自底向上地调用最大堆调整程序将一个数组A[1.....N]
        变成一个最大堆。将数组视为一颗完全二叉树，从其最后一个非叶子节点（n/2）开始调整。调整过程如下图所示
        """
        for start in xrange((len(list_a)-2) // 2, -1, -1):
            sift_down(list_a, start, len(list_a) - 1)

        #堆排序
        for end in xrange((len(list_a)-1), 0, -1):
            self.swap(list_a, 0, end)
            sift_down(list_a, 0, end-1)
        return list_a

    def count_sort(self, list_a):
        """
            步骤
                1. 找出待排序的数组中最大和最小的元素
                2. 统计数组中每个值为i的元素出现的次数，存入数组 C 的第 i 项
                3. 对所有的计数累加（从C中的第一个元素开始，每一项和前一项相加）
                4. 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1
        """
        min_value = 99999999999
        max_value = 0
        #取得最大最小值
        for x in list_a:
            if x > max_value:
                max_value = x
            if x < min_value:
                min_value = x

        #创建数组C
        count_c = [0] * (max_value - min_value + 1)
        for index in list_a:
            count_c[index - min_value] += 1
        index = 0
        print count_c

        #填值
        for a in xrange(max_value - min_value + 1):
            for b in xrange(count_c[a]):
                list_a[index] = a + min_value
                index += 1
                print list_a
        return list_a







# print argv



bs = basic_sort()
rhigh = 100
a = list(list(np.random.randint(rhigh, size = 10)))
print a

print bs.quik_sort_inplace(a)
