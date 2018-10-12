#用例1：
#定义一个RF变量var1为整数 100
#定义一个RF变量var2为字符串 '5'
#用RF关键字 should be true 验证变量 var1 * int(var2) == 500

#用例3 ：
#登录百度网站搜索 "北京时间" ，检查第一个搜索项显示当前的年份是否是 2017年。
#SeleniumLibrary 有关键字 Get Text， 其参数 如果使用 css选择元素的方法 以'css='开头，后面加上 css选择表达式

*** Settings ***
Library    SeleniumLibrary
Library    Collections

*** Test Case ***
用例1：关键字练习1
    ${var1}    Convert To Integer    100  # 关键字、变量、参数之间空格两个以上
    ${var2}    Convert To Integer    10
    ${var3}    Set Variable    5
    should not be equal    ${var1}    ${var2}
    Should Be True    $var1 * int($var3) == 500  # RF中，python表达式内的变量没有{}

用例2：关键字练习2
    ${list}=   create list
    ${dict}=   create dictionary
    Append To List  ${list}  hello  world
    Set To Dictionary  ${dict}   a=1
    log to console    list中第一个元素是：@{list}[0]
    :FOR   ${var}  IN   @{list}                 #     for var in list:
    \   log to console  list中元素有：${var}    #          print(var)


用例3：百度北京时间年份是否正确
    open browser    http://www.baidu.com    chrome
    Set Selenium Implicit Wait    5
    Input Text    id:kw    北京时间
    Click Button    id:su
    ${text}    get text    css:span.op-beijingtime-date
    Should Contain    ${text}   2017年
    close browser

