程序介绍：
    开发简单的FTP：
    1. 用户登陆
    2. 上传/下载文件
    3. 不同用户家目录不同
    4. 查看当前目录下文件
    5. 充分使用面向对象知识
FTP：
    bin:
            Sock_client.py #客户端执行程序
            Sock_server.py #服务端执行程序
    conf:
            setting.py #配置文件
    core:
            auth.py #用户认证模块
            main.py #程序主逻辑
            userinfo.py # 用户信息操作修改模块
            admin.py #管理员模块
            user.py #普通用户模块，客户端ftp主程序
    db:     #用户信息存放数据库
    file_data:  #用户家目录

注：
1.执行客户端程序前请务必先执行服务器程序，确保服务器程序已启动！
2.管理员默认账户密码：
       admin 123456
3.创建讲师默认账户密码：
       123456
4.请严格按照操作格式进行ftp操作！
