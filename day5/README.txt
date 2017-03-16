程序介绍：
    ATM：模拟实现一个ATM + 购物商城程序
    额度 15000或自定义
    实现购物商城，买东西加入 购物车，调用信用卡接口结账
    可以提现，手续费5%
    支持多账户登录
    支持账户间转账
    记录每月日常消费流水
    提供还款接口
    ATM记录操作日志
    供管理接口，包括添加账户、用户额度，冻结账户等。。。
    用户认证用装饰器
程序结构：
ATM
   bin:
        atm.py #执行程序
   conf:
        set.py #配置文件
   core:
        auth.py #用户认证模块
        logger.py #日志文件模块
        main.py #ATM程序主逻辑
        transactions.py # 金额变动模块
        userinfo.py # 用户信息操作修改模块
   db:
        accounts #ATM端用户信息数据库
        goods #购物车商品表
        shop_acc #购物车端用户信息数据库
        shopre # 用户购物记录数据库
   log:
        access.log #用户登录日志
        admin.log #管理员操作日志
        transactions.log #交易流水
   shopping:
        shopmain.py #购物端主逻辑

注：管理员账户密码为：admin admin