1. 类和实例
2. 访问限制
3. 继承和多态以及多重继承
4. 获取对象信息
5. 实例属性和类属性
6. 模块和包

Class类用驼峰表示，方法名、变量名用_隔开

# 创建类
```
class Student:
  __name = 'Foo' # 表示内部变量，__表示private，类属性

  def __init__(self,name):#构造函数
    self.__name = name

  def bar(self): # self是必带的参数，指代类自身
    print('bar')

  def hello(self,name):
    print('i am %s',%self.__name)
    print('i am %s',%name)

  //Getter和Setter
  def get_name(self):
    return self.__name
  def set_name(name):
    self.__name = name


obj = Foo('John')
obj.__name = 'Hi' #修改不了
obj.hello('Li')

obj.age = 20 # 实例属性，使用对象声明，不需要在类中声明
s.name = 's'
del s.name # 删除该属性


# 继承，python可以多继承
# 多继承时，从谁先开始
# - 深度优先,先纵向寻找
# - 广度优先，先平辈寻找
class PrimaryStudent(Student): # 继承语法
  pass

# 多态
# python不支持多态也用不到多态，多态用于强类型，
# python崇尚`鸭子类型`，Duck Typing，好猫类型。
# 在python中，只要是不报错运行的类型，都可以运行。

```

## 查看对象的属性和方法：
```
type('1') #<class 'str'>
type(1) #<class 'int'>
print(type('1') == type(1)) # False

print(isinstance([],list)) # True

# 查看对象的所有属性和
dir(list)

# 使用getattr()、setatrr()、hasattr()设置和访问属性
getattr(obj,'x')
getattr(obj,'x'，404) #添加默认值404，不存在时返回

setatrr('obj','x',19)
hasattr(obj,'x') # obj里有x这个属性么

```

# 模块和包
Python程序是由包(package)、模块(module)、函数组成。
包是一系列模块组成的集合，模块是处理某一类问题的函数和类集合。

包必须至少含有一个__init__.py文件，该文件内容可以为空。
__init__.py标识当前文件夹是一个包


## 文件读写

```
# 第一种方法
file = open('test.txt','w');# 可写
file.write('nn')
file.close()

# 第二种方法
for line in file:
  file.write(line[:s] + ',')
file.close()

# 第三种方法，使用with open，自带关闭功能
with open('test.txt','r') as f: #只读模式
  data = f.read()
  for line if f:
    print(line)  

# 二进制文件读写
f = open('a.jpg','rb') # 只读二进制文件

```

# 文件和目录操作

```
import os

print(os.name)
print(os.environ) #环境变量


ab_path = os.path.abspath('.') #当前目录的绝对路径

# 创建新目录
newDir = os.path.join(ab_path,'newDir') # 拼接新的路径
os.mkdir(newDir) # 创建该目录

os.rmdir(newDir) #删除该目录

# 拆分路径
os.path.split('/xx/xx/xx/1.jpg') #拆出来是路径名和文件名 '/xx/xx/xx'和'1.jpg'

os.path.splitext('/xx/xx/xx/1.jpg') #获取文件扩展名

os.rename('xx','newName') # 重命名
os.remove('1.jpg') # 删除文件

os.path.isdir('xx') #是否是目录

# 使用Shutil来复制文件
import shutil
shutil.copyfile('target','destination')

```
# 序列化和反序列化
```
import pickle

# 序列化，使用pickle是进行二进制的序列化和反序列化
l = [1,2,3,4,5]
str = pickle.dumps(l) #序列化成str
print(str)

f = open('dump.txt','wb')
pickle.dump(l,f) #序列化到文件
f.close()

# 反序列化
f = open('dump.txt','rb')
l = pickle.load(f)
f.close()
print(l)

# 用JSON实现
import json
str = json.dumps(l)
print(str)

l = json.loads(str)

```

# 函数式编程
函数是Python内建支持的一种封装，我们通过把大段代码拆成函数，通过一层一层的函数调用，就可以把复杂任务分解成简单的任务，这种分解可以称之为面向过程的程序设计。函数就是面向过程的程序设计的基本单元。

函数式编程就是一种抽象程度很高的编程范式，纯粹的函数式编程语言编写的函数没有变量，因此，任意一个函数，只要输入是确定的，输出就是确定的，这种纯函数我们称之为没有副作用。
而允许使用变量的程序设计语言，由于函数内部的变量状态不确定，同样的输入，可能得到不同的输出，因此，这种函数是有副作用的。

函数式编程的一个特点就是，允许把函数本身作为参数传入另一个函数，还允许返回一个函数！

Python对函数式编程提供部分支持。由于Python允许使用变量，因此，Python不是纯函数式编程语言。




# 匿名函数
语法：
lambda [arg1,arg2...argn : expression]

匿名函数有个限制，就是只能有一个表达式，不用写return，返回值就是该表达式的结果。


```
list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

# lambda x : x * x 实际上就是def，
def f(x):
    return x * x

# 匿名函数也是一个函数对象，也可以把匿名函数赋值给一个变量再
# 利用变量来调用该函数：
f = lambda x: x * x
print(f(5))

# 也可以把匿名函数作为返回值返回
def build(x, y):
    return lambda: x * x + y * y

```

reduce、map、filter三个函数可以用来进行更有效的操作。



# decorator 装饰器
装饰器就是函数的包装，可以写成函数、也可以写成class
```
def hello(fn): #装饰器本身是一个高阶函数，传入的参数是一个函数
  def wrapper():
    print('start' + fn.__name)
    fn()
    print('end' + fn.__name__)

  return wrapper #该hello函数返回一个函数

@hello #装饰
# @hello1(arg1)
# @hello2(arg1,arg2) 可以传入参数

def foo():
  print('here it is')

# start,foo
# here it is
# end foo

# 简单的说 func --> decorator(func)

```

# 偏函数
部分函数，只设置一部分参数
```
import functools

int2 = functools.partial(int,base=2)
int2('1000')
```




## 高级面向对象

```
__slots__:

1. 使用__slots限定class实例能添加的属性:__slots__ = ['name','set_name']

2. __slots__仅对当前类实例起作用，**对继承的子类是不起作用的**
```

```
property:

1. 属性的获取使用getters/setter
2. 利用@property简化get/set方法
3. 利用@property实现只读属性
4. 装饰器与property的实现

```

# 枚举
```
from enum import Enum
Moth = Enum('Month',('Feb','Setmp','Mar'))
for name,member in Month.__members.items():
  print(name ==> member, ', ' member.value)

```


# 元类
使用type创建新类型
metaclass(元类)


# 异常与错误处理

# 单元测试
```
import unittest


class MyDict(dict):
  pass

class TestMyDict(unittest.TestCase):
  def setUp(self):
    print('测试前初始化')

  def terDown(self):
    print('测试结束')

  def test_init(self):
    d = MyDict(one = 1, two = 2)
    self.assertEqual(d['one'],1)
    self.assertEqual(d['two'],2)

if __name__ == '__main__':
  unittest.main()

```





























---
