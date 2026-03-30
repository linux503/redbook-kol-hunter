# 红书猎手 (RedBook Hunter)

> **精准捕获小红书达人**
> 
> *让优质KOL无处遁形*

[![GitHub stars](https://img.shields.io/github/stars/yourusername/redbook-hunter?style=social)](https://github.com/yourusername/redbook-hunter)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 🎯 简介

红书猎手是一款开源的小红书蒲公英 KOL 智能采集工具，帮助品牌方和代理商快速筛选优质达人。

**核心优势：**
- ⚡ 1分钟提取100条KOL数据
- 🎯 精准采集粉丝数、互动率、报价等核心数据
- 📊 支持 JSON/CSV/Markdown 三格式导出
- 🔗 自动生成小红书搜索链接

## 🚀 快速开始

### 方式一：浏览器控制台（最简单）

```javascript
// 复制以下代码到浏览器控制台运行
const extractKOL = () => {
  const rows = document.querySelectorAll('table tbody tr');
  const data = [];
  
  rows.forEach(row => {
    const cells = row.querySelectorAll('td');
    if (cells.length >= 6) {
      data.push({
        name: cells[0].textContent.trim().split('\n')[0],
        location: cells[0].textContent.match(/[\u4e00-\u9fa5]{2,3}\s+[\u4e00-\u9fa5]{2,3}/)?.[0] || '',
        followers: cells[2].textContent.trim(),
        avgViews: cells[3].textContent.trim(),
        avgInteractions: cells[4].textContent.trim(),
        price: cells[5].textContent.trim()
      });
    }
  });
  
  // 下载数据
  const blob = new Blob([JSON.stringify(data, null, 2)], {type: 'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `kol_data_${data.length}.json`;
  a.click();
  
  return data;
};

extractKOL();
```

### 方式二：Python 脚本

```bash
# 安装依赖
pip install requests pandas

# 运行提取脚本
python extract_kol_data.py

# 查看结果
cat data/kol_data.json
```

## 📊 数据结构

```json
{
  "name": "橙橙子的家（软装中）",
  "location": "浙江 宁波 鄞州区",
  "followers": "9691",
  "avgViews": "4,504",
  "avgInteractions": "283",
  "price": "¥ 3,000起",
  "xhs_search_url": "https://www.xiaohongshu.com/search_result?keyword=..."
}
```

## 💡 使用场景

- **品牌方找达人**：新品上市，批量筛选合作KOL
- **代理商选号**：为客户匹配最合适的达人资源
- **竞品分析**：分析竞品合作的KOL画像
- **数据研究**：小红书达人市场趋势分析

## 📁 项目结构

```
redbook-hunter/
├── 📄 README.md              # 本文件
├── 📄 LICENSE                # MIT 许可证
├── 🖥️ index.html             # 官网
├── 📁 examples/              # 示例代码
│   ├── browser_extract.js    # 浏览器控制台脚本
│   └── python_extract.py     # Python 提取示例
└── 📁 docs/                  # 文档
    └── API.md                # API 文档
```

## 🔧 高级功能

完整版包含更多高级功能：

- ✅ 批量翻页采集（支持20-400+条）
- ✅ 断点续传，中断后可继续
- ✅ Tampermonkey 插件支持
- ✅ Playwright 自动化采集
- ✅ 数据分析和统计报告
- ✅ 多格式导出（JSON/CSV/Markdown）

> 💼 **企业版/完整版**：如需完整功能，请联系获取

## ⚠️ 免责声明

本工具仅供学习研究使用，请遵守小红书平台规则，不得用于非法用途。

## 📄 License

MIT License © 2026 RedBook Hunter

---

**让优质KOL无处遁形** 🎯

[🌐 官网](https://yourusername.github.io/redbook-hunter) | [💻 GitHub](https://github.com/yourusername/redbook-hunter)
