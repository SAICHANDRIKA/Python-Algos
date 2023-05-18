#! /usr/bin/env python
import random
from time import process_time_ns
from matplotlib import pyplot as plt
# How to represent a binary tree?

# datatype def'n:
#  A BSTree is either:
#    - False,                              (interpretation: empty tree)
#    - ( [number], [BSTree], [BSTree] )    (interpretation: number at root, and left-, right- subtrees)
#                                           we'll call this non-empty tree a "Branch".

myData = [57, 
          [18,
           [2,False,False],
            [35, 
            [20,False,False], 
            [40,False,False]]],
          [78,
           False,
           False]]

#myData[0] -- value at root
#myData[1] -- left  child
#myData[2] -- right child



# wrappers, so we can act like these tuples have named-fields
def val(  aBSTree): return aBSTree[0]
def left( aBSTree): return aBSTree[1]
def right(aBSTree): return aBSTree[2]



# constructor, predicate:
def isEmpty( aBSTree): return aBSTree==mt
def newBranch( val, l, r ): return [val,l,r]

mt = False    # convenient variable/name for the empty-tree



t1 = newBranch(29,       
               newBranch(2,mt,mt),
               newBranch(35,     
                         newBranch(30,mt,mt),
                         newBranch(44,mt,mt)))            

assert val(t1) == 29
assert left(t1) == [2,mt,mt]
assert val(left(right(t1))) == 30 



# Template, for *any* function processing a BSTree:
#
# anyTreeFunc : BSTree -> ???
#
# def anyTreeFunc( t ):
#   return answer_for_base_case  if isEmpty(t) else \
#          somehowCombine( val(t), anyTreeFunc(left(t)), anyTreeFunc(right(t)) )


def size( t ):
  """size : BSTree -> natnum
  Return the # of Branches in `t` (that is, non-Empty subtrees it contains)
  """
  return 0 if isEmpty(t) else \
         1 + size(left(t)) + size(right(t))

assert size(mt) == 0
assert size([50,mt,mt]) == 1
assert size(t1) == 5


def height( t ):
  """ height : BSTree -> natnum
  Return the length of longest path from root to some (Empty) leaf
  """
  return 0 if isEmpty(t) else \
         1 + max( height(left(t)), height(right(t)))

assert height(mt) == 0
assert height([50,mt,mt]) == 1
assert height(t1) == 3


def contains_v1( t, target ):
  """contains_v1 : BSTree, number -> boolean
  Does `target` contain `t`?  
  v1 is for *any* binary tree; it does *not* use the binary-search-tree property (and it searches the entire tree).
  """
  return False if isEmpty(t) \
    else target==val(t)  \
         or contains_v1(left(t),target)  \
         or contains_v1(right(t),target)

assert contains_v1(mt, 50)         == False
assert contains_v1([50,mt,mt], 50) == True
assert contains_v1([50,mt,mt], 37) == False
assert contains_v1(t1,29) == True
assert contains_v1(t1, 2) == True
assert contains_v1(t1,35) == True
assert contains_v1(t1,30) == True
assert contains_v1(t1,44) == True
assert contains_v1(t1,31) == False


# What is the Running-time of each of the above
# functions, `size`  `height`   `contains_v1` ?



#######################

# The Binary **Search** Tree ("BST") Property:
#   - holds for `mt`
#   - For a non-empty tree t, holds if
#     val(left(t))  <=  val(t)  <= val(right(t))    (assuming those exist)
#     and left(t),right(t) also have the BST Property.



# contains : BSTree, number -> boolean
#
def contains( t, target ):
  """contains : BSTree, number -> boolean
  Does `target` contain `t`?  
  (Runs in time O(height(t));  `t` must be a Binary Search Tree.)
  """
  return False if isEmpty(t) else \
         val(t)==target \
         or (val(t) < target and contains(right(t), target))  \
         or (val(t) > target and contains(left(t),  target))

assert contains(mt, 50)         == False
assert contains([50,mt,mt], 50) == True
assert contains([50,mt,mt], 37) == False
assert contains(t1,29) == True
assert contains(t1, 2) == True
assert contains(t1,35) == True
assert contains(t1,30) == True
assert contains(t1,44) == True
assert contains(t1,31) == False


