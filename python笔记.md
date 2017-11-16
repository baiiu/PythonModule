## 如何学好编程
- 基础部分
  - 基本语法
    - 关键字
    - 运算符
    - 基本语法
      - 变量和类型
      - 常见字符串处理
      - 条件判断
      - 循环控制
      - 函数
  - 数据结构
    - 数组
    - 字符串
    - 系统标准库自带的类型
    - 如何实现常用数据结构：链表、堆栈、二叉树等
  - 输入输出
    - 标准输入输出
    - 文件读写：文本(行读写)、二进制(偏移量+大小)
    - 格式化字符串
  - 异常处理
    - 抛出和捕获异常：try/catch，try/except
    - 异常和错误的区别以及应用场合

- 进阶提高
  - 常用算法
    - 分治
    - 贪心
    - 动态规划
  - 数据库访问
    - 建立连接
    - 执行SQL查询
    - 读取查询记录
  - 面向对象
    - 继承
    - 多态
    - 静态变量与方法
  - 其他
    - 多线程、进程(Windows高级编程里一章)
    - 匿名函数
    - 语言相关特定知识
      - Java的反射
      - C++的模板
      - Python的协程
      - 等

---

## 常用关键字
- 常量
  - True
  - False
  - None
- 对象和容器
  - class
  - import
  - from
  - del
- 判断
  - if
  - elif
  - else
  - is
  - in
  - assert
- 循环
  - for
  - while
  - continue
  - break
  - pass，什么都不做
- 异常
  - raise
  - try
  - except
  - finally
  - as

## 常用运算符
- 算数运算
  - + - * /
  - %
  - ** 指数运算
  - // 只保留整数，小数部分扔掉
- 比较运算
  - > , >=
  - < , <=
  - ==
  - !=
- 逻辑运算
  - and
  - or
  - not
- 位运算
  - >>
  - <<
  - & 与
  - | 或
  - ^ 异或，不等取1，相等取0

## 基本语法
- 缩进
- 注释
  - 单行注释 `#`
  - 多行注释 三个单引号
- 多行代码表示
  - 多行字符串,三个双引号
- 中文支持


## python2和3的区别
- print函数：3.x 必须加()
- Unicode：3.x默认使用unicode编码
- 除法运算：3.x整数相除也能得到浮点数结果
- 异常：3.x只能抛出继承自BaseException的异常
- xrange：3.x取消了xrange，range与xrange一样为实现为惰性求职
- 二/八进制：3.x必须强制写成0b1011和0o7236
- 不等式：3.x取消了`<>`，只有`!=`
- ""表达式：3.x必须使用`repr`函数
- 多个模块名称的改变
- 数据类型
  - 3.x取消了long，统一为int
  - 新增bytes类型，并可与string相互转化
  - dict的`keys`、`items`、`values`方法返回迭代器，`iterkeys`函数被废弃，`has_key`被`in`取代



---

## 类型
所有对象都是一个类，类本身也是一个类

- 整数 <class 'int'>
- 浮点数 <class 'float'>
- 字符串 <class 'str'>

- 布尔值
- 空值

- list 列表 <class 'list'>
- tuple 元组 <class 'tuple'>
- set <class 'set'>
- dict 字典 <class 'dict'>

- 函数类型 <class 'function'>，是一个函数类型的对象
- 模块 <class 'module'>
- 类 <class 'type'> 元编程，用于描述类的类
- 自定义类型

```
print(type(1))
print(type(1.))
print(type('abc'))

# 函数类型
def function(a,b,c):
  print(a + b + c)

print(type(function))

# 模块类型
import string
print(type(string))

# 类
class MyClass(object):
  pass
print(type(MyClass)) # <class 'type'>

my_class = MyClass()
print(type(my_class)) # <class '__main__.MyClass'>
```

## 变量
- 变量定义：
  - 变量是存储在内存中的值。即会在创建变量时在内存中申请一个空间。
  自带垃圾回收的语言中，所有的变量都是分配在堆上的。
  - 基于变量的数据类型，解释器会分配指定内存，并决定什么数据可以被存储在内存中。
  - python是弱类型语言，变量可以指定不同的数据类型。

