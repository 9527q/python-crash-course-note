# 第 2 章 变量和简单数据类型

## 变量

关联一种数据的量

命名：
- 只能使用字母、数字、下划线组成，且不能以数字开头
- 不能包含空格，可以使用下划线来关联单词
- 不要将 Python 关键字和函数名用作变量名，即不要使用已经有特殊用途的名字
- 变量名应即简短又具有描述性
- 慎用 l 和 O，容易被看成 1 和 0
- 大小写敏感

运行时可能会遇到**名称错误**，它一般由两个原因产生：使用前忘记给变量赋值了，或者变量名拼写错误了

> **trackback**
> 
> traceback 是一条记录，当解释器无法成功的运行代码时，就会提供一个 traceback 以指出尝试运行代码时在**哪里**遇到了**何种**困难

## 字符串

一系列字符

Python 中引号括起来的都是字符串，可以是单引号，也可以是双引号

### 改变大小写

```py
name = "ada loveLAce"
print(name.title())  # Ada Lovelace
print(name.upper())  # ADA LOVELACE
print(name.lower())  # ada lovelace
```

`name` 变量后面的句点 `.` 让 Python 对变量 `name` 执行后面的 `title()` 指定的操作。每个方法后面都有一对括号，因为方法通常需要额外的信息来完成工作，这些信息是从括号中提供的，这里 `title()` 不需要额外的信息，所以括号里是空的。

**`title()` 把字符串处理成首字母大写、其余字母均小写**的格式。`upper()` 将所有字母都转变为大写。`lower()` 将所有字母转换成小写。

### 合并（拼接）字符串

```py
first_name = "宇琪"
last_name = "刘"
full_name = first_name + " " + last_name

print(full_name)  # 宇琪 刘
```

合并字符串使用加号 `+`，这种合并字符串的方式被称为**拼接**

### 使用制表符、换行符添加空白

编程中，**空白**泛指任何非打印字符，如空格、制表符 `\t`、换行符 `\n`

```py
>>> print("Python")
Python
>>> print("\tPython")
    Python
>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C
JavaScript
```

### 删除空白

`.lstrip()`、`.rstrip()`、`.strip()` 分别为去除字符串左侧、右侧、两侧的空白


### 注意字符串的语法错误

如果单引号包裹的字符串里面还有一个单引号，那么解释器会认为字符串提前结束了，后面都是违规的代码，会抛出**语法错误**

要注意最外面声明字符串的引号和内部的引号不能一致，或者使用转义

## 数字

### 整数

整数可进行加 `+`、减 `-`、乘 `*`、除 `/` 运算，且支持运算次序

### 浮点数

Python 将带有小数点的数都成为**浮点数**，小数点可能出现在其任意位置

### 与字符串的加法

要想将数字拼接到字符串中，要使用 `str(数字)` 对数字进行类型转换

## 注释

井号 `#` 后面的内容将被认为是注释，会被 Python 解释器忽略

在代码中编写清晰、简洁的注释

## Python之禅

由 Tim Peters 撰写，只需在解释器中执行 `import this` 即可看到全文

> Beautiful is better than ugly.

Python 程序员确信代码可以编写得漂亮而优雅

> Simple is better than complex.

同样有效的两个方案，一个简单一个复杂，选择简单的，易于自己和他人的维护和改进

> Readability counts.

复杂的代码也要让他易于理解，注释是个好工具

> There should be one-- and preferably only one --obvious way to do it.

应该使用尽可能简单常见的方案解决问题，在一个大项目的具体细节中，各种实现应该对其他 Python 程序员来说是易于理解的

> Now is better than never.

不要企图编写完美的代码，先编写行之有效的代码
