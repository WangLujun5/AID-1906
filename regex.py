"""
    regex.py re模块 功能函数演示
"""
import re

# 目标字符串
s = "Alex:1994,Sunny:1996"

pattern = r"\w+:\d+"

# re模块调用findall
l = re.findall(pattern,s)
print(l)

# compile 对象调用findall
regex = re.compile(pattern)
l = regex.findall(s,3,5)    # 3,5截取目标字符串
print(l)

