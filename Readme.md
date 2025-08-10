## 文档撰写规范
- Aihubmix Docs 不是简单的操作手册，除了指引开发者/AI IDE 如何使用，更应该体现功能和更新等的作用。简要规范如下，也适用于更新日志：
```
[更新]，[作用]
```
例：  
```
# 指南
此处为最新 OpenAI 包的使用指引，大陆用户可以直连使用，构建业务更省心。

# 更新
新增 OpenAI CodeX CLI 支持！在命令行中用自然语言编程。
```
- 📍 文档名称规范：使用英语、"-" 连接符，否则会导致：
  - 不利于 SEO 且显示异常
  - 导航异常
  - 底部无法翻页
- 引用链接时，文件名的空格要替换为 %20，例如：[Claude 原生接口调用](/api/Claude%20原生接口调用)
- 做好脱敏，发布前务必检查，确保没有写入 API KEY
 
**两种图片引用格式示例**
1. 卡片
```
<Card title="Girl with a Pearl Earring" img="/media/en/Girl-with-a-Pearl-Earring.PNG">
  1. The famous painting is reinterpreted, with text and watermark directly output.
</Card>
```

2. 直接显示，注意文字标题要有清晰的语义，如：
```
![auth](../../public/cn/claude-auth.png)
```

**带格式的功能信息块**
带有特殊功能的信息块用以下 xml 标签组来展示，不需要 codeblock。
注意，当前使用 ```codeblock``` 主要用于 Github 解析。

辅助信息
```
<Info>
  辅助信息
</Info>
```

实用技巧
```
<Tip>
  实用技巧
</Tip>
```

警告或提醒
```
<Warning>
  需要强调的注意事项
</Warning>
```

代码示例务必用编组收纳，确保良好的可读性：

```
<CodeGroup>

```shell 清晰的名称
```

```py 清晰的名称
```

</CodeGroup>
```

邮件链接：
[business@aihubmix.com](mailto:business@aihubmix.com)

---

## 实用方法
1. 图片在 Github 仓库上传
2. 优先处理 cn → Claude Code 批处理翻译为 en、jp、ko、zh-Hant
3. 主要配置项为文档路径 docs.json 和每种语言目录下的更新日志 changelog/News.mdx
4. 优先发布 cn 和 en，完成宣发后排期补其他语言

## 注意事项
- 只能主号 commit deploy
- 本地开发：`mintlify dev` 运行
- 根目录的 docs.json 管理全局的配置，新增文档要在这里引用
- 先处理 logo 和品牌色版，后续需要改成 iferEra
- 导航形式只能在顶部 tab 和侧边 sidebar 二选一
- 多语言支持 @navigation/localization.mdx

---

**Step 1**: Install the Mintlify CLI:

<CodeGroup>

```bash npm
npm i -g mintlify
```


```bash yarn
yarn global add mintlify
```


```bash pnpm
pnpm add -g mintlify
```

</CodeGroup>

**Step 2**: Navigate to the docs directory (where the `docs.json` file is located) and execute the following command:

```bash
mintlify dev
```

Alternatively, if you do not want to install the CLI globally you can use a run script available:

<CodeGroup>

```bash npm
npx mintlify dev
```


```bash yarn
yarn dlx mintlify dev
```


```bash pnpm
pnpm dlx mintlify dev
```

</CodeGroup>

<Warning>
  Yarn's "dlx" run script requires yarn version \>2. See [here](https://yarnpkg.com/cli/dlx) for more information.
</Warning>

A local preview of your documentation will be available at `http://localhost:3000`.

### Custom Ports

By default, Mintlify uses port 3000. You can customize the port using the `--port` flag. To run Mintlify on port 3333, for instance, use this command:

```bash
mintlify dev --port 3333
```

If you attempt to run on a port that's already in use, it will use the next available port:

```md
Port 3000 is already in use. Trying 3001 instead.
```

## Versions

Please note that each CLI release is associated with a specific version of Mintlify. If your local website doesn't align with the production version, please update the CLI:

<CodeGroup>

```bash npm
npm i -g mintlify@latest
```


```bash yarn
yarn global upgrade mintlify
```


```bash pnpm
pnpm up --global mintlify
```

</CodeGroup>

## Validating Links

The CLI can assist with validating reference links made in your documentation. To identify any broken links, use the following command:

```bash
mintlify broken-links
```

## Deployment

If the deployment is successful, you should see the following:

![You Did it](/images/deployment/checks-passed.png)

## Code Formatting

We suggest using extensions on your IDE to recognize and format MDX. If you're a VSCode user, consider the [MDX VSCode extension](https://marketplace.visualstudio.com/items?itemName=unifiedjs.vscode-mdx) for syntax highlighting, and [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode) for code formatting.

## Troubleshooting

<AccordionGroup>
  <Accordion title='Error: Could not load the "sharp" module using the darwin-arm64 runtime'>
    This may be due to an outdated version of node. Try the following:

    1. Remove the currently-installed version of mintlify: `npm remove -g mintlify`
    2. Upgrade to Node v19 or higher.
    3. Reinstall mintlify: `npm install -g mintlify`
  </Accordion>
  <Accordion title="Issue: Encountering an unknown error">
    Solution: Go to the root of your device and delete the ~/.mintlify folder. Afterwards, run `mintlify dev` again.
  </Accordion>
</AccordionGroup>

## 文档迁移完成

- 确认只能主号 commit deploy
- 建立骨架
- API 目录下的文档细节修复
- Sidebar 改成 Tab
- review 中文版结构
- 多语言适配：只需要在对应语种目录下添加对应语言的文件，docs 引用即可
- 迁移英文版
- 修复双语配置顺序
- 双语版本的路径：中文/cn/index 英文/en/index
- 域名迁移
- 正式发布 🎉