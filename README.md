# Auto-Test-Frame
## auto test framework
### 环境
language:Python 3.7 
browser:Firefox
### 使用的library
logging
selenium
xlutils
xlrd
configparser
unittest
operator
json
time
os
### 前言
本工具利用selenium和unittest搭建了一个自动化web测试框架，可用于高效开发测试脚本，即用较少的代码完成自动化测试，减少开发成本，提高测试效率。
- 在ini配置文件中可以设置通用信息如url和browser。
- 在.xls文件中可通过填入三组参数来编写、组建测试用例。如设置要执行的测试步骤，每步操作之后的sleep时间，一系列操作后的assert。
- 在代码文件中，只需在框架中添加少许代码就能完成测试脚本的开发。比如，在代码中创建类的实例，调用框架中已封装好的execute函数，可以自动完成.xls文件中设置好的一系列的测试用例，并将assert结果记录到.xls文件中。
- 在日志中可查看完备的执行记录，遇到错误或在代码中调用了封装好的截屏函数则可查看截屏。可利用日志迅速定位bug并提供证据。
### 框架结构
![](https://img2020.cnblogs.com/blog/2049095/202009/2049095-20200919180746714-981112199.jpg)
1. common中封装了执行用例所需的基本模块。
- browser.py封装了浏览器的open、close和quit方法
- excel.py封装了操作excel所需的各种方法：open、copy、sheet_by_index、sheet_names、cell_value、get_sheet、write和save等。
- page.py封装了操作page的各种方法：
```
    def get_windows_img(self, name='', fail=True):
        
    def refind(self, by=By.ID, value=''):
        
    # find_element  by:元素定位方法  value:元素位置
    def find_element(self, by='i', value=''):
        """
        定位元素
        :param  by:定位方法
                value:元素位置
        :return:element:定位成功后找到的元素
        """

    # Text input 文本框输入    text:要输入的文本
    def send_keys(self, by, value, text):
        
    # Text clear 文本框清空
    def clear(self, by, value):
        
    # click 点击事件
    def click(self, by, value):
    
    # 获取属性      attr:要获取的属性   
    def get_attribute(self, by, value, attr):
        
    def execute_script(self, js=''):
        
    def set_window_size(self, n, m):
        
    # Dictionary类型win_size_dict会存储windows分辨率
    def get_window_size(self, win_size_dict):
        
    def maximize_window(self):
        
    def back(self):
        
    def forward(self):
        
    def refresh(self):
        
    def close(self):
    
    # 获取当前url    
    def current_url(self):
        
    # 获取网页标题
    def get_url_title(self):
        
    def switch_to_frame(self, value):
     
    # 先找到frame元素再切换 
    def switch_frame(self, by='i', value=''):
        
    def switch_to_default_content(self):
        
    def switch_to_parent_frame(self):
     
    # handle_list[0]中会存储当前window的handle 
    def current_window_handle(self, handle_list=None):
        
    def window_handles(self):
        
    def switch_to_window(self, handle):
    
    # handle_list[0]中存储着要切换的handle    
    def switch_window(self, handle_list):
```
2. config
- config.ini存储通用信息
![](https://img2020.cnblogs.com/blog/2049095/202009/2049095-20200919192110797-1311368177.jpg)

- config_parser.py封装了读取ini文件的方法。
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
