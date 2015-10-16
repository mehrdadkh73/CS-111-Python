# Xiaofan Wu and Jingyao Liu
# CS111 Problem Set 4
# More List Functions

# 2a: partition
def partition(pivot, elts):
    list1=[]
    list2=[]
    for s in elts:
    # add words to different lists depending on how they compare to pivot
        if s<=pivot:
            list1.append(s)
        else:
            list2.append(s)
    return list1, list2

def testPartition(pivot, elts):
    print('partition(' + str(pivot) + ', ' + str(elts) + ') -> ' 
    + str(partition(pivot,elts)))

testPartition(7,[8, 12, 5, 6, 9, 4, 10])
testPartition(6,[8, 12, 5, 6, 9, 4, 10])
testPartition(9,[8, 12, 5, 6, 9, 4, 10])
testPartition(12,[8, 12, 5, 6, 9, 4, 10])
testPartition(1,[8, 12, 5, 6, 9, 4, 10])
testPartition('gettysburg',['four', 'score', 'and', 'seven', 'years', 'ago'])
    
# 2b: product
def product(list1, list2):
    result = []
    # use double for loops to make and add all the pairs in order
    for n in range(len(list1)):
        for s in list2:
            result.append((list1[n], s))
    return result
    
def testProduct(list1, list2):
    print('product(' + str(list1) + ', ' + str(list2) + ') -> ' 
    + str(product(list1, list2)))
     
testProduct([1, 2, 3, 4],['a', 'b', 'c'])
testProduct(['a', 'b', 'c'],[1, 2, 3, 4])
testProduct([2,4,3,1], ['c', 'a', 'b'])