程序介绍：
    角色:学校、学员、课程、讲师
    要求:
    1. 创建北京、上海 2 所学校
    2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开
    3. 课程包含，周期，价格，通过学校创建课程
    4. 通过学校创建班级， 班级关联课程、讲师
    5. 创建学员时，选择学校，关联班级
    5. 创建讲师角色时要关联学校，
    6. 提供两个角色接口
    6.1 学员视图， 可以注册，交学费， 选择班级，
    6.2 讲师视图， 讲师可管理自己的班级， 上课时选择班级， 查看班级学员列表 ， 修改所管理的学员的成绩
    6.3 管理视图，创建讲师， 创建班级，创建课程
    7. 上面的操作产生的数据都通过pickle序列化保存到文件里
    程序结构：
Course selection2.0
   bin:
        course_selection.py #执行程序
   conf:
        setting.py #配置文件
   core:
        auth.py #用户认证模块
        main.py #程序主逻辑
        userinfo.py # 用户信息操作修改模块
        admin.py #管理员模块
        teacher.py #讲师模块
        student.py #学员模块
   db:
        classes # 班级信息数据库
        course # 课程信息数据库
        grade # 成绩信息数据库
        login # 登录信息数据库
        record # 打卡记录信息数据库
        school # 学校信息数据库
        student # 学生信息数据库
        teacher # 教师信息数据库
注：
   1.管理员默认账户密码：
       admin 123456
   2.创建讲师默认账户密码：
       123456
