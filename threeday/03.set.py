# set集合

# 集合的定义
setA = {1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4}
listA = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4]
print(setA)
print(listA)

# 对列表中重复元素去重的操作
new_listA = set(listA)
print(new_listA)

# 集合的基本操作
setA = {1, 2, 3, 4, 5}
setB = {3, 4, 5, 6, 7}

# 交集和并集
setC = setA & setB   # 两个集合之间交集
print(setC)

setD = setA | setB   # 两个集合之间并集
print(setD)

# 集合的顺序