- 变量赋值：
  - 每个变量在使用前必须赋值，变量赋值以后该变量才会被创建
  - `=`用于赋值

## 常见字符串处理
字符串本身不能被修改，返回一个新的字符串

- 去除空格及特殊符号:
`strip`、
`lstrip`删除左空格、
`rstrip`删除右空格

- 复制字符串 str1 = str2

- 连接字符串 str2 += str1

- 查找字符串
pos = str1.index(str2)，如果不存在会抛出异常

- 比较字符串
`cmp(str1,str2)`被移除，直接使用 > 、 < 、 == 来比较

- 字符串长度 len(str)
len(NONE),会抛出异常

- 大小写转换 str.upper()、 str.lower()
- 首字母大写 str.capitalize()、str.capword(str)

- 分割与合并字符串,分割返回的是list类型
`split`、
`splitlines`换行分割，等价于 split('\n')
`join`

- 字符串判断
str.startswith('adc')
str.endswith(‘abc’)
str.isalnum()，是否由字母和数字组成
str.isalpha(),是否全是字母
str.isdigit()，是否全是数据
str.isspace()，是否全是空格
str.islower()，是否全是小写
str.isupper()，是否全是大写
str.isTitle()，首字母是否大写，且其他为小写

- 类型转换
数字到字符串：
str(5)
str(5.) --> '5.0'
str(-5.123)

字符串到数字：
int('1234')
float('123.45')
int('123.45') 抛出异常
int(int（'110011',2)) 二进制转换
int('ffff',16) 十六进制转换

字符串到List：list(s)


```
import string

s = ['abc','def','ghi']
print(''.join(s)) # abcdefghi
print(',,,'.join(s)) # abc,,,def,,,ghi


s = 'abcd'
print(list(s)) # ['a','b','c','d']

```


## 条件判断 if语句
```
a = 100
b = 200
c = 300

if a > b:
  print(b)
elif a > c:
  print(c)
else:
  print(a)

# None的判断
x = None
if not x: #等价于 if x is not None
  print('None')
else:
  print('not None')

```

## 循环语句
```
# for循环
for i in 迭代器:
  print(i)

```

```
# while循环
sum = 0
i = 1

while i <= 100:
  sum += i
  i += 1

print(sum)
```

```
# pass、continue、break关键字

for i in range(0,100):
  if i < 10:
    pass
  elif i < 30:
    continue
  elif i < 35:
    print(i)
  else:
    break
```

## 函数
参数定义的顺序必须是：必选参数、默认参数、可变参数和关键字参数。

```
# 函数的定义
def func_name(arg_1,arg_2):
  print(arg_1,arg_2)
  return arg_1,arg_2 #返回的tuple，只读的元组

r = func_name(1,2)
print(type(r))
print(r[0],r[1])


# 默认参数，并且可以指定参数传值，不需要遵照参数声明顺序
def func(x , y = 500):
  return x + y

print(func(1,2)) # 3
print(func(1)) # 501

print(func(y = 2, x = 3)) # 5
print(func(x = 3)) # 503


# 可变参数
def func_variable(name, *numbers):
  print(type(numbers))
  print(numbers)

func_variable("哈哈",1,2,'3',True)

## 关键字参数
def func_dict(name, **args):
  print(type(args))
  print(args)

func_dict("哈哈",china='BeiJing',uk='London')

## 命名关键字参数,*号后面的变量传参时一定要带上参数名，否则抛出异常
def func_name(a, b, c, *, d, e):
  print(d,e)

func_name(1, 2, 3, d = 4,e = 5)


# 函数可以作为参数
def cmp(x, y, cp = None):
  if not cp:
    if x > y:
      return 1
    elif x < y:
      return -1
    else
      return 0
  else:
    return cp(x,y)

def my_cp(x, y):
  if x > y:
    return -1
  elif x < y:
    return 1
  else:
    return 0

print(cmp(1, 2))
print(cmp(1, 2, my_cp))

```




## TODO:
汉诺塔的问题
















---
