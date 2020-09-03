# 第1章 起步

按照计算机语言惯例，第一个目标就是 Hello World 程序
```py
# hello_world.py
print('Hello World!')  # Py3 当然2中也能正常运行
```

## Python 2 还是 Python 3？

如果你纠结于选择2还是3，那么选择3。如果你已经安装了2，那么建议你赶紧升级3。

## Python 自带终端（terminal）运行的解释器（interpreter）

在终端中输入 `python` 即可进入

```sh
$ python
Python 3.7.1 (default, Dec 14 2018, 13:28:58)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> print('Hello Python interpreter!')
Hello Python interpreter!
```

- `>>>` 三个尖括号表示代码输入提示符，在其后输入 Python 代码，回车即可运行
- **退出**：运行 `exit()` / 运行 `quit()` / 快捷键 <kbd>Ctrl</kbd> <kbd>D</kbd> / 快捷键 <kbd>Ctrl</kbd> <kbd>Z</kbd>

## Linux 中搭建 Python 环境

大多数 Linux 系统中都默认安装了 Python。

使用 Geany 文本编辑器（易于安装、直接运行程序、高亮）

```sh
$ sudo apt-get install geany
```

## 查看Python解释器的完整路径

```sh
$ type -a python
```

## Windows 中安装 Python

一定记得安装时勾选 Add Python x.x to PATH

Windows 中的显示目录下所有文件的命令
```sh
$ dir
```

## 终端运行 Python 文件

```sh
$ python xxx.py
```