#
def smallest(t):
    """ smallest : BSTree -> num-or-None
    Return the smallest item in `t` (or None, if `t` is empty).
    """
    return None if isEmpty(t) else \
           smallest(left(t)) or val(t)  # abuse how `None or 3` evals to `3`
    

# Or, here's a different, sneaky technique:
# Walk down the right-hand-branch, keeping track of the previously-seen item.

def biggest(t):
    """ biggest : BSTree -> num-or-None
    Return the biggest item in `t` (or None, if `t` is empty).
    """
    return biggestOr(t,None)

def biggestOr(t,biggestSeenSoFar):
    """ biggest : BSTree, num -> num-or-None
    Return the biggest item in `t` (or `bigestSeenSoFar`, if `t` is empty).
    """
    return biggestSeenSoFar if isEmpty(t) else \
           biggestOr(right(t),val(t))


assert biggest( [7,mt,mt] ) == 7
#print( biggest( t1 ) )
assert biggest( t1 ) == 44
assert smallest( [7,mt,mt] ) == 7
assert smallest( t1 ) == 2



def insert_v1( t, n ):
  """insert : BSTree, num -> BSTree
  Return a new BSTree like `t` except with `n` inserted (at a leaf).
  The result may not be balanced.
  """
  if isEmpty(t):
    return newBranch(n,mt,mt)
  else:
    if val(t) < n:
      return newBranch(val(t),left(t),insert_v1(right(t),n))
    else:
      return newBranch(val(t),insert_v1(left(t),n),right(t))


assert insert_v1( mt, 77 ) == [77,mt,mt]
assert insert_v1( [50,mt,mt], 77 ) == [50,mt,[77,mt,mt]]
assert insert_v1( [50,mt,mt], 22 ) == [50,
                                       [22,mt,mt],
                                       mt]
assert insert_v1(t1,32) == [29,       
                             [2,mt,mt],
                             [35,     
                              [30,
                                mt,
                                [32,mt,mt]],
                              [44,mt,mt]]]   


assert t1 == [29,       
              [2,mt,mt],
              [35,     
               [30,mt,mt],
               [44,mt,mt]]]  


# Btw: we can use `and`,`or` if we *really* wanted to keep using
# the 'if-else' expression rather than the 'if-else' statement:
#
#def insert( t, n ):
#  return newBranch(n,mt,mt) if isEmpty(t) else \
#         ((val(t) < n) and newBranch(val(t),left(t),insert(right(t),n))) \
#         or newBranch(val(t),insert(left(t),n),right(t)) 




# To delete from a BSTRee:
#   - deleting a leaf easy -- just return empty tree
#   - deleting the root: "replace" it with the smallest(right)),
#      OR biggest(left(t))

#    pre-condition: t != mt
#
def delete_v1( t, n ):
  """delete : BSTree, num -> BSTree
  Return a BSTree like `t` except with `n` deleted.
  Throws an exception if `n` doesn't occur.
  """
  if isEmpty(t):
    raise f"{n} not contained in the initial tree"
  else:
    if n < val(t):
      return newBranch(val(t), delete_v1(left(t),n), right(t))
    elif n > val(t):
      return newBranch(val(t), left(t), delete_v1(right(t),n))
    else: # n==val(t) -- delete the root
      if not(isEmpty(right(t))):
         replacement = smallest(right(t))
         return newBranch(replacement, left(t), delete_v1(right(t),replacement))
      elif not(isEmpty(left(t))):
         replacement = biggest(left(t))
         return newBranch(replacement, delete_v1(left(t),replacement), right(t))
         # Alternately, since we know isEmpty(right), we could just return left(t)
      else: # deleting root, whose children are both empty:
        return mt
        

# run-time of contains, insert, and delete, in a BSTree:
#     for a tree of height h, it takes O(h) steps.
#
#  IF the tree is (relatively) balanced, then height is log(n) -- yay!
#
# BUT: how to keep tree balanced???

###############
# "AVL Trees" -- self-balancing, after inserts and deletes.
#
#
#  We call a tree t "AVL Balanced" if:
#    | height[left) - height[right) | <= 1,
#  and both left and right are themselves AVL balanced.
#
# We will show how to insert/delete into a balanced, so that they *stay* balanced.
#
# - We'll do it by using tree rotations:
#   

