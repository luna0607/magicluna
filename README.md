# magicluna
用Node.js实现的个人博客
## 安装
在控制台输入
<pre><code>npm app.js
</code></pre>
再打开[http://localhost]()或[http://localhost:80]()即可
## 目录结构
```
project
│   README.md
│   .gitignore ─ （git忽略文件/文件夹）
│   app.js  ─ （主程序入口）
│   package.json ─ (引用包的列表)
│   package.json ─ (引用包的详细信息列表)
│
└───bin
│   │   www.js 
│   │  
└───public ─ （公用文件）
│   │   magicluna.ico ─（网站icon）
│   │
│   └───files
│   │     │  bootstrap.min.css ─ (bootstrap样式表)
│   │     │  bootstrap.min.js ─（bootstrap插件）
│   │     │  holder.min.js  ─（屏幕自动切图的js）
│   │     │  jquery-3.2.1.js ─ (jquery库)
│   │     │  magicluna.css ─（公用样式表）
│   │      
│   └───stylesheets
│         │  articlelist.css ─ （列表页样式表）
│         
└───routers ─ （路由）
│    │   api.js ─ （面向外部的HTTP请求路由）
│    │   index.js ─ （自用的HTTP请求路由）
│    │   dao.js ─ （操作数据的方法们）（似乎不应该放在这个目录下but whatever啦）
│   
└───views ─ （页面）   
│    │   article.html ─ （文章详情页）
│    │   article_list.html─ （文章列表页）
│    │   error.html ─ （错误页）
│    │   layout.html ─ （模板布局页）
│    │   Magicluna.html ─ （主页）
│   
```
