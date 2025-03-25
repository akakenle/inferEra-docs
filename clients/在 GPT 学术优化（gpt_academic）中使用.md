---
sidebar_position: 16
---

# 在 GPT 学术优化（gpt_academic）中使用

1. 打开 gpt_academic/config.py文件：  
![图片](../media/image16.png) 
1. 找到 config.py中的 API_KEY 变量，将[本站的Key](https://aihubmix.com/token)填入，即可：  
![图片](../media/image17.png) 
2. 往下滚动，找到 config.py中的 API_URL_REDIRECT变量，修改为（直接复制下面的代码块进去就行）：  
```
API_URL_REDIRECT = {"https://api.openai.com/v1/chat/completions": "https://aihubmix.com/v1/chat/completions"}
```
![图片](../media/image18.png) 
3. 然后就能用了  
![图片](../media/image19.png) 
