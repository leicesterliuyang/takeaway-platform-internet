"""
database table column(字段) row(记录)
mysql -uroot -p123456

********************************************************
库操作
show databases;
create database [name] charset=utf8;
show create database [name];
select database();
use [name];
drop database [name];

********************************************************
表操作
create table `name`(`id` int primary key auto_increment, `name` char not null,
 `score` float unsigned default 1, `sex` enum("m","f"))
show tables;
show create table [name];
desc [name];
drop table [name];

********************************************************
索引操作
MUL index普通索引  UNIQUE唯一索引 PRIMARY主键索引
create table `name`(`id` int,`name` char,`score` float,
    primary key(column), index(column), unique(column));
create [unique] index column on [table_name](column);
show index from [table_name];
========================================================
********************************************************
表字段操作
alter table [name] add [column][column_type];
alter table [name] add [column][column_type] first;
alter table [name] add [column][column_type] after column;
alter table [name] drop [column];
alter table [name] modify [column][column_type];
alter table [name] change [column][column][column_type];
alter table [name] rename [name]

*********************************************************
数据操作
insert into [name] values(value1,value2,value3);
insert into [name] (column1,column2,column3) values (value1,value2,value3);
select * from [name];
select * from [name] where [condition];
update [name] set value=* where [condition];
update [name] set value1=*,value2=* where [condition];
delete from [name]  where [condition];

**********************************************************
限制条件
where
    可运算  +,-,/,*;
    可比较  ><= ,!=, in, not in, between, like "%A%"--regexp "正则表达式";
    可逻辑  and or not xor;
order by
    select * from [name] where [condition] order by [column] / order by [column] desc;
limit
    select * from [name] where [condition] limit [number];
union
    select * from [name] where [condition] union [all 完全拼接--distinct 去重] select *
        from [name] where [condition];
聚合
    avg(column) max(column) min(column) sum(column) count(column)
    select [column] [avg(column)] from [table] group by [column];
    聚合筛选
    select [column] [avg(column)] from [table] group by [column] having [avg(column) condition];
    可搭配运算
去重
    select distinct [column] from [name];
子集
    select * from [name] where [condition-(select * from [name] where [condition])]
    通常搭配as来减少命令长度
总括:
    select
    [distinct]
    [column,column,]--[avg(column)] from
    [table_name]
    (left / inner / right) join [table_name] on [join_condition]
    where [normal_condition]
    group by [column,column,]
    having [group_condition]
    order by [column] desc
    limit [number];

*******************************************************************
tips:
1.时间函数
    date time datetime timestamp
    now()当前日期时间 curdate()当前日期 curtime()当前时间
2.as
    可以给字段或者表重命名

"""

