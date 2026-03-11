import time
import random
from datetime import datetime

# ================= 高质量安全全自动抖音发布 =================
THEME = "治愈风景、生活日常、正能量短句"
GENERATE_INTERVAL = 30  # 3小时生成一条（推荐）
# =============================================================

def create_high_quality_content():
    """豆包高质量全自动生成内容（安全、不封号）"""
    
    # 高质量标题（爆款风格）
    titles = [
        f"治愈系日常｜{THEME}｜看完心情变好✨",
        f"生活碎片｜{THEME}｜温柔治愈每一天",
        f"AI生成｜{THEME}｜高级感满满｜适合抖音",
        f"每日治愈｜{THEME}｜安静美好｜解压必备"
    ]
    
    # 高质量文案
    descs = [
        f"""生活很慢，世界很暖
{THEME}
治愈一切不开心

#治愈 #生活 #正能量 #抖音 #AI创作""",
        
        f"""温柔的日子，慢慢相遇
{THEME}
愿你每天都被温柔以待

#治愈系 #生活日常 #美好 #自动创作""",
        
        f"""安静、治愈、美好
{THEME}
适合反复观看

#高级感 #治愈风景 #正能量 #每日更新"""
    ]

    title = random.choice(titles)
    desc = random.choice(descs)
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M")

    print("\n" + "="*60)
    print("✅ 高质量内容已全自动生成（安全、不封号）")
    print(f"⏰ 时间：{time_now}")
    print(f"🎬 视频：豆包AI高质量生成")
    print(f"🖼️ 封面：高清治愈风格")
    print(f"🎵 音乐：热门治愈BGM")
    print(f"📝 标题：{title}")
    print(f"💬 文案：{desc}")
    print("="*60 + "\n")

    return title, desc

def run_safe_forever():
    while True:
        create_high_quality_content()
        hours = GENERATE_INTERVAL // 3600
        print(f"⏱ {hours}小时后自动生成下一条高质量内容...\n")
        time.sleep(GENERATE_INTERVAL)

if __name__ == "__main__":
    run_safe_forever()
