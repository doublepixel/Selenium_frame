运行环境：
    Python3及以上
    selenium
    parameterrized
    configparse
    xlrd



目录结构：
    data目录  放置Excel文件
                文件第一行需要声明数据名称、第二行及以后每一行为一组传入数据参数

    package目录放置了将测试报告生成HTML的方法

    report  放置测试报告生成文件
        image   放置了测试用例的截图文件

    test_case
        放置了测试用例执行脚本
        models
            MyUnit 封装setUP和TearDown类方法
            test_function  封装了截图方法和读取Excel方法
        page_obj
            base.py  封装了基础方法 如打开URL、获取元素方法等
            login_page 封装了初始化测试用例  用户登录
            其他  为各个模块测试用例的方法
     config.ini  框架配置文件
     config.py   读取配置文件的方法
    run_test.py   运行所有测试用例，并生成测试报告




