# 第 4 章 操作列表

## 遍历整个列表

for 循环打印所有魔术师名字

```py
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
```

输出：

    alice
    david
    carolina

临时变量使用任何名字都可以，但是选择描述单个列表元素的有意义的名称是最好的

## 注意缩进

for 循环体的内容要缩进才行，不要过度缩进，注意冒号

## 创建数值列表

### range()

三个参数，`(start, end, step)`，左闭右开区间

```py
numbers = list(range(1,6))

print(numbers)  # [1, 2, 3, 4, 5]
```

打印 1~10 内的偶数

```py
even_numbers = list(range(2,11,2))

print(even_numbers)  # [2, 4, 6, 8, 10]
```

### 统计计算：`sum()`、`max()`、`min()`

### 列表推导式

平方数列表

```py
squares = [value**2 for value in range(1,11)]

print(squares)  # [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
```

> 先考虑编写清晰易读且能完成所需功能的代码，再考虑采用更高效的方法

## 使用列表的一部分

### 切片

与 `range()` 类似，三个参数左闭右开区间

两个区间限值都可以省略以表示从头开始或到头为止，可以使用负值

```py
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players[1:4])  # ['martina', 'michael', 'florence']
```

### 复制列表

使用切片复制

```py
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
```

运行结果表示正确的复制了一份列表为朋友喜欢的食物，并且能分别为我和朋友添加喜欢的食物

    My favorite foods are:
    ['pizza', 'falafel', 'carrot cake', 'cannoli']
    My friend's favorite foods are:
    ['pizza', 'falafel', 'carrot cake', 'ice cream']

单纯的赋值是无法产生两份食物列表的

```py
my_foods = ['pizza', 'falafel', 'carrot cake']
# 这行不通
friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)
```

输出表明两个变量名代表的其实是同一个列表

    My favorite foods are:
    ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']
    My friend's favorite foods are:
    ['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

## 元组

Python 中不能修改的值称为**不可变的**，不可变的列表就是**元组**，元组的取值和列表是一致的

### 定义元组

元组使用圆括号标识 `()`

```py
dimensions = (200, 50)

print(dimensions[0])  # 200
print(dimensions[1])  # 50
```

当尝试修改元组内的值的时候，Python 将会抛出异常

### 遍历元组中的所有值：for 循环

### 修改元组变量

元组内部的值无法改变，但是可以通过为变量赋值另一个元组来实现改变变量的值的目的

## 设置代码格式

### 格式设置指南

如果要提出 Python 语言修改建议，需要编写 Python 改进提案（Python Enhancement Proposal，PEP）

> Enhancement: [ɪnˈhænsmənt]

PEP8 提供了 Python 的代码格式设置指南

如果非要在易于编写和易于阅读之间做出取舍，那应该选择后者

### 缩进

每级缩进使用 4 个空格

> Python 解释器允许 Tab 和空格两种缩进，但两种只能择一，不可同时使用。但是建议是使用 4 个空格，而不是 2 个或 8 个或 Tab。

### 行长

每行不超过 80 个字符（最多 79 个），最初是因为当时终端窗口每行只能容纳79字符，而现在则更多地因为专业程序员通常在一个屏幕上打开多个文件，标准行长可以让他们在屏幕上并排打开两三个文件时同事看到各个文件的完整行

注释不超过 72 个字符，因为有些工具为大型项目自动生成文档时，会在每行注释开头添加格式化字符

编辑器中可以设置一个竖线来提示我们

### 空行

使用空行来组织程序文件，隔开程序的不同部分，但也不能滥用。

空行不会影响代码的运行，但会影响代码的可读性。Python 解释器根据水平缩进解读代码，但不关心垂直间距
