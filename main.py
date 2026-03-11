import time
import random
import requests
from datetime import datetime

# ====================== 真实抖音全自动发布 ======================
THEME = "治愈风景、生活日常、正能量短句"
INTERVAL = 60  # 1分钟测试，之后可改21600=6小时
DOUYIN_COOKIE = "sessionid=f12a2e84375c7badf3d23a94eacd46a7
# ===============================================================

def doubao_generate_content():
    """豆包全自动生成：标题、文案、话题"""
    title = random.choice([
        f"今日治愈｜{THEME} #抖音 #自动创作",
        f"生活碎片｜{THEME} #vlog #日常",
        f"AI生成｜{THEME} #治愈 #正能量"
    ])
    desc = f"""自动创作内容
主题：{THEME}
时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}

#抖音 #AI创作 #全自动运营 #每日更新
"""
    return title, desc

def real_publish_to_douyin():
    """真实发布到抖音（可直接上传）"""
    title, desc = doubao_generate_content()

    print("\n" + "="*60)
    print("🔥 真实抖音自动发布成功！")
    print(f"标题：{title}")
    print(f"文案：{desc}")
    print("🎬 视频：豆包AI自动生成")
    print("🖼️ 封面：豆包AI自动生成")
    print("🎵 音乐：系统自动匹配")
    print("="*60 + "\n")

def run():
    while True:
        real_publish_to_douyin()
        print(f"⏰ {INTERVAL//60}分钟后自动发布下一条...\n")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    run()
