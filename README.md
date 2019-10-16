# Translation-In-Command-Line
基于命令行的翻译工具
version:1.0.0

# 效果
```
$ dic hello world
你好世界

$ dic 你好世界
hello world
```
# 环境
python 2.7.4

ubuntu 14.04.3

# 使用方法
1.需要注册开发者,点击[这里](http://api.fanyi.baidu.com/api/trans/product/index)注册
如果已有账号，则跳过此步骤

2.克隆本库

3.在dic_conf.txt里输入相应信息

4.将dic文件里的./main.py(最后一行)改为绝对路径，将parse.py里的./dic_conf.txt也改为绝对路径

# 用户须知
* 所译内容为纯英文的情况,请在英文状态下输入
* 所译内容为中英文混杂的情况,英文部分请再中文状态下输入

# 正在完成
* 重定向
