import os
import requests
from urllib.parse import urlparse

# 定义资源映射表（根据源码分析出的真实链接）
ASSET_MAP = {
    "banners": [
        "https://fs.img4399.com/ma/1554_230111133815_qn2F.png", # 默认池
        "https://fs.img4399.com/bbs/202604/6/2026001010964/4FHqSQOejw.1080x533.jpg" # 活动池
    ],
    "buttons": [
        "https://m.img4399.com/rds/release/maintain/game/genshinLottery/static/img/btn_1.png", # 假设路径
        "https://m.img4399.com/rds/release/maintain/game/genshinLottery/static/img/btn_10.png"
    ]
}

def sync_assets():
    base_path = "assets/genshin"
    for category, urls in ASSET_MAP.items():
        dir_path = f"{base_path}/{category}"
        os.makedirs(dir_path, exist_ok=True)
        
        for url in urls:
            # 自动提取文件名并保存
            filename = os.path.basename(urlparse(url).path)
            save_path = os.path.join(dir_path, filename)
            
            if not os.path.exists(save_path):
                print(f"正在同步: {category}/{filename}")
                res = requests.get(url, timeout=10)
                with open(save_path, "wb") as f:
                    f.write(res.content)
    print("✨ 资源同步完成！")

if __name__ == "__main__":
    sync_assets()
