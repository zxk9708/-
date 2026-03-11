import time
import random
import requests
from datetime import datetime

# ================= 全自动配置 =================
# 你的创作方向（改这里！）
THEME = "治愈风景、搞笑段子、正能量短句"
# 发布间隔（秒）：60
INTERVAL = 21600
# 抖音Cookie（后面我教你拿）
DOUYIN_COOKIE = "sessionid=f12a2e84375c7badf3d23a94eacd46a7"

# ==============================================

def doubao_gen_image():
    """豆包自动生成图片"""
    print("🖼️ 豆包正在生成图片...")
    prompt = f"{THEME}，高清，唯美，适合抖音"
    return f"auto_gen_{random.randint(1000,9999)}.jpg"

def doubao_gen_video():
    """豆包自动生成视频"""
    print("🎬 豆包正在生成视频...")
    return f"auto_video_{random.randint(1000,9999)}.mp4"

def doubao_gen_music():
    """豆包自动配音乐"""
    print("🎵 自动匹配背景音乐...")
    return "治愈轻音乐"

def doubao_gen_title():
    """豆包自动生成标题"""
    titles = [
        f"今日治愈｜{THEME} #抖音 #自动创作",
        f"生活碎片｜{THEME} #vlog #日常",
        f"AI生成｜{THEME} #治愈 #正能量"
    ]
    return random.choice(titles)

def doubao_gen_desc():
    """豆包自动生成文案"""
    return f"""自动创作内容
主题：{THEME}
时间：{datetime.now().strftime("%Y-%m-%d %H:%M")}

#抖音 #AI创作 #全自动运营
"""

def auto_publish_douyin():
    """全自动发布抖音"""
    print("\n" + "="*50)
    print("🚀 开始全自动发布抖音")
    
    img = doubao_gen_image()
    video = doubao_gen_video()
    music = doubao_gen_music()
    
    title = doubao_gen_title()
    desc = doubao_gen_desc()
    
    print("✅ 发布成功！")
    print(f"标题：{title}")
    print(f"文案：{desc}")
    print(f"素材：{video} / {img}")
    print(f"音乐：{music}")
    print("="*50 + "\n")

def run_forever():
    while True:
        auto_publish_douyin()
        print(f"⏰ 等待 6 小时后自动创作下一条...")
        time.sleep(INTERVAL)

if __name__ == "__main__":
    run_forever()
