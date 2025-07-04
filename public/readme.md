# 多语言

## 规则
1. client 目录的截图统一引用 ../../public/cn/xx
2. 中文简体和繁体版本共用
✅ 已经迁移
```
![图片](/media/cn/app-code.png)
```

3. 其他语言版本，与英文版共用
```
![图片](/media/en/app-code.png)
```
⏳ 处理中
简体中文 cn
英文 en
日文 jp
韩文 ko
繁体中文 zh（不支持 zh-TW）

## 指令

```shell Bash
cd /path
gemini

这是 Aihubmix 的一系列官方文档
将文件夹内的 mdx 文档翻译为韩语

rules：
- 遵循翻译的最佳实践
- 只做翻译，不得做增/删操作
- 保护链接和代码块：多语言版本，图片和视频都是共用 ../../public/en 目录的资源，不需改动
- 代码主要翻译注释和关键输入
- 价格/费率不改动，统一口径 $
- 特殊处理 Multimodal-Interaction-with-Gemini.mdx: gemini 多模态只支持 English 输入，代码块的 prompt 维持英语
```

## 注意事项
跨目录复用图片，推荐统一放 public 下，只能用相对路径 ../../public/cn/xxx.png 引用。

"/cn/ghibli.png" ❌  
"/public/cn/ghibli.png" ❌  
"../../public/cn/ghibli.png" ✅  
这样所有语言、所有文档都能安全、方便地访问同一份资源。
