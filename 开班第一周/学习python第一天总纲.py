'''
1).python基础语法：4周课程(结束阶段考试)

2).前端知识点：html、css、javascript(js)、jQuery

3).Linux(系统)、数据库(关系型&非关系型)

4).python框架

5).爬虫

6).数据分析(人工智能)

数据库(database：db)

定义：存储数据的仓库

主要的对象：数据表(table)

常见的数据库对象：表、视图、索引、序列、同义词...

表结构：行(row)、列(column)

行：一条数据(信息)

列：字段(单独的信息数据)

sql：structure query language(结构化查询语言)

分类：

1).DDL操作：(强硬、相当于企业中的ceo)

针对于操作数据库对象(表格)的层面：

包含：

①.创建表：create table ...

②.删除表：drop table ...

③.修改表(增加/删除/修改一个列)：alter table ...

④.清空表：truncate table ...

特点：

默认提交，没有后悔药吃(不允许返回)

2).DML操作：(柔和、相当于企业中的项目经理)

针对于数据层面：

包含：

①.增加数据：insert into ...

②.删除数据：delete ...

③.修改数据：update ...

④.查询数据：select ...

特点：

不会默认提交，可以回滚(有后悔药吃)

web程序员口头禅：crud操作(增删改查)

3).DCL操作：

针对于一些事物的处理：

包含：

①.提交操作：commit

②.回滚操作：rollback

oracle中的数据类型：

1).数值型：number

划分：

①.整数型：

变量m：表示长度

number(m)-->举例：number(5)1000(对)、20000(对)、0(对)、999999(错)

②.浮点型：

变量m:表示整体的长度

变量n：小数占多少位

number(m,n)-->举例：number(8,3)1234.567(对)、123.23(对)、666666.666(错)

2).字符型：

变量m：表示长度

划分：

①.定长字符：

char(m)：-->举例：char(3)性别(男/m/0、女/f/1)

②.变长字符：

varchar2(m)：-->举例：char(30)性名：东方不败、欧阳震华

区分定长和变长字符：

对于变长字符而言，如果数据存不满，数据库底层会自动的将剩余的容量节省出来，但是检索效率比较慢(相当于定义而言)

对于定长字符而言，如果数据存不满，数据库底层会还是会将多余的容量用掉(浪费)，但是检索效率比较快(相当于变长而言)

3).日期型：

关键字：date

DDL操作之创建表格：

格式：

create table 表名(

列名1 数据类型1(长度),

列名2 数据类型2(长度),

...

列名n 数据类型n(长度)

);

注意事项：

1).标点符号全部必须是英文输入法下的

2).表名我们不能重名,不要使用中文命名

3).最后一个列名后面可以省略分号

需求：

创建我们的第一张表格：表名(python1808_你的名字)

设计的列和类型&长度如下：

列名类型&长度

姓名(name)varchar2(30)

年龄(age)number(3)

性别(sex)char(2)

出生年月(birthday)date

毕业学校(school)varchar2(25)
'''