
## list列表
```
li = [1, 2, 3, '456', [1, 2, 3],{1 : 'one', 2 : 'two'}]
print(type(list)) # <class 'type'>
print(type(li)) # <class 'list'>

# 访问元素，通过索引
li[0]
li[-1] #倒数第一个元素, li[len(li) - 1]

# 查找元素位置
print(li.index('456'))
print(li.index([1,2,3]))
print(li.index(-1)) #不存在的话会抛出异常

# 添加元素
li.append(4)

l_a = [7, 8, 9]
li.extend(l_a) #遍历l_a，把里面的元素一个一个添加进去
li.append(l_a) #把l_a当做一个元素添加进去

# 删除元素，根据索引删除
del(li[-1]) # 删除最后一个元素
li.pop() #删除最后一个元素
li.pop(0) # 删除指定索引的元素

# 判断是否为空
l_a = []
if not l_a:
  print('empty')

if len(l_a) == 0:
  print('empty')

l_a = None
#下面这个打印不出empty，毕竟分配了内存等,not xx 和 is None不是一回事
if l_a is None:
  print('empty')


# 遍历元素
for i in li:
  print(i)

for i in range(len(li)):
  print(li[i])

```


## tuple元组
只读，不可修改
```
t = (1, 2, 3)
print(type(tuple)) # <class 'type'>
print(type(t)) # <class 'tuple'>

```

## 字典dict
```
d = {
  'a' : 1,
  'b' : 2,
   1 : 'one',
   2 : 'two'
   3 : [1, 2, 3]
}

# 访问元素，通过key,key不存在会抛出异常
print(d['a'])
print(d[1])
d.get('c') #返回None
d.get('c', -1) # 返回-1

# 判断key是否存在
print('c' in d)
print(3 in d)

# 删除元素
del(d[3])
print(len(d))
d.pop('a') # key不存在会抛出异常

# 添加元素
d[]

# 字典遍历
for key in d:
  print(d[key])

for key,value id d.items():
  print(key, value)

keys = d.keys()
print(type(keys))
print(keys)
for key in keys:
  print(d[key])



```

## set
里面的元素没有重复的
```
s_a = set([1,2,2,3,5,6,9,0,9])
s_b = set([1,'a','c',0,0])

# 判断元素是否存在
print(2 in s)
print(len(s_a))

# 并集
print(s_a | s_b)
print(s_a.union(s_b))

# 交集
print(s_a & s_b)
print(s_a.intersection(s_b))

# 差集 A - A & B
print(s_a - s_b)
print(s_a.difference(s_b))

# 对称差 (A + B) - (A & B)
print(s_a ^ a_b)
print(s_a.symmetric_difference(s_b))

# 修改元素，不能添加不能hashable的元素
s_a.add('x')
s_a.update([4,5]) # 添加一个数组，会挨个添加进去，
s_a.remove(2) # 删除一个元素，不存在该元素时会抛出异常

# 遍历
for i in set:
  print(i)


```

# 切片
语法：[start:end:steps]，产生一个新的对象
>= start & < end 左开右闭

```
li = list(range(10))
print(li)
print(li[2:5]) #[2,3,4]
print(li[:4]) # [0,1,2,3]
print(li[5:]) # [5,6,7,8,9]
print(li[0:10:3]) # [0,3,6,9]
print(li[0:15:3]) # [0,3,6,9] #越界不会抛异常


```


# 列表推导
```
li = [0] * 10 # 生成10个0的数组

li = [i * 2 for i in range(10)] # 生成前10个偶数

# li = [[0] * 3] * 3，浅拷贝，同一个对象引用三次
li_2d = [[0] * 3 for i in range(3)] # 二维数组

# 集合和字典也支持列表推导
s = {x for x in range(10) if x % 2 == 0} #10以内的偶数

d = {x : x % 2 == 0 for x in range(10)} # {0:True, 1:False, ...}


```

# 生成器
把真正的计算推迟到使用时

```
# 例子1：平方表，range是一个生成器

square_table = (x * x for x in range(50000)) # 用()
print(type(square_table)) # <class 'generator'>
for i in range(10):
  print(next(square_table))

```

```
def fib(limit):
  n,a,b =  0,0,1
  while(n < limit):
    yield b
    a,b = b, a + b
    n += 1
  return 'done'

f = fib(5)
print(type(f)) # <class 'generator'>
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
# print(next(f)) 抛出错误,从yield开始执行

for i in fib(5):
  print(i)


```

# 迭代器
可以直接作用于for循环的对象称为可迭代对象，Iterable
可以被next()函数调用并不断返回下一个值的对象成为迭代器:Iterator

```
from collections import Iterable
from collections import Iterator

print(isinstance([],Iterable)) # True
print(isinstance({},Iterable)) # True
print(isinstance("",Iterable)) # True

print(isinstance([],Iterator)) # False
print(isinstance({},Iterator)) # False
print(isinstance("",Iterator)) # False

```



























---
