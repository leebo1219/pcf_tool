# PCF_tool
It's to generate PCF(Potatso Config File) to import the version 2 of Potatso

本工具用于生成Potatso 2中的PCF（Potatso Config File）配置文件，由pcf_tool.py、PROXY.txt、DIRECT.txt、REJECT.txt组成。
## 文件介绍
### 主程序
pcf_tool.py，用于生成.pcf文件，代入Potatso 2中。
### 规则文件
PROXY.txt，用于存放需要经过代理服务器的域名，给生成PCF配置文件使用；

DIRECT.txt，用于存放需要不经过代理服务器的域名，给生成PCF配置文件使用；

REJECT.txt，用于存放拒绝连接的域名，给生成PCF配置文件使用，一般用于屏蔽广告。
## 使用方法
### 写入规则文件
如我们要让google.com、youtube.com经过代理服务器，这打开PROXY.txt，写入如下内容：
```
google.com
youtube.com
```
每一行写一个域名，不需要有多余的,（逗号）;（分号）来进行分割。
### 程序的运行
将pcf_tool.py、PROXY.txt、DIRECT.txt、REJECT.txt放置在同一个目录下，用终端进入到目录中，如文件在桌面，则代码如下：
```python
cd ~/Desktop
python pcf_tool.py
```
输入并回车即可运行，接着就按照提示进行操作。
## 其它说明
本程序的效率还有待进一步提高，并且对用户输入，还需要加入正则表达式来规范，希望网友们可以帮忙一起完善它。
