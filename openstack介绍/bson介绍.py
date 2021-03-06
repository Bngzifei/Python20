# coding:utf-8

BSON( Binary Serialized Document Format):类json的一种二进制形式
 是一种二进制形式的存储格式，采用了类似于 C 语言结构体的名称、对表示方法，支持内嵌的文档对象和数组对象，具有轻量性、可遍历性、高效性的特点，可以有效描述非结构化数据和结构化数据。
主要用于mongodb,是mongodb的数据存储格式.BSON基于JSON格式.

主要实现三点:
1.>更快的遍历速度
2.>操作更容易
3.>增加了额外的数据类型 byte array .这样就使得二进制存储不再需要先base64转换后再存json.

综上所述

　　数据结构上json是按字符串存储，bson是按结构存储。

　　存储空间上 bson>json

　　操作速度上 bson>json。比如，遍历查找：json需要扫字符串，而bson可以直接利用预先在字符串前面的字符串长度直接定位。

　　修改上json要因为字符串长度的改变而大动大移，bson的话因为是按结构存储，因此还是占用同样的存储空间，不需要移动。