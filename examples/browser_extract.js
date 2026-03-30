/**
 * 红书猎手 - 浏览器控制台提取脚本
 * RedBook Hunter - Browser Console Extractor
 * 
 * 使用方法：
 * 1. 登录小红书蒲公英平台 https://pgy.xiaohongshu.com
 * 2. 进入 KOL 列表页
 * 3. 按 F12 打开开发者工具 → Console
 * 4. 复制本代码粘贴运行
 * 5. 数据自动下载为 JSON 文件
 */

const extractKOL = () => {
  const rows = document.querySelectorAll('table tbody tr');
  const data = [];
  
  rows.forEach(row => {
    const cells = row.querySelectorAll('td');
    if (cells.length >= 6) {
      const nameEl = cells[0].querySelector('.name, [class*="name"], a, span');
      const name = nameEl ? nameEl.textContent.trim() : cells[0].textContent.trim().split('\n')[0];
      
      const locationMatch = cells[0].textContent.match(/([\u4e00-\u9fa5]{2,3}\s+[\u4e00-\u9fa5]{2,3}(?:\s+[\u4e00-\u9fa5]{2,3})?)/);
      const location = locationMatch ? locationMatch[1].replace(/\s+/g, ' ') : '';
      
      const followers = cells[2] ? cells[2].textContent.trim() : '';
      const avgViews = cells[3] ? cells[3].textContent.trim() : '';
      const avgInteractions = cells[4] ? cells[4].textContent.trim() : '';
      const price = cells[5] ? cells[5].textContent.trim() : '';
      
      if (name && followers) {
        data.push({
          name: name,
          location: location,
          followers: followers,
          avgViews: avgViews,
          avgInteractions: avgInteractions,
          price: price,
          xhs_search_url: 'https://www.xiaohongshu.com/search_result?keyword=' + encodeURIComponent(name)
        });
      }
    }
  });
  
  // 下载数据
  const blob = new Blob([JSON.stringify(data, null, 2)], {type: 'application/json'});
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = `kol_data_${data.length}_${new Date().toISOString().split('T')[0]}.json`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
  
  console.log(`✅ 成功提取 ${data.length} 条 KOL 数据`);
  console.log('📊 数据预览：', data.slice(0, 3));
  
  return data;
};

// 执行提取
extractKOL();
