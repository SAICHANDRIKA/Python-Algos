class treeNode(object):
	def __init__(self, value):
		self.value = value
		self.l = None
		self.r = None
		self.h = 1

class AVLTree(object):

	def insert(self, root, key):
	
		if not root:
			return treeNode(key)
		elif key < root.value:
			root.l = self.insert(root.l, key)
		else:
			root.r = self.insert(root.r, key)

		root.h = 1 + max(self.getHeight(root.l),
						self.getHeight(root.r))

		b = self.getBal(root)

		if b > 1 and key < root.l.value:
			return self.rRotate(root)

		if b < -1 and key > root.r.value:
			return self.lRotate(root)

		if b > 1 and key > root.l.value:
			root.l = self.lRotate(root.l)
			return self.rRotate(root)

		if b < -1 and key < root.r.value:
			root.r = self.rRotate(root.r)
			return self.lRotate(root)

		return root

	def lRotate(self, z):

		y = z.r
		T2 = y.l

		y.l = z
		z.r = T2

		z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
		y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

		return y

	def rRotate(self, z):

		y = z.l
		T3 = y.r

		y.r = z
		z.l = T3

		z.h = 1 + max(self.getHeight(z.l),
						self.getHeight(z.r))
		y.h = 1 + max(self.getHeight(y.l),
						self.getHeight(y.r))

		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.h

	def getBal(self, root):
		if not root:
			return 0

		return self.getHeight(root.l) - self.getHeight(root.r)

	def preOrder(self, root):

		if not root:
			return

		print("{0} ".format(root.value), end="")
		self.preOrder(root.l)
		self.preOrder(root.r)

Tree = AVLTree()
root = None

root = Tree.insert(root, 1)
root = Tree.insert(root, 2)
root = Tree.insert(root, 3)
root = Tree.insert(root, 4)
root = Tree.insert(root, 5)
root = Tree.insert(root, 6)

import random
from time import process_time_ns
num_inserts=[2,4,8,16,32,64,128,256]  
def measure_BStreePerformance(num_inserts):
    Tree = AVLTree()
    insert_time =[]
    for j in num_inserts:
        root = None
        random_list = []
        # generating random numbers using random.randint
        for i in range(j):
            random_list.append(random.randint(0,1000))
        print("Length of random list",len(random_list))
        t1_start = process_time_ns()
        for k in random_list:
            root = Tree.insert(root, k)
        t1_stop = process_time_ns()
        insert_time.append(t1_stop-t1_start)
    return insert_time

insertTimeList = measure_BStreePerformance(num_inserts)
print(insertTimeList)


# # Preorder Traversal
# print("Preorder traversal of the",
# 	"constructed AVL tree is")
# Tree.preOrder(root)
# print(root)

import matplotlib
from matplotlib import pylab as plt
from matplotlib import gridspec as gridspec


matplotlib.rcParams['figure.figsize'] = (8,5)
gs = gridspec.GridSpec(2, 2)
# plt.grid(zorder=0)
plt.plot(num_inserts,insertTimeList,color='blue', marker = ".", linewidth=1, scalex=True,scaley=True, zorder=3)
plt.xlabel('Number of inserts', fontsize=10)
plt.ylabel('Time taken for number of inserts(nanoseconds)', fontsize=10)
plt.title('Performance Measure of AVLTree', loc='Center', fontsize=14)
plt.show()
