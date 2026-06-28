#username - ronbenhaim\kaharamani
#id1      - 208610212 
#name1    - ronbenhaim 
#id2      - 322549478
#name2    - kaharamani  


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	@type key: int or None
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.bal_status = True

		

	"""returns whether self is not a virtual node 
	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.key != None



"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.  
	"""
	def __init__(self):
		self.root = None
		self.Tsize = 0
		self.max = None
		self.bal_cnt = 0

	"""searches for a node in the dictionary corresponding to the key
	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key
	"""
	def search(self, k):
		if self.root is None:
			return None
		node = self.get_root()
		while (node.is_real_node()):
			if k == node.key:
				return node
			elif k > node.key:
				node = node.right
			else:
				node = node.left	
		return None

	#####################
	# ASSISTING METHODS #
	#####################
	"""makes a right rotation on the pivot node
	@type node: AVLNode
	@rtype: None
	@returns: a valid AVL tree
	"""
	def rotate_right(self, node):
		#		z										y
		#	   / \		   Right Rotation			   / \
		#	  y   t2   =====================>		  x	  z
		#	 / \										 / \
		#   x   t1										t1  t2			
		z = node
		p = z.parent
		y = z.left
		x = y.left
		t1 = y.right
		t2 = z.right
		old_bal = 0
		old_bal += 1 if z.bal_status else 0
		old_bal += 1 if y.bal_status else 0
		z.parent = y
		z.left = t1
		z.right= t2
		z.height = 1+max(t1.height,t2.height)
		y.parent = p 
		y.left = x
		y.right = z
		y.height = 1+max(x.height,z.height)
		if p is not None:
			if p.left is z:
				p.left = y
			else:
				p.right = y
		new_bal = 0
		z.bal_status = True if self.check_balance_factor(z) == 0 else False
		y.bal_status = True if self.check_balance_factor(y) == 0 else False
		new_bal += 1 if z.bal_status else 0
		new_bal += 1 if y.bal_status else 0
		dif = new_bal - old_bal
		self.bal_cnt += dif
		if self.root == z:
			self.root = y
		t1.parent = z
		


	"""makes a left rotation on the pivot node
	@type node: AVLNode
	@rtype: None
	@returns: a valid AVL tree
	"""
	def rotate_left(self, node):
		#		z										y
		#	   / \		   Left Rotation			   / \
		#	  t1  y   =====================>		  z	  x
		#	 	 / \ 								 / \
		#		t2  x								t1  t2
		p = node.parent
		z = node
		y = node.right
		x = y.right
		t1 = z.left
		t2 = y.left
		if self.root == z:
			self.root = y
		old_bal = 0
		old_bal += 1 if z.bal_status else 0
		old_bal += 1 if y.bal_status else 0
		z.parent = y
		z.left = t1
		z.right= t2
		z.height = 1+max(t1.height,t2.height)
		y.parent = p 
		y.left = z
		y.right = x
		y.height = 1+max(z.height,x.height)
		if p is not None:
			if p.left is z:
				p.left = y
			else:
				p.right = y
		new_bal = 0
		z.bal_status = True if self.check_balance_factor(z) == 0 else False
		y.bal_status = True if self.check_balance_factor(y) == 0 else False
		new_bal += 1 if z.bal_status else 0
		new_bal += 1 if y.bal_status else 0
		dif = new_bal - old_bal
		self.bal_cnt += dif
		t2.parent = z
		

	"""rotates nodes to maintain AVL balance
	@type self: AVLTree
	@type node: AVLNode
	@rtype: int
	@returns: the number of rotation operations due to performing a single roatation step
	"""
	def rotate(self, node):
		cnt = 0
		if self.check_balance_factor(node) == 2:
			if self.check_balance_factor(node.left) == -1:
				self.rotate_left(node.left)
				cnt+=1
			self.rotate_right(node)
			cnt+=1
		elif self.check_balance_factor(node) == -2:
			if self.check_balance_factor(node.right) == 1:
				self.rotate_right(node.right)
				cnt+=1
			self.rotate_left(node)
			cnt+=1
		return cnt


	"""updates the balance status of a node and the number of balanced nodes in a tree
	@type self: AVLTree
	@type node: AVLNode
	@rtype: None
	@returns: None
	"""
	def update_bal(self, node):
		if node.bal_status and self.check_balance_factor(node) != 0:
			node.bal_status = False
			self.bal_cnt -= 1
		elif not node.bal_status and self.check_balance_factor(node) == 0:
			node.bal_status = True
			self.bal_cnt += 1
	
	
	"""rebalances the tree after an insertion or deletion
	@type self: AVLTree
	@type node: AVLNode
	@rtype: int
	@returns: the number of rebalancing operations due to AVL rebalancing
	"""
	def rebalanceAVL(self, node, op):
		cnt = 0
		while node is not None and node.is_real_node():
			new_height = 1 + max(node.left.height, node.right.height)
			if (abs(self.check_balance_factor(node)) < 2):
				if (node.height == new_height):
					self.update_bal(node)
					return cnt
				else:
					node.height = new_height
					self.update_bal(node)
					cnt += 1
			else: #|bf(node)| = 2
				if op == "ins":
					cnt += self.rotate(node)
					return cnt
				else:  # op == "del"
					cnt += self.rotate(node)
					node = node.parent
			if node.parent is not None and node.parent.is_real_node():
				node = node.parent
		return cnt


	"""inserts a new node into the dictionary with corresponding key and value from a given node
	@type self: AVLTree
	@type node: AVLNode
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operations due to AVL rebalancing
	"""
	def insert_at_node(self, key, val, node):
		while node.is_real_node():
			if key < node.key:
				if not node.left.is_real_node():
					node.left = AVLNode(key, val)
					node.left.left = AVLNode(None, None)
					node.left.right = AVLNode(None, None)
					node.left.height = 0
					node.left.parent = node
					node = node.left
					break
				else:
					node = node.left
			else:
				if not node.right.is_real_node():
					node.right = AVLNode(key, val)
					node.right.left = AVLNode(None, None)
					node.right.right = AVLNode(None, None)
					node.right.height = 0
					node.right.parent = node
					node = node.right
					break
				else:
					node = node.right
		self.bal_cnt += 1
		if key>self.max.key:
			self.max = node
		cnt = self.rebalanceAVL(node.parent, "ins")
		return cnt
	

	"""inserts a new node into the dictionary with corresponding key and value from the root
	@type self: AVLTree
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operations due to AVL rebalancing
	"""
	def insert_at_root(self, key, val):
		if self.root is None:
			self.root = AVLNode(key, val)
			self.root.right = AVLNode(None, None)
			self.root.left = AVLNode(None, None)
			self.root.height = 0
			self.max= self.root
			self.bal_cnt = 1
			return 0
		else:
			r = self.root
			cnt = self.insert_at_node(key, val, r)
		return cnt


	"""inserts a new node into the dictionary with corresponding key and value from the maximum node
	@type self: AVLTree
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: int
	@returns: the number of rebalancing operations due to AVL rebalancing
	"""

	def insert_at_max(self, key, val):
		if self.root is None:
			self.root = AVLNode(key, val)
			self.root.right = AVLNode(None, None)
			self.root.left = AVLNode(None, None)
			self.root.height = 0
			self.max= self.root
			self.bal_cnt = 1
			return 0
		else:
			node = self.max
			while node is not self.root and key < node.key:
				node = node.parent
			cnt = self.insert_at_node(key, val, node)
		return cnt


	"""inserts a new node into the dictionary with corresponding key and value
	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
    @param start: can be either "root" or "max"
	@rtype: int
	@returns: the number of rebalancing operations due to AVL rebalancing
	"""
	def insert(self, key, val, start="root"):
		if start == "root":
			cnt = self.insert_at_root(key, val)
		elif start == "max":
			cnt = self.insert_at_max(key, val)
		else:
			raise ValueError("start must be either 'root' or 'max'")
		self.Tsize += 1
		return cnt

	"""find a succesor of a node in the dictionary
	@type node: AVLNode
	@pre: node is a real pointer to a real node in an AVL tree with two children - hence the succesor is not an Ancestor
	@rtype: AVLNode
	@returns: a pointer to the succesor of the given node
	"""
	def succesor(self, node):
		node = node.right
		while node.is_real_node() and node.left.is_real_node():
			node = node.left
		return node


	"""deletes node from the dictionary
	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""
	def delete(self, node):
		cnt = 0
		#checking if the node being deleted is the max node and update accordingly
		if node.key == self.max.key:
			self.max = node.parent
		#deleting a leaf
		if (not node.left.is_real_node()) and (not node.right.is_real_node()):
			if node.parent is None:
				self.root = None
				self.bal_cnt = 0
			else:
				if node.parent.left is node:
					node.parent.left = node.left
					node.left.parent = node.parent
					node.right.parent = None
					node.right = None
				else:
					node.parent.right = node.right
					node.right.parent = node.parent
					node.left.parent = None
					node.left = None
				p = node.parent
				node.parent = None
				self.bal_cnt -= 1
				cnt = self.rebalanceAVL(p, "del")
		#deleting a node with two children
		elif node.left.is_real_node() and node.right.is_real_node():
			suc = self.succesor(node)
			node.key = suc.key
			node.value = suc.value
			suc.key, suc.value = None, None
			p = suc.parent
			cr = suc.right
			suc.parent, suc.right = None, None
			cr.parent = p
			if p != self.root:
				p.left = cr
			self.bal_cnt -= 1 if suc.bal_status else 0 
			cnt = self.rebalanceAVL(p, "del")
		#deleting a node with one child
		else:
			if node.left.is_real_node():
				if node.parent is None:
					node.left.parent = None
					self.root = node.left
					node.left = None
				else:
					if node.parent.left is node:
						node.parent.left = node.left
					else:
						node.parent.right = node.left
					node.left = None
			else:
				if node.parent is None:
					node.right.parent = None
					self.root = node.right
					node.right = None
				else:
					if node.parent.left is node:
						node.parent.left = node.right
					else:
						node.parent.right = node.right
					node.right = None
			p = node.parent
			node.parent = None
			cnt = self.rebalanceAVL(p, "del")
		self.Tsize -= 1
		return cnt


	"""returns an array representing dictionary 
	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		def in_order(node, result):
			if node is None or not node.is_real_node():
				return
			in_order(node.left, result)
			result.append((node.key, node.value))
			in_order(node.right, result)

		result = []
		in_order(self.get_root(), result)
		return result


	"""returns the number of items in dictionary 
	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.Tsize


	"""returns the root of the tree representing the dictionary
	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root


	####################
	# ASSISTING METHOD #
	####################

	"""calculates the balance factor of a node
	@type node: AVLNode
	@param node: a node in the tree
	@rtype: boolean
	@returns: True if the balance factor of node is 0, False otherwise
	"""
	def check_balance_factor(self, node):
		return node.left.height - node.right.height


	"""gets amir's suggestion of balance factor
	@returns: the number of nodes which have balance factor equals to 0 devided by the total number of nodes
	"""
	def get_amir_balance_factor(self):
		if self.size() == 0:
			return 0
		return self.bal_cnt/self.size()