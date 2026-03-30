#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
红书猎手 - Python 提取示例
RedBook Hunter - Python Extractor Example

使用方法：
1. 安装依赖: pip install requests pandas
2. 配置 Cookie 和参数
3. 运行: python python_extract.py
"""

import json
import csv
import urllib.parse
from datetime import datetime


def extract_kol_data():
    """
    示例：从本地文件或API提取KOL数据
    实际使用时需要替换为真实的API调用或页面解析
    """
    
    # 示例数据（实际使用时替换为真实数据）
    sample_data = [
        {
            "name": "橙橙子的家（软装中）",
            "location": "浙江 宁波 鄞州区",
            "followers": "9691",
            "avgViews": "4,504",
            "avgInteractions": "283",
            "price": "¥ 3,000起"
        },
        {
            "name": "小白小磊小天才",
            "location": "福建 厦门 湖里区",
            "followers": "66.4w",
            "avgViews": "957,158",
            "avgInteractions": "81,358",
            "price": "¥ 29,000起"
        }
    ]
    
    # 生成小红书搜索链接
    for item in sample_data:
        item['xhs_search_url'] = f"https://www.xiaohongshu.com/search_result?keyword={urllib.parse.quote(item['name'])}"
    
    return sample_data


def save_to_json(data, filename=None):
    """保存为 JSON 格式"""
    if not filename:
        filename = f"kol_data_{len(data)}_{datetime.now().strftime('%Y%m%d')}.json"
    
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    
    print(f"✅ JSON 文件已保存: {filename}")


def save_to_csv(data, filename=None):
    """保存为 CSV 格式"""
    if not filename:
        filename = f"kol_data_{len(data)}_{datetime.now().strftime('%Y%m%d')}.csv"
    
    if not data:
        return
    
    fieldnames = ['name', 'location', 'followers', 'avgViews', 'avgInteractions', 'price', 'xhs_search_url']
    
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)
    
    print(f"✅ CSV 文件已保存: {filename}")


def analyze_data(data):
    """简单的数据分析示例"""
    print(f"\n📊 数据分析:")
    print(f"- 总记录数: {len(data)}")
    print(f"- 有地域信息的: {sum(1 for d in data if d.get('location'))}")
    print(f"- 有报价信息的: {sum(1 for d in data if d.get('price'))}")


if __name__ == "__main__":
    print("🎯 红书猎手 - KOL 数据提取")
    print("-" * 40)
    
    # 提取数据
    data = extract_kol_data()
    
    # 保存文件
    save_to_json(data)
    save_to_csv(data)
    
    # 数据分析
    analyze_data(data)
    
    print("\n✨ 完成！")
