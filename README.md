# Auto-Test-Frame
## auto test framework
### 环境
language:Python 3.7 

browser:Firefox
### 前言
本工具利用selenium和unittest搭建了一个自动化web测试框架。
在ini配置文件中可以设置通用信息如url和browser，在.xls文件中可填入参数如要执行的操作，每步操作之后的sleep时间，一系列操作后的assert。
打开代码文件，在代码中创建类的实例，调用执行用例的函数就可以自动完成.xls文件中设置好的一系列的测试并将结果记录到.xls文件中，在日志中可查看执行记录，错误或设置了截屏可查看截屏。此工具的目的是用较少的代码完成自动化测试，减少开发成本，提高测试效率。
### 使用说明
一.config.ini文件用于记录通用信息。在这里设置要用到的浏览器类型和要打开的url。程序中也可不使用此处指定的信息。

二..xls文件（必须是这个扩展名，已上传了模板）填写测试用例详细信息：步骤、sleep时间、assert。

1.步骤的填写

方法名,参数&方法名,参数,参数
+ 无参数可省略“,参数”。
+ 参数之间用“,”间隔，步骤之前用“&”间隔，符号用英文字符，不要有空格。

例：get_url_title&get_attribute,c,icon_qq,c

执行用例的函数会按此次序依次执行操作。具体方法和参数详见page类，page类基本封装了所需的大部分操作。


2.sleep时间的填写

整数,整数,整数...
+ 0为步骤中第一个方法执行后sleep零秒，1为第二个方法执行后sleep一秒，依次类推。“,”用英文字符，不要有空格。

例：0,1,2


3.assert的填写

unnitest断言函数名,参数（值）:参数（方法，用其取得校对值）,方法参数,方法参数
+ 能取得校对值的方法若无参数可省略“,方法参数”。
+ 参数之间用“,”间隔，参数（值）与参数（方法，用其取得校对值）之间用“&”间隔，assert之间用“&”间隔，符号用英文字符，不要有空格。

例：assertIn,登录:get_url_title&assertIn,icon_qq:get_attribute,c,icon_qq,c

三.代码
```
# 可通过config.get_value("browserType", "browserName")指定browser，也可自行指定
# config.get_value("testServer", "URL")指定url，也可自行指定
self.browser = Browser(BaiduTest.browser, 'https://www.iziqian.com/')

self.driver = self.browser.open_browser()
driver = Page(self.driver)

# 可通过config.get_value()读取rd_book_path、rd_book_name、sheet_name，也可自行指定
self.excl = Excel(BaiduTest.rd_book_path, BaiduTest.rd_book_name, sheet_name=BaiduTest.sheet_name)

# 1,3：从第一行循环执行到第三行，可自己依据excel文件中内容自行填写
# 可通过config.get_value()读取case_col、sleep_col、assert_col，也可自行指定
# sleep_bool=False则不读取sleep列，反之则读取并进行相应时间的sleep
# assert_bool=False则不读取assert列，反之则读取并执行相应assert
execute(self.excl, driver, 1, 3, self,
                  case_col=1, sleep_col=2, assert_col=3, sleep_bool=False, assert_bool=False)
```
暂时先写到这
