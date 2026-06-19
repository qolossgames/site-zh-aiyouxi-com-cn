import json
import sys
from datetime import datetime

SITE_DATA = {
    "site_name": "AI游戏资源站",
    "url": "https://site-zh-aiyouxi.com.cn",
    "keywords": ["爱游戏", "AI游戏", "游戏资源", "游戏资讯"],
    "tags": ["游戏", "资源", "AI"],
    "description": "提供丰富的AI游戏资源和最新游戏资讯，为玩家打造一站式游戏服务平台。"
}

def generate_summary(data: dict) -> str:
    """生成结构化的站点摘要"""
    lines = []
    lines.append("=" * 50)
    lines.append(f"站点摘要 - 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("=" * 50)
    lines.append(f"名称: {data.get('site_name', '未知')}")
    lines.append(f"URL: {data.get('url', '未知')}")
    lines.append(f"关键词: {', '.join(data.get('keywords', []))}")
    lines.append(f"标签: {', '.join(data.get('tags', []))}")
    lines.append(f"说明: {data.get('description', '无')}")
    lines.append("=" * 50)
    return "\n".join(lines)

def format_json_summary(data: dict) -> str:
    """返回JSON格式的摘要"""
    summary_obj = {
        "generated_at": datetime.now().isoformat(),
        "site_name": data.get("site_name"),
        "url": data.get("url"),
        "keywords": data.get("keywords"),
        "tags": data.get("tags"),
        "description": data.get("description")
    }
    return json.dumps(summary_obj, ensure_ascii=False, indent=2)

def main():
    print("=== 生成站点摘要 ===")
    text_summary = generate_summary(SITE_DATA)
    print(text_summary)
    print("\n=== JSON格式摘要 ===")
    print(format_json_summary(SITE_DATA))

if __name__ == "__main__":
    main()