## selenium 工作原理

### selenium原理
- 自动化测试代码发送请求给浏览器驱动；
- 浏览器驱动 解析自动化测试代码，发送给浏览器；
- 浏览器：执行浏览器驱动发送的指令

### selenium 和浏览器如何通信
- 对于每一条selenium，会创建一个http请求发送给浏览器的驱动；
- 浏览器驱动中包含了一个HTTP Server，用来接受这些http请求；
- HTTP Server接受请求后根据请求来具体操控对应的浏览器；
- 浏览器执行具体的测试步骤；
- 浏览器将执行步骤结果返回给HTTP Server；
- HTTP Server又将结果返回给selenium的脚本；

### WebDriver协议
- 通讯格式是JSON；
- 在http之上封装的公有协议；