t23 = [60,mt,mt]
t4  = [99,mt,mt]

def rotateCCW( t ):
    """ rotateCCW : BSTree -> BSTree
    Do a counter-clockwise rotation on a BSTree,
    maintaining the binary-search-tree invariant (ordering).
    Pre-condition: t and right(t) are both non-empty BSTrees.
    """
    # see diagram https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/AVL-simple-left_K.svg/388px-AVL-simple-left_K.svg.png
    X   = val(t)
    t1  = left(t)
    Z   = val(right(t))
    t23 = left(right(t))
    t4  = right(right(t))
    return [Z, [X,t1,t23], t4]

assert rotateCCW(  [50,mt,[75,mt,mt]])  == [75,[50,mt,mt],mt]
assert rotateCCW(  [50,t1,[75,t23,t4]] ) == [75, [50,t1,t23], t4]

def rotateCW( t ):
    """ rotateCW : BSTree -> BSTree
    Do a clockwise rotation on a BSTree,
    maintaining the binary-search-tree invariant (ordering).
    Pre-condition: t and left(t) are both non-empty BSTrees.
    """
    # see diagram https://upload.wikimedia.org/wikipedia/commons/thumb/7/76/AVL-simple-left_K.svg/388px-AVL-simple-left_K.svg.png
    X   = val(t)
    t1  = right(t)
    Z   = val(left(t))
    t23 = right(left(t))
    t4  = left(left(t))
    return [Z,t4,[X,t23,t1]]

assert rotateCW(  [50,[75,mt,mt],mt] )  == [75,mt,[50,mt,mt]]
assert rotateCW(  [50,[75,t23,t4],t1])  == [75,t23,[50,t4,t1]]

# AVL observation:
# when you do an insert or delete, the 
# balance gets messed up by at most 1, so the unbalance is at most 2.
# - if the left side is shorter than the outside-right (by two),
#   then a single rotateCCW fixes.
# - if the left side is shorter than the inside-right (by two),
#   then first rotateCW the right-child, then do a rotateCCW at root.
# - other two mirror-images similarly.
#
def balance(t):
   """balance: BSTree -> BStree
   precondition:  abs(height(left(t)) - height(right(t))) <= 2
                  and there is only one *leaf* causing this excess.
   postcondition: for the returned tree `r`,
                  abs(height(left(r)) - height(right(r))) <= 1
                  and it still has binary-search-tree property.
   """
   if t==mt: return t
   elif abs(height(left(t)) - height(right(t))) <= 1 : return t
   else:
       hl = height(left(t))
       hr = height(right(t))
       if (hl == hr - 2): # left side short
          if hl == height(right(right(t))) - 1: 
             # the unbalance is on outside
             return rotateCCW(t)
          else:
             # the unbalance is on inside; 2 rotations needed:
             return rotateCCW([val(t),left(t),rotateCW(right(t))] )
       else:             # right side short
          # TODO: add mirror-image of above if-else
          if (hr == hl - 2): # right side short
            if hr == height(left(left(t))) - 1: 
             # the unbalance is on outside
             return rotateCW(t)
            else:
             # the unbalance is on inside; 2 rotations needed:
             return rotateCW( [val(t),rotateCCW(left(t)),right(t)] )


#right of tree unbalanced on inside
assert balance([50,[30,mt,mt],[75,[60,[55,mt,mt],[73,mt,mt]],[80,mt,mt]]]  ) == [60, [50, [30, False, False], [55, False, False]], [75, [73, False, False], [80, False, False]]]

#left of tree unbalanced on inside
assert balance([50,[30,[20,mt,mt],[40,[35,mt,mt],[45,mt,mt]]],[75,mt,mt]] ) == [40, [30, [20, False, False], [35, False, False]], [50, [45, False, False], [75, False, False]]]


          
def insert_v2( t, n ):
  """Balanced insert : BSTree, num -> BSTree
  Returns same BSTree `t` except with `n` inserted (at a leaf).
  The result is balanced.
  """
  if isEmpty(t):
    return newBranch(n,mt,mt)
  else:
    if val(t) < n:
      t[2] = insert_v2(right(t),n)
      return balance([val(t),left(t),right(t)])
    else:
      t[1] = insert_v2(left(t),n) 
      return balance([val(t),left(t),right(t)])

