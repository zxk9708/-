import random
from datetime import datetime

# ================= 配置 =================
THEME = "治愈风景、生活日常、正能量短句"
# ========================================

def create_high_quality_content():
    """高质量安全内容生成"""
    
    titles = [
        f"治愈系日常｜{THEME}｜看完心情变好✨",
        f"生活碎片｜{THEME}｜温柔治愈每一天",
        f"AI生成｜{THEME}｜高级感满满｜适合抖音",
        f"每日治愈｜{THEME}｜安静美好｜解压必备"
    ]
    
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

    # 生成内容并保存到 output.txt
    result = f"""
【{time_now} 全自动生成】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🎬 视频：治愈风景 / 生活日常
🖼️ 封面：高清治愈风格
🎵 音乐：热门治愈BGM
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 标题：
{title}

💬 文案：
{desc}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(result)

    print("✅ 内容已生成 → output.txt")

# 主程序（只运行一次）
if __name__ == "__main__":
    create_high_quality_content()
