# 商会 BI 智能看板 v2.0

## 功能概览

- **概览卡片**：8 张核心指标卡（会员总数、性别分布、在籍率、职位结构等）
- **条件筛选**：支持性别、年龄段、行业、区域、职位、政治面貌 6 维联动筛选
- **地理分布**：辽宁省商会企业分布地图 + 沈阳市各区会员热力图
- **结构分析**：行业分布、年龄结构、政治面貌、职位结构、性别比例、入会趋势 6 大图表
- **交叉分析**：行业×区域热力图 + 行业×职位分布对比
- **会员明细**：支持搜索、分页、CSV 导出
- **自动刷新**：可开启 60 秒自动刷新
- **双数据源**：支持 JSON 和 CSV 两种数据格式，可灵活切换

## 文件结构

```
shanghui-bi/
├── index.html       ← 看板主页面（纯前端，无需后端）
├── data.json        ← 会员数据（JSON 格式）
├── members.csv      ← 会员数据（CSV 格式，可用 Excel 直接编辑）
├── gen_data.py      ← 示例数据生成脚本
├── gen_csv.py       ← 从 data.json 生成 CSV 的脚本
├── excel_to_json.py ← Excel 转 JSON 工具
└── README.md        ← 本文档
```

## 数据源配置

看板支持两种数据源，在 `index.html` 中的 `DATA_SOURCE` 变量配置：

```javascript
// 方式一：读取 CSV 文件（推荐，可直接用 Excel 编辑）
const DATA_SOURCE = 'members.csv';

// 方式二：读取远程 CSV 文件（部署后自动更新）
const DATA_SOURCE = 'https://你的域名/members.csv';

// 方式三：读取 GitHub 上的 CSV（改了就自动更新）
const DATA_SOURCE = 'https://raw.githubusercontent.com/用户名/仓库名/main/members.csv';

// 方式四：留空则默认读取 data.json
const DATA_SOURCE = '';
```

## 数据更新方法

### 方法一：CSV 文件直读（最简单，推荐）

1. 用 Excel / WPS 打开 `members.csv`
2. 直接修改数据（增删改行都可以）
3. 保存文件（保持 CSV 格式）
4. 上传替换服务器上的 `members.csv`
5. 看板刷新后自动显示新数据（开启自动刷新则 60 秒内自动更新）

**适合场景**：数据量不大、更新频率不高、希望操作简单

### 方法二：远程 CSV 自动更新

1. 将 `members.csv` 上传到 GitHub 仓库
2. 在 `index.html` 中设置 `DATA_SOURCE` 为 GitHub raw 链接
3. 以后只需在 GitHub 网页上编辑 CSV → 保存 → 看板自动更新

**适合场景**：多人协作、需要随时更新、希望零运维

### 方法三：Excel 转 JSON

1. 按模板格式整理 Excel 表格
2. 运行转换脚本：
   ```bash
   pip install openpyxl
   python excel_to_json.py 你的数据.xlsx
   ```
3. 将 `DATA_SOURCE` 设为空（使用 data.json）

### CSV / Excel 字段说明

| 列名 | 类型 | 示例 | 必填 |
|------|------|------|------|
| 姓名 | 文本 | 张三 | ✅ |
| 性别 | 男/女 | 男 | ✅ |
| 年龄段 | 文本 | 36-40岁 | ✅ |
| 政治面貌 | 文本 | 中共党员 | ✅ |
| 所属行业 | 文本 | 制造业 | ✅ |
| 区域 | 文本 | 沈阳市 | ✅ |
| 区县 | 文本 | 和平区 | ✅ |
| 会内职位 | 会长/副会长/理事/会员 | 理事 | ✅ |
| 入会年份 | 数字 | 2020 | ✅ |
| 会费状态 | 在籍/未缴费 | 在籍 | ✅ |
| 所属企业 | 文本 | XX有限公司 | 可选 |
| 好人好事 | 数字 | 3 | 可选 |

## 部署方案

### 方案一：Vercel（推荐，免费且国内访问稳定）

1. 注册 [Vercel](https://vercel.com) 账号（可用 GitHub 登录）
2. 将 `shanghui-bi` 文件夹上传到 GitHub 仓库
3. 在 Vercel 导入该仓库，自动部署
4. 获得永久访问地址，如 `https://shanghui-bi.vercel.app`

**优点**：免费、自带 CDN、国内访问较快、支持自动部署

### 方案二：GitHub Pages（免费，国内访问不稳定）

1. 将文件推送到 GitHub 仓库
2. 仓库 Settings → Pages → Source: main 分支
3. 访问 `https://用户名.github.io/shanghui-bi/`

### 方案三：腾讯云/阿里云静态托管

1. 开通云服务商的静态网站托管服务
2. 上传 `index.html` 和数据文件（`members.csv` 或 `data.json`）
3. 绑定自定义域名

### 方案四：钉钉 H5 微应用嵌入

1. 登录 [钉钉开放平台](https://open.dingtalk.com)
2. 创建企业内部应用 → H5 微应用
3. 应用首页地址填写部署后的 URL（如 Vercel 地址）
4. 发布后企业成员可在钉钉工作台访问

**钉钉嵌入注意事项**：
- 建议使用 Vercel 或国内云服务部署，确保访问速度
- 钉钉内嵌浏览器对 CDN 资源加载可能有限制，确保 ECharts CDN 可访问
- 页面已做响应式适配，支持手机端浏览

## 数据自动更新流程（CSV 模式）

```
Excel/WPS 编辑 CSV → 保存 → 上传到服务器/GitHub → 看板自动刷新（60秒）→ 数据更新
```

**最简单的自动更新方案**：
1. 把 `members.csv` 放在 GitHub 仓库里
2. `DATA_SOURCE` 设为 GitHub raw 链接
3. 用手机/电脑在 GitHub 网页上直接编辑 CSV
4. 看板开启自动刷新，60 秒内自动拉取最新数据

## 技术栈

- 前端：HTML5 + CSS3 + Vanilla JavaScript
- 图表：Apache ECharts 5.5
- 地图：DataV.GeoAtlas 地理数据
- 数据：支持 JSON 和 CSV 双格式，无需数据库
- 托管：纯静态，支持任意静态服务器

## 浏览器兼容性

- Chrome / Edge 90+
- Safari 14+
- Firefox 88+
- 钉钉内嵌浏览器
- 微信内置浏览器
