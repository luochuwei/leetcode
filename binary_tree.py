#-*- coding: utf-8 -*-
# binary tree

class Node(object):
	"""
	二叉树左右枝, https://github.com/qiwsir/algorithm/blob/master/binary_tree.md
	二叉查找树（英语：Binary Search Tree），也称二叉搜索树、有序二叉树，排序二叉树，是指一棵空树或者具有下列性质的二叉树：
	任意节点的左子树不空，则左子树上所有结点的值均小于它的根结点的值；
	任意节点的右子树不空，则右子树上所有结点的值均大于它的根结点的值；
	任意节点的左、右子树也分别为二叉查找树；
	没有键值相等的节点。
	"""
	def __init__(self, arg):
		"""
		节点结构
		"""
		self.left = None
		self.right = None
		self.data = None

	def insert(self, data):
		"""
		插入节点数据
		"""
		if data < self.data:
			if self.left is None:
				self.left = Node(data)
			else:
				self.left.insert(data)
		elif data > self.data:
			if self.right is None:
				self.right = Node(data)
			else:
				self.right.insert(data)

	def lookup(self, data, parent = None):
		"""
		遍历二叉树
		此方法用于查找树中的某个节点，如果找到了，就返回该节点，否则返回None。
		为了方便，也返回父节点。
		"""
		if data < self.data:
			if self.left is None:
				return None, None
			else:
				return self.left.lookup(data, self)
		elif data > self.data:
			if self.right is None:
				return None, None
			else:
				return self.right.lookup(data, self)
		else:
			return self, parent

	def children_count(self):
	    """
	    子节点个数
	    """
	    cnt = 0
	    if self.left:
	        cnt += 1
	    if self.right:
	        cnt += 1
	    return cnt

	def delete(self, data):
		"""
		删除节点
		"""
		node, parent = self.lookup(data)
		if node is not None:
			children_count = node.children_count()
			if children_count == 0:
				#如果没有子节点，直接删除
				if parent.left is node:
					parent.left = None
				else:
					parent.right = None
			elif children_count == 1:
				# 如果有一个子节点，则让子节点上移替换该节点（该节点消失)
				if node.left:
					n = node.left
				else:
					n = node.right
				if parent:
					if parent.left is node:
						parent.left = n
					else:
						parent.right = n
				del node
			elif children_count == 2:
				# 如果有两个子节点，则要判断节点下所有叶子
				parent = node
				successor = node.right
				while successor.left:
					parent = successor
					successor = successor.left
				node.data = successor.data
				if parent.left == successor.right:
					parent.left = successor.right
				else:
					parent.right = successor.right

	def compare_trees(self, node):
		"""
		比较两棵树
		"""
		if node is None:
			return False
		if self.data != node.data:
			return False
		res = True
		if self.left is None:
			if node.left:
				return False
		else:
			res = self.left.compare_trees(node.left)
		if res is False:
			return False
		if self.right is None:
			if node.right:
				return False
		else:
			res = self.right.compare_trees(node.right)
		return res

	def print_tree(self):
		"""
		按顺序打印数的内容
		"""
		if self.left:
			self.left.print_tree()
		print self.data,
		if self.right:
			self.right.print_tree()

	def tree_data(self):
		"""
		二叉树数据结构
		"""
		stack = []
		node = self
		while stack or node:
			if node:
				stack.append(node)
				node = node.left
			else:
				node = stack.pop()
				yield node.data
				node = node.right



