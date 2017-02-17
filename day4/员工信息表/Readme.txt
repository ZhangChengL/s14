1.数据表字段依次为：staff_id 用户ID,name 用户名,age 年龄,phone 电话号码,dept 职位,enroll_date 入职日期
2.支持语法：
    简单的查询语句以及模糊查询支持like,>,<,=
        例：
            select name,age from staff_table where age > 22
        　　select * from staff_table where dept = IT
            select * from staff_table where enroll_date like 2017
         注：只支持最多一个where，即 where 后不能加and,or
    添加：insert into emp values(xxx,xx,xx,xx,xx)
        注：请严格按照字段顺序录入对应数值，用户ID无需手动输入，电话号码不能重复
    删除：可删除指定员工信息纪录，输入员工id，即可删除
        例：delete from emp where staff_id = 1
    修改：可修改员工信息，语法如下:
    　　UPDATE staff_table SET dept = Market WHERE where dept = IT
    按'q' or 'Q'可退出查询
注：请严格使用空格进行语法分割，关键字无需使用引号，使用中请使用正确的字段名！
