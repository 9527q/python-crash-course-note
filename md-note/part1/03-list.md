# 第 3 章 列表简介

## 什么是列表

列表由一系列按顺序排列的元素组成，其中可以包含任何东西，元素之间没有任何关系

由于列表一般用于存储多个元素，所以其变量名一般是复数的

Python 中用方括号 `[]` 表示列表，用逗号 `,` 隔开其中的元素

```py
bicycles = ['trek', 'cannondale', 'redline', '捷安特']

print(bicycles)  # ['trek', 'cannondale', 'redline', '捷安特']
```

打印列表将带有其方括号和逗号

### 访问元素

列表是有序集合，可以通过元素的位置或索引来访问

```py
bicycles = ['trek', 'cannondale', 'redline', '捷安特']

print(bicycles[0])  # trek
```

### 索引从 0 开始

大多数编程语言都是如此

负数索引可以倒着获取元素

```py
bicycles = ['trek', 'cannondale', 'redline', '捷安特']
message = "我最好的自行车是一辆" + bicycles[-1].title() + "。"

print(message)  # 我最好的自行车是一辆捷安特。
```

## 修改、添加和删除元素

### 修改元素

可以使用索引直接指定新值

```py
motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)  # ['honda', 'yamaha', 'suzuki']

motorcycles[0] = 'ducati'

print(motorcycles)  # ['ducati', 'yamaha', 'suzuki']
```

### 添加元素

`.append()` 结尾添加新元素；`.insert()` 在指定位置添加新元素；

```py
motorcycles = []

print(motorcycles)  # []

motorcycles.append('honda')

print(motorcycles)  # ['honda']

motorcycles.insert(0, 'ducati')

print(motorcycles)  # ['ducati', 'honda']
```

### 删除元素

`del` 可以删除指定元素；`.pop()` 可以删除列表末尾元素并让你接着能够使用它（类似于栈的**弹出**）；`.pop()` 还可以通过参数来指定弹出指定位置的元素；`.remove()` 根据值删除指定元素（如果有多个一样的元素，只删除第一个）

```py
motorcycles = ['ducati', 'honda']
del motorcycles[0]

print(motorcycles)  # ['honda']

popped_motorcycle = motorcycles.pop()

print(popped_motorcycle)  # honda
print(motorcycles)  # []

motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles.pop(0))  # yamaha
print(motorcycles)  # ['suzuki']

motorcycles.remove('suzuki')
print(motorcycles)  # []
```

## 组织列表

### `.sort()` 永久性排序

`reverse` 参数可以指定倒序排序

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()

print(cars)  # ['audi', 'bmw', 'subaru', 'toyota']

cars.sort(reverse=True)
print(cars)  # ['toyota', 'subaru', 'bmw', 'audi']
```

### `sorted()` 临时排序

`reverse` 参数可以指定倒序排序，用法同上

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

print(sorted(cars))  # ['audi', 'bmw', 'subaru', 'toyota']

print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']
```

### `.reverse()` 永久性颠倒顺序

```py
cars = ['bmw', 'audi', 'toyota', 'subaru']

print(cars)  # ['bmw', 'audi', 'toyota', 'subaru']

cars.reverse()

print(cars)  # ['subaru', 'toyota', 'audi', 'bmw']
```

### `len(列表)` 获取列表的长度

## 避免索引异常

只有列表中确有 n 号元素时，才可以使用 `列表[n]` 的取值用法，不然会报错
