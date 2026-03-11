import random
from datetime import datetime

# 主题
THEME = "治愈风景、生活日常、正能量短句"

def 生成内容():
    # 标题
    标题列表 = [
        f"治愈系日常｜{THEME}｜看完心情变好✨",
        f"生活碎片｜{THEME}｜温柔治愈每一天",
        f"AI生成｜{THEME}｜高级感满满｜适合抖音",
        f"每日治愈｜{THEME}｜安静美好｜解压必备"
    ]

    # 文案
    文案列表 = [
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

    标题 = random.choice(标题列表)
    文案 = random.choice(文案列表)
    时间 = datetime.now().strftime("%Y-%m-%d %H:%M")

    最终内容 = f"""
【{时间} 自动生成】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 标题：
{标题}

💬 文案：
{文案}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

    # 保存到 output.txt
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write(最终内容)

    print("✅ 生成完成！output.txt 已更新")

# 运行一次
if __name__ == "__main__":
    生成内容()