assert insert_v2( mt, 77 ) == [77,mt,mt]
assert insert_v2( [50,[40,mt,mt],mt], 77 ) == [50,[40,mt,mt],[77,mt,mt]]
assert insert_v2( [50,mt,mt], 22 ) == [50,
                                       [22,mt,mt],
                                       mt]
assert insert_v2( [50,[20,mt,mt],mt], 22 ) == [22,
                                       [20,mt,mt],
                                       [50,mt,mt]]                                     

def delete_v2( t, n ):
  """Balanced delete : BSTree, num -> BSTree
  Returns same BSTree `t` except with `n` deleted.
  Throws an exception if `n` doesn't occur.
  """
  if isEmpty(t):
    raise f"{n} not contained in the initial tree"
  else:
    if n < val(t):
      return balance([val(t), delete_v2(left(t),n), right(t)])
    elif n > val(t):
      return balance([val(t), left(t), delete_v2(right(t),n)])
    else: # n==val(t) -- delete the root
      if not(isEmpty(right(t))):
         replacement = smallest(right(t))
         return balance([replacement, left(t), delete_v2(right(t),replacement)])
      elif not(isEmpty(left(t))):
         replacement = biggest(left(t))
         return balance([replacement, delete_v2(left(t),replacement), right(t)])
         # Alternately, since we know isEmpty(right), we could just return left(t)
      else: # deleting root, whose children are both empty:
        return mt

assert delete_v2( [50,mt,mt],50 ) ==  mt
assert delete_v2( [50,[20,mt,mt],mt], 20 ) == [50,mt,mt]     
assert delete_v2([50,[30,mt,mt],[75,[60,[55,mt,mt],[73,mt,mt]],[80,mt,mt]]] , 55 ) == [60, [50, [30, False, False], False], [75, [73, False, False], [80, False, False]]]

 
#   (0) measure performance: 
#   Do (say) 1,000 inserts;  then 2,000;  then 4,000;  ... and time/graph them.
#   (Are they as expected, theoretically?  If not, offer hypotheses.  [Then, test the hypotheses??])
#   hypotheses : update our 3-tuple to keep one more field: the (cached) height,
#   to avoid O(n) time for each call to `height`.


import math  
# num_inserts=[1000,2000,4000,8000]
num_inserts=[2,4,8,16,32,64,128,256]  
def measure_BStreePerformance(num_inserts):
    insert_time =[]
    for j in num_inserts:
        mutableBStree = mt
        random_list = []
        # generating random numbers using random.randint
        for i in range(j):
            random_list.append(random.randint(0,1000))
        print("Length of random list",len(random_list))
        t1_start = process_time_ns()
        for k in random_list:
            mutableBStree = insert_v2(mutableBStree,k)
        t1_stop = process_time_ns()
        insert_time.append(t1_stop-t1_start)
    return insert_time

insertTimeList = measure_BStreePerformance(num_inserts)
print(insertTimeList)

 
import matplotlib
from matplotlib import pylab as plt
from matplotlib import gridspec as gridspec


matplotlib.rcParams['figure.figsize'] = (8,5)
gs = gridspec.GridSpec(2, 2)
# plt.grid(zorder=0)
plt.plot(num_inserts,insertTimeList,color='blue', marker = ".", linewidth=1, scalex=True,scaley=True, zorder=3)
plt.xlabel('Number of inserts', fontsize=10)
plt.ylabel('Time taken for number of inserts(nanoseconds)', fontsize=10)
plt.title('Performance Measure of RealMutableBSTree', loc='Center', fontsize=14)
plt.show()

# Testing outputs 
# HeightCachedBSTree(immutable) [2,4,8,16,32,64,128,256] inserts output [4000, 7000, 21000, 51000, 119000, 286000, 742000, 1423000]
# HeightCachedMutableBSTree [2,4,8,16,32,64,128,256] inserts output [5000, 8000, 22000, 50000, 119000, 327000, 702000, 1395000]
# RealMutableBSTree [2,4,8,16,32,64,128,256] inserts output [6000, 8000, 42000, 139000, 453000, 5458000, 22518000, 72625000]



