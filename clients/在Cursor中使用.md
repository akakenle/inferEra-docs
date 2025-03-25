---
sidebar_position: 7.1
---

# 在Cursor中使用
## 通常使用方法
- 右上角点击齿轮进入设置页面，选择Models。  
- 在Open API key下方输入[本站的Key](https://aihubmix.com/token)。  
![图片](../media/cur1.png)
- 点击Override OpenAl Base URL，输入：  
```
https://aihubmix.com/v1
```  
![图片](../media/cur2.png)
- 最后点击Verify验证通过即可。

## 特殊说明（在Cursor中使用claude-3.5的方法）
由于cursor自动根据请求名请求claude的api接口，所以为了可以通过我们的服务正常使用claude-3.5模型，  
我们新增了一个**anthropic-3-5-sonnet-20240620**的名字来映射到claude-3-5-sonnet-20240620，  
以此来绕过cursor的自动请求，从而通过我们走claude接口。  
- 具体使用方法为：在模型列表中添加名为：**anthropic-3-5-sonnet-20240620**的模型。选择启用该模型即可。  
![图片](../media/cur3.png)