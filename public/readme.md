# 多语言资源问题

跨目录复用图片，推荐统一放 public 下，只能用相对路径 ../../public/cn/xxx.png 引用。

"/cn/ghibli.png" ❌
"/public/cn/ghibli.png" ❌
"../../public/cn/ghibli.png" ✅

这样所有语言、所有文档都能安全、方便地访问同一份资源。

中文简体和繁体版本共用
✅ 已经迁移
```
![图片](/media/cn/app-code.png)
```

其他语言版本，与英文版共用
```
![图片](/media/en/app-code.png)
```
⏳ 处理中
日文
韩文
繁体中文

client 目录的截图统一引用 ../../public/cn/xx


