#!/usr/bin/env python3
"""黄师傅 · 科学与人文 网站生成器"""
import json, os, sys

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

# Load TR35 data for science section
tr35_path = os.path.join(os.path.dirname(SITE_DIR), 'deeptech-website', 'tr35_data.json')
scientists = []
if os.path.exists(tr35_path):
    with open(tr35_path, 'r', encoding='utf-8') as f:
        scientists = json.load(f)

photo_count = sum(1 for s in scientists if s.get('photo'))

# 游学目的地数据
tours = [
    {"year": "2025", "dest": "不丹", "teacher": "曹蕴 / 胡赳赳", "tagline": "世上最幸福的国度", "img": "img/不丹（第一程）ai-01.jpg"},
    {"year": "2025", "dest": "香格里拉", "teacher": "雪虎 / 扎巴格丹", "tagline": "寻梦香巴拉", "img": "img/香巴拉-胡赳赳.jpg"},
    {"year": "2025", "dest": "尼泊尔", "teacher": "胡赳赳", "tagline": "喜马拉雅山脚下的生命课堂", "img": "img/不丹（第一程）ai-01.jpg"},
    {"year": "2025", "dest": "土耳其", "teacher": "雪虎", "tagline": "东西文明交汇", "img": "img/姜鹏-修心之旅_封面.jpg"},
    {"year": "2025", "dest": "日本", "teacher": "胡赳赳", "tagline": "禅修与美学", "img": "img/胡赳赳-日本（定）-10.jpg"},
    {"year": "2024", "dest": "德国", "teacher": "", "tagline": "哲学与音乐之旅", "img": "img/德国游学-定0912-05.jpg"},
    {"year": "2024", "dest": "尼泊尔", "teacher": "胡赳赳", "tagline": "生命哲学高研班", "img": "img/姜鹏-修心之旅_封面.jpg"},
    {"year": "2024", "dest": "香格里拉", "teacher": "胡赳赳 / 扎巴格丹", "tagline": "寻梦香巴拉首发", "img": "img/香巴拉-胡赳赳.jpg"},
    {"year": "2023", "dest": "夏威夷", "teacher": "", "tagline": "太平洋上的思想碰撞", "img": "img/德国游学-定0912-05.jpg"},
    {"year": "2023", "dest": "德国", "teacher": "", "tagline": "欧洲文化寻根", "img": "img/德国游学-定0912-05.jpg"},
    {"year": "2022", "dest": "敦煌", "teacher": "", "tagline": "丝路文明探源", "img": "img/姜鹏-修心之旅_封面.jpg"},
    {"year": "2022", "dest": "香格里拉", "teacher": "吴思", "tagline": "修心之旅", "img": "img/姜鹏-修心之旅_封面.jpg"},
]

# 思想食堂师资
teachers = [
    {"name": "吴思", "topic": "血酬史观", "note": "《血酬定律》作者"},
    {"name": "费勇", "topic": "禅与生活方式", "note": "暨南大学教授"},
    {"name": "胡赳赳", "topic": "修心之旅", "note": "文化学者·「赳赳说」主理人"},
    {"name": "余世存", "topic": "易经/金刚经", "note": "文化学者"},
    {"name": "吴晓波", "topic": "历代经济变革得失", "note": "财经作家"},
    {"name": "雷颐", "topic": "中国近现代史", "note": "中国社科院研究员"},
    {"name": "姜鹏", "topic": "家族传承", "note": "复旦大学历史系"},
    {"name": "包刚升", "topic": "解读美国政治传统", "note": "复旦大学"},
    {"name": "韦森", "topic": "大转型中的中国经济", "note": "复旦大学经济学院"},
    {"name": "周国平", "topic": "企业家与哲学", "note": "哲学家·作家"},
    {"name": "毕飞宇", "topic": "水浒与红楼", "note": "作家·茅盾文学奖得主"},
    {"name": "孙立平", "topic": "经济困境与社会转型", "note": "清华大学社会学系"},
    {"name": "秦朔", "topic": "中国企业战略创新", "note": "秦朔朋友圈创始人"},
    {"name": "陈立", "topic": "音乐的力量", "note": "浙江大学心理学教授"},
    {"name": "田艺苗", "topic": "古典音乐鉴赏", "note": "音乐学者"},
    {"name": "于赓哲", "topic": "唐朝", "note": "陕西师范大学"},
    {"name": "罗新", "topic": "游牧民族与中国历史", "note": "北京大学历史学系"},
    {"name": "傅佩荣", "topic": "哲学与人生", "note": "台湾大学哲学系"},
    {"name": "张宏杰", "topic": "解读曾国藩", "note": "中国人民大学"},
    {"name": "曹蕴", "topic": "生命哲学", "note": "修行导师"},
]

# 黄师傅原创文章
articles = [
    {"title": "寻梦香巴拉", "type": "游记", "excerpt": "哲学家说，每个人都有三个我。香格里拉，一定是那个让你看到天使的地方。一个用藏刀砍竹子的康巴汉子，正在等待10位来自远方的朋友…"},
    {"title": "生命的讯息", "type": "毕业旅行记", "excerpt": "南迦巴瓦雪山，被《国家地理》杂志誉为世界上最美的雪山。一个人需要隐藏多少秘密，才能巧妙地度过一生…"},
    {"title": "理想三旬", "type": "个人叙事", "excerpt": "4年前的今天，我决定离开全心全意耕耘3年之久的公司。三十而立，即将只身离家南下，这一去尚不知前途，只知断不能回头…"},
    {"title": "益西故事", "type": "人物特写", "excerpt": "在喜马拉雅山脚下，他用爱点亮400多个孩子的未来。一个康巴汉子的传奇人生…"},
    {"title": "游学不丹", "type": "游学笔记", "excerpt": "走进世界上最幸福的国度，探究生命的终极意义…"},
    {"title": "聂圣哲：从思想回到常识", "type": "人物访谈", "excerpt": "一个有思想的企业家，如何在商业世界保持清醒…"},
]

# 非常深科技 视频号数据
video_channel = {
    "name": "非常深科技",
    "tagline": "走进中国最前沿的科学现场",
    "features": [
        "TR35 科学家深度访谈",
        "大科学装置现场探访",
        "前沿科技产业解读",
    ],
    "locations": ["怀柔科学城", "合肥科学城", "上海科学城", "杭州/深圳"],
}

# 深科技内参
neican = {
    "name": "深科技内参",
    "tagline": "52 周深科技趋势洞察",
    "description": "每周一份深度报告，覆盖 AI、半导体、生命科学、新材料等关键领域。基于 MIT Technology Review 全球编辑网络的第一手信息，让你始终站在信息链顶端。"
}

def build():
    tours_json = json.dumps(tours, ensure_ascii=False)
    teachers_json = json.dumps(teachers, ensure_ascii=False)
    articles_json = json.dumps(articles, ensure_ascii=False)
    scientists_json = json.dumps(scientists, ensure_ascii=False)

    html = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>黄师傅 · 科学与人文</title>
<meta name="description" content="黄师傅的科学与人文——思想食堂十年人文游学 + DeepTech+ 企业家科学社区">
<style>
  :root {{
    --ink: #1a1a1a;
    --ink-light: #3d3d3d;
    --ink-muted: #888;
    --paper: #fafaf7;
    --paper-dark: #f0ede5;
    --accent: #b8352c;
    --accent-light: #d46353;
    --accent-warm: #c8960c;
    --science-blue: #1a3a5c;
    --science-light: #2d5a8e;
    --white: #ffffff;
    --border: #e5e0d8;
    --shadow: 0 1px 4px rgba(0,0,0,0.06);
    --shadow-md: 0 4px 20px rgba(0,0,0,0.08);
    --shadow-lg: 0 8px 40px rgba(0,0,0,0.1);
    --radius: 8px;
    --radius-lg: 16px;
    --font-cn: "PingFang SC", "Noto Serif SC", "Source Han Serif SC", "STSong", "SimSun", serif;
    --font-sans: "PingFang SC", "Microsoft YaHei", -apple-system, sans-serif;
    --font-display: "PingFang SC", "Noto Serif SC", "STKaiti", "KaiTi", serif;
  }}

  * {{ margin:0; padding:0; box-sizing:border-box; }}

  body {{
    font-family: var(--font-cn);
    background: var(--paper);
    color: var(--ink);
    line-height: 1.8;
    -webkit-font-smoothing: antialiased;
  }}

  /* ── Navigation ── */
  .nav {{
    position: fixed; top: 0; left: 0; right: 0; z-index: 1000;
    background: rgba(250,250,247,0.94);
    backdrop-filter: blur(16px);
    border-bottom: 1px solid var(--border);
    padding: 0 2rem;
  }}
  .nav-inner {{
    max-width: 1280px; margin: 0 auto;
    display: flex; align-items: center; justify-content: space-between;
    height: 64px;
  }}
  .nav-brand {{
    font-family: var(--font-display);
    font-size: 1.3rem; font-weight: 700;
    color: var(--ink); text-decoration: none;
    letter-spacing: 0.04em;
  }}
  .nav-brand span {{ color: var(--accent); }}
  .nav-links {{ display: flex; gap: 2.2rem; list-style: none; align-items: center; }}
  .nav-links a {{
    color: var(--ink-light); text-decoration: none;
    font-size: 0.9rem; font-family: var(--font-sans);
    transition: color 0.2s;
  }}
  .nav-links a:hover {{ color: var(--accent); }}
  .nav-divider {{ width: 1px; height: 18px; background: var(--border); }}

  /* ── Hero ── */
  .hero {{
    padding: 120px 2rem 80px;
    text-align: center;
    position: relative;
    overflow: hidden;
  }}
  .hero::before {{
    content: ''; position: absolute;
    top: -300px; left: 50%; transform: translateX(-50%);
    width: 1000px; height: 1000px;
    background: radial-gradient(ellipse, rgba(184,53,44,0.03) 0%, transparent 60%),
                radial-gradient(ellipse at 70% 60%, rgba(26,58,92,0.02) 0%, transparent 60%);
    pointer-events: none;
  }}
  .hero-eyebrow {{
    font-family: var(--font-sans);
    font-size: 0.85rem; letter-spacing: 0.18em;
    color: var(--ink-muted); margin-bottom: 1.5rem;
    text-transform: uppercase;
  }}
  .hero h1 {{
    font-family: var(--font-display);
    font-size: clamp(2.4rem, 5vw, 4rem);
    font-weight: 800; line-height: 1.25;
    position: relative; margin-bottom: 1.5rem;
  }}
  .hero h1 .dot {{
    display: inline-block; color: var(--accent);
    font-size: 1em; margin: 0 0.15em;
  }}
  .hero-subtitle {{
    font-size: 1.15rem; color: var(--ink-muted);
    max-width: 520px; margin: 0 auto 2.5rem;
    line-height: 1.9;
  }}
  .hero-pillars {{
    display: flex; justify-content: center; gap: 2rem;
    margin-top: 2rem;
  }}
  .pillar {{
    text-decoration: none; color: inherit;
    background: var(--white);
    padding: 1.4rem 2.2rem;
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow-md);
    border: 1px solid var(--border);
    transition: all 0.3s;
    text-align: center;
    min-width: 180px;
  }}
  .pillar:hover {{ transform: translateY(-3px); box-shadow: var(--shadow-lg); }}
  .pillar.humanities:hover {{ border-color: var(--accent); }}
  .pillar.science:hover {{ border-color: var(--science-blue); }}
  .pillar-emoji {{ font-size: 2.2rem; margin-bottom: 0.5rem; }}
  .pillar-label {{
    font-family: var(--font-display);
    font-size: 1.25rem; font-weight: 700;
    margin-bottom: 0.3rem;
  }}
  .pillar-desc {{ font-size: 0.85rem; color: var(--ink-muted); font-family: var(--font-sans); }}

  /* ── Sections ── */
  section {{ padding: 6rem 2rem; }}
  section.alt {{ background: var(--white); }}
  section.dark {{ background: var(--ink); color: var(--white); }}
  .sec-inner {{ max-width: 1280px; margin: 0 auto; }}

  .sec-header {{
    text-align: center; margin-bottom: 4rem;
  }}
  .sec-tag {{
    font-family: var(--font-sans);
    display: inline-block; font-size: 0.78rem; font-weight: 600;
    letter-spacing: 0.14em; color: var(--accent);
    text-transform: uppercase; margin-bottom: 1rem;
  }}
  .sec-title {{
    font-family: var(--font-display);
    font-size: 2.2rem; font-weight: 800;
    margin-bottom: 1rem; line-height: 1.35;
  }}
  .sec-subtitle {{
    font-size: 1rem; color: var(--ink-muted);
    max-width: 600px; margin: 0 auto;
    font-family: var(--font-sans);
  }}
  section.dark .sec-subtitle {{ color: rgba(255,255,255,0.55); }}

  /* ── Division Banner ── */
  .division {{
    text-align: center; padding: 3rem 2rem;
    background: linear-gradient(180deg, var(--paper) 0%, var(--paper-dark) 50%, var(--paper) 100%);
  }}
  .division-line {{
    display: flex; align-items: center; justify-content: center;
    gap: 2rem; max-width: 600px; margin: 0 auto;
  }}
  .division-line .dl {{ flex: 1; height: 1px; background: var(--border); }}
  .division-symbol {{ font-size: 1.6rem; color: var(--accent); }}

  /* ── Tour Timeline ── */
  .tour-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
    gap: 1.2rem;
  }}
  .tour-card {{
    background: var(--white);
    border-radius: var(--radius-lg);
    overflow: hidden;
    box-shadow: var(--shadow);
    border: 1px solid var(--border);
    transition: all 0.3s;
  }}
  .tour-card:hover {{ transform: translateY(-2px); box-shadow: var(--shadow-md); }}
  .tour-img {{
    height: 180px; background: var(--paper-dark);
    background-size: cover; background-position: center;
    position: relative;
  }}
  .tour-img .tour-year {{
    position: absolute; top: 12px; right: 12px;
    background: var(--accent); color: var(--white);
    padding: 0.2rem 0.7rem; border-radius: 4px;
    font-family: var(--font-sans);
    font-size: 0.75rem; font-weight: 700;
  }}
  .tour-body {{ padding: 1.2rem; }}
  .tour-dest {{
    font-family: var(--font-display);
    font-size: 1.15rem; font-weight: 700;
    margin-bottom: 0.3rem;
  }}
  .tour-teacher {{
    font-size: 0.82rem; color: var(--accent);
    margin-bottom: 0.4rem; font-family: var(--font-sans);
  }}
  .tour-tagline {{ font-size: 0.85rem; color: var(--ink-muted); line-height: 1.6; }}

  /* ── Teacher Cloud ── */
  .teacher-cloud {{
    display: flex; flex-wrap: wrap; gap: 0.7rem;
    justify-content: center; margin-bottom: 2rem;
  }}
  .teacher-chip {{
    background: var(--white); border: 1px solid var(--border);
    padding: 0.55rem 1.2rem; border-radius: 24px;
    font-size: 0.9rem; font-family: var(--font-sans);
    transition: all 0.2s; cursor: default;
    display: flex; align-items: center; gap: 0.5rem;
  }}
  .teacher-chip:hover {{ border-color: var(--accent); background: #fef9f8; }}
  .teacher-chip .tc-name {{ font-weight: 600; }}
  .teacher-chip .tc-topic {{
    font-size: 0.78rem; color: var(--ink-muted);
  }}

  /* ── Article Cards ── */
  .article-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
    gap: 1.5rem;
  }}
  .article-card {{
    background: var(--white);
    border-radius: var(--radius-lg);
    padding: 2rem;
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
    transition: all 0.2s;
  }}
  .article-card:hover {{ box-shadow: var(--shadow-md); }}
  .article-type {{
    font-family: var(--font-sans);
    font-size: 0.72rem; letter-spacing: 0.1em;
    color: var(--accent); text-transform: uppercase;
    margin-bottom: 0.8rem; font-weight: 600;
  }}
  .article-title {{
    font-family: var(--font-display);
    font-size: 1.2rem; font-weight: 700;
    margin-bottom: 0.8rem; line-height: 1.4;
  }}
  .article-excerpt {{
    font-size: 0.92rem; color: var(--ink-light);
    line-height: 1.8; display: -webkit-box;
    -webkit-line-clamp: 4; -webkit-box-orient: vertical;
    overflow: hidden;
  }}

  /* ── Decade Stats ── */
  .decade-stats {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem; margin-top: 3rem;
  }}
  .decade-stat {{
    text-align: center; padding: 2rem 1.5rem;
    background: var(--white);
    border-radius: var(--radius-lg);
    box-shadow: var(--shadow);
    border: 1px solid var(--border);
  }}
  .decade-stat .num {{
    font-family: var(--font-display);
    font-size: 3rem; font-weight: 900;
    color: var(--accent); line-height: 1.1;
  }}
  .decade-stat .label {{
    font-size: 0.92rem; color: var(--ink-muted);
    margin-top: 0.5rem; font-family: var(--font-sans);
  }}

  /* ── Science Section ── */
  .sci-cards {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(350px, 1fr));
    gap: 1.5rem;
  }}
  .sci-card {{
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.12);
    border-radius: var(--radius-lg);
    padding: 2rem;
    transition: all 0.3s;
  }}
  .sci-card:hover {{ background: rgba(255,255,255,0.1); }}
  .sci-card .sci-emoji {{ font-size: 2.5rem; margin-bottom: 1rem; }}
  .sci-card h3 {{
    font-family: var(--font-display);
    font-size: 1.3rem; margin-bottom: 0.8rem;
    color: var(--white);
  }}
  .sci-card p {{
    font-size: 0.92rem; color: rgba(255,255,255,0.6);
    line-height: 1.7; font-family: var(--font-sans);
  }}
  .sci-card .sci-stat {{
    font-family: var(--font-display);
    font-size: 2.2rem; font-weight: 900;
    color: var(--accent-warm); margin-top: 1rem;
  }}

  /* ── Video Channel ── */
  .video-features {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 1.5rem;
    margin-bottom: 2rem;
  }}
  .vf-card {{
    background: var(--white);
    border: 1px solid var(--border);
    border-radius: var(--radius-lg);
    padding: 2rem; text-align: center;
    box-shadow: var(--shadow);
  }}
  .vf-card .vf-icon {{ font-size: 2.2rem; margin-bottom: 1rem; }}
  .vf-card h4 {{
    font-family: var(--font-display);
    font-size: 1.1rem; font-weight: 700;
    margin-bottom: 0.5rem;
  }}
  .vf-card p {{ font-size: 0.85rem; color: var(--ink-muted); font-family: var(--font-sans); }}

  .location-tags {{
    display: flex; flex-wrap: wrap; gap: 0.6rem;
    justify-content: center;
  }}
  .loc-tag {{
    padding: 0.45rem 1.2rem; border-radius: 20px;
    background: var(--science-blue); color: var(--white);
    font-family: var(--font-sans); font-size: 0.88rem;
    font-weight: 500;
  }}

  /* ── TR35 mini cards ── */
  .tr35-mini {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
    gap: 0.8rem;
    margin-top: 2rem;
  }}
  .tm-card {{
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: var(--radius);
    padding: 1rem 1.2rem;
    display: flex; align-items: center; gap: 0.8rem;
  }}
  .tm-avatar {{
    flex-shrink: 0; width: 40px; height: 40px; border-radius: 50%;
    display: flex; align-items: center; justify-content: center;
    font-family: var(--font-sans); font-weight: 700; font-size: 0.85rem;
    color: var(--white);
  }}
  .tm-info {{ flex: 1; min-width: 0; }}
  .tm-name {{ font-size: 0.9rem; font-weight: 600; color: var(--white); }}
  .tm-domain {{ font-size: 0.72rem; color: rgba(255,255,255,0.5); }}

  /* ── Combined Quote ── */
  .quote-block {{
    max-width: 700px; margin: 3rem auto 0;
    text-align: center; padding: 2.5rem 2rem;
    background: var(--paper-dark);
    border-radius: var(--radius-lg);
    position: relative;
  }}
  .quote-block .q-mark {{
    font-size: 4rem; color: var(--accent);
    opacity: 0.15; position: absolute; top: -10px; left: 20px;
    font-family: Georgia, serif; line-height: 1;
  }}
  .quote-block .q-text {{
    font-family: var(--font-display);
    font-size: 1.2rem; line-height: 2;
    color: var(--ink-light); font-style: italic;
  }}
  .quote-block .q-author {{
    font-size: 0.88rem; color: var(--accent);
    margin-top: 1rem; font-weight: 600;
  }}

  /* ── CTA ── */
  .cta-section {{
    text-align: center; padding: 5rem 2rem;
    background: linear-gradient(135deg, var(--ink) 0%, #2a2020 100%);
    color: var(--white);
  }}
  .cta-section .cta-title {{
    font-family: var(--font-display);
    font-size: 2rem; font-weight: 800; margin-bottom: 1rem;
  }}
  .cta-section .cta-desc {{
    font-size: 1rem; color: rgba(255,255,255,0.6);
    max-width: 500px; margin: 0 auto 2rem;
    font-family: var(--font-sans);
  }}
  .cta-section .cta-note {{
    font-size: 0.82rem; color: rgba(255,255,255,0.35);
    margin-top: 2rem; font-family: var(--font-sans);
  }}
  .btn-cta {{
    display: inline-block;
    background: var(--accent); color: var(--white);
    padding: 1rem 2.5rem; border-radius: 10px;
    text-decoration: none; font-size: 1.05rem;
    font-weight: 700; font-family: var(--font-sans);
    transition: all 0.2s;
  }}
  .btn-cta:hover {{ background: var(--accent-light); transform: translateY(-1px); }}

  footer {{
    padding: 3rem 2rem; text-align: center;
    background: var(--ink); color: rgba(255,255,255,0.35);
    font-family: var(--font-sans); font-size: 0.85rem;
  }}
  footer .f-line {{ margin-bottom: 0.5rem; }}

  @media (max-width: 768px) {{
    .hero h1 {{ font-size: 2rem; }}
    .hero-pillars {{ flex-direction: column; gap: 1rem; align-items: stretch; }}
    .nav-links {{ display: none; }}
    .sec-title {{ font-size: 1.6rem; }}
    .article-grid {{ grid-template-columns: 1fr; }}
    .sci-cards {{ grid-template-columns: 1fr; }}
    .tour-grid {{ grid-template-columns: 1fr; }}
    .decade-stats {{ grid-template-columns: repeat(2, 1fr); }}
    .tr35-mini {{ grid-template-columns: repeat(auto-fill, minmax(200px, 1fr)); }}
  }}
</style>
</head>
<body>

<nav class="nav">
  <div class="nav-inner">
    <a href="#" class="nav-brand">黄师傅<span>·</span>科学与人文</a>
    <ul class="nav-links">
      <li><a href="#humanities">人文</a></li>
      <li class="nav-divider"></li>
      <li><a href="#science">科技</a></li>
      <li class="nav-divider"></li>
      <li><a href="#cta">联系</a></li>
    </ul>
  </div>
</nav>

<!-- ═══════════ HERO ═══════════ -->
<section class="hero">
  <div class="hero-eyebrow">Science <span class="dot">·</span> Humanities</div>
  <h1>用人文滋养灵魂<span class="dot">·</span>以科技洞见未来</h1>
  <p class="hero-subtitle">
    思想食堂十年人文游学实践，融合 DeepTech+ 前沿科技社区——让每一位企业家在文明的回响中找到方向，在科学的浪尖上看见未来。
  </p>
  <div class="hero-pillars">
    <a href="#humanities" class="pillar humanities">
      <div class="pillar-emoji">🏛️</div>
      <div class="pillar-label">人文</div>
      <div class="pillar-desc">思想食堂 · 十年游学<br>师者问道 · 生命修行</div>
    </a>
    <a href="#science" class="pillar science">
      <div class="pillar-emoji">🔬</div>
      <div class="pillar-label">科技</div>
      <div class="pillar-desc">DeepTech+ 科学社区<br>TR35 科学家 · 前沿洞察</div>
    </a>
  </div>
</section>

<!-- ═══════════ 人文板块 ═══════════ -->
<section id="humanities">
  <div class="sec-inner">
    <div class="sec-header">
      <div class="sec-tag">Humanities</div>
      <h2 class="sec-title">思想食堂：中国高端人文旅课品牌</h2>
      <p class="sec-subtitle">自 2017 年起，汇聚中国最优秀的人文学者，带领超过 10,000 名学员走向世界。在行走中对话先贤，在旅途中关照内心。</p>
    </div>

    <!-- 品牌理念 -->
    <div class="quote-block">
      <div class="q-mark">"</div>
      <div class="q-text">15岁上大学；29岁当教授；35岁当博导；50岁下海，用商业布道。<br>费勇老师说：可以做任何你想做的；但不可以要任何你想要的。</div>
      <div class="q-author">—— 黄师傅 · 十年手记</div>
    </div>

    <!-- 十年战绩 -->
    <div class="decade-stats">
      <div class="decade-stat"><div class="num">10+</div><div class="label">年品牌沉淀</div></div>
      <div class="decade-stat"><div class="num">60+</div><div class="label">位人文学者</div></div>
      <div class="decade-stat"><div class="num">30+</div><div class="label">次全球游学</div></div>
      <div class="decade-stat"><div class="num">1,071</div><div class="label">篇朋友圈实录</div></div>
      <div class="decade-stat"><div class="num">20+</div><div class="label">个目的地国家</div></div>
    </div>
  </div>
</section>

<!-- 游学履历 -->
<section class="alt">
  <div class="sec-inner">
    <div class="sec-header">
      <div class="sec-tag">Study Tours</div>
      <h2 class="sec-title">游学履历</h2>
      <p class="sec-subtitle">行万里路，读万卷书。每一次旅程都是一场跨越时空的对话。</p>
    </div>
    <div class="tour-grid" id="tourGrid"></div>
  </div>
</section>

<!-- 师者风采 -->
<section>
  <div class="sec-inner">
    <div class="sec-header">
      <div class="sec-tag">Teachers</div>
      <h2 class="sec-title">师者风采</h2>
      <p class="sec-subtitle">思想食堂汇聚中国最优秀的人文学者，横跨历史、哲学、经济、音乐、文学等学科。</p>
    </div>
    <div class="teacher-cloud" id="teacherCloud"></div>
  </div>
</section>

<!-- 原创文章 -->
<section class="alt">
  <div class="sec-inner">
    <div class="sec-header">
      <div class="sec-tag">Original Writing</div>
      <h2 class="sec-title">黄师傅原创文章</h2>
      <p class="sec-subtitle">游学笔记、人物特写、个人叙事——记录十年行走的深度思考。</p>
    </div>
    <div class="article-grid" id="articleGrid"></div>
  </div>
</section>

<!-- ═══════════ 分隔线 ═══════════ -->
<div class="division">
  <div class="division-line">
    <div class="dl"></div>
    <div class="division-symbol">◆</div>
    <div class="dl"></div>
  </div>
</div>

<!-- ═══════════ 科技板块 ═══════════ -->
<section id="science" class="dark">
  <div class="sec-inner">
    <div class="sec-header">
      <div class="sec-tag">Science & Technology</div>
      <h2 class="sec-title">科技：企业家的科学社区</h2>
      <p class="sec-subtitle">DeepTech 是《麻省理工科技评论》中国独家运营方。我们为企业家搭建通往前沿科技的桥梁。</p>
    </div>

    <!-- Three products -->
    <div class="sci-cards">
      <div class="sci-card">
        <div class="sci-emoji">🧬</div>
        <h3>DeepTech+ 年度会员</h3>
        <p>为每一位会员一对一链接 MIT Technology Review「35 岁以下科技创新 35 人」入选者。不是泛泛的报告，而是针对你企业技术痛点的定向对话。</p>
        <div class="sci-stat">¥9,800<small style="font-size:0.9rem;font-weight:400">/年</small></div>
        <p style="font-size:0.78rem;margin-top:0.5rem;opacity:0.5;">原价 ¥48,000 · 首期 100 人封顶</p>
      </div>
      <div class="sci-card">
        <div class="sci-emoji">🎬</div>
        <h3>非常深科技 · 视频号</h3>
        <p>走进中国最前沿的科学现场——从怀柔科学城到合肥人造太阳，从 TR35 科学家深度对谈到产业前沿解读。用镜头记录中国科技的高光时刻。</p>
        <div style="margin-top:1rem;">
          <div class="location-tags">
            <span class="loc-tag">怀柔科学城</span>
            <span class="loc-tag">合肥科学城</span>
            <span class="loc-tag">上海科学城</span>
            <span class="loc-tag">杭州/深圳</span>
          </div>
        </div>
      </div>
      <div class="sci-card">
        <div class="sci-emoji">📊</div>
        <h3>深科技内参</h3>
        <p>52 周深科技趋势洞察周报。基于 MIT Technology Review 全球编辑网络的第一手信息，覆盖 AI、半导体、生命科学、新材料等关键领域。</p>
        <div class="sci-stat">52<small style="font-size:0.9rem;font-weight:400">期/年</small></div>
        <p style="font-size:0.78rem;margin-top:0.5rem;opacity:0.5;">DeepTech+ 会员专属</p>
      </div>
    </div>

    <!-- TR35 科学家库预览 -->
    <div style="margin-top:3rem;">
      <h3 style="text-align:center;font-family:var(--font-display);font-size:1.3rem;margin-bottom:0.5rem;color:var(--white);">
        TR35 科学家数据库
      </h3>
      <p style="text-align:center;color:rgba(255,255,255,0.5);font-size:0.88rem;margin-bottom:1.5rem;">
        覆盖 {len(scientists)} 位全球顶尖青年科学家 · 7 大前沿领域 · {photo_count} 位已收录真人照片
      </p>
      <div class="tr35-mini" id="tr35Mini"></div>
      <div style="text-align:center;margin-top:2rem;">
        <a href="deeptech-scientists.html" class="btn-cta" style="background:var(--science-light);">浏览完整科学家库 →</a>
      </div>
    </div>
  </div>
</section>

<!-- ═══════════ CTA ═══════════ -->
<section class="cta-section" id="cta">
  <h2 class="cta-title">链接你的科学家</h2>
  <p class="cta-desc">无论你关注人文修行还是科技创新，这里都有你需要的入口。<br>首期 DeepTech+ 会员仅限 100 人，9,800 元/年。</p>
  <a href="https://deeptech-plus.com" class="btn-cta">申请成为 DeepTech+ 会员 →</a>
  <p class="cta-note">或直接联系黄师傅</p>
</section>

<footer>
  <div class="f-line">黄师傅 · 科学与人文 —— 用人文滋养灵魂，以科技洞见未来</div>
  <div class="f-line">思想食堂 2017–2026 · DeepTech+ 企业家的科学社区</div>
  <div class="f-line" style="margin-top:1rem;">© 2026 DeepTech 深科技</div>
</footer>

<script>
// ── Render Tour Cards ──
const tours = {tours_json};
document.getElementById('tourGrid').innerHTML = tours.map(t => `
  <div class="tour-card">
    <div class="tour-img" style="background-image:url(${{t.img}})">
      <span class="tour-year">${{t.year}}</span>
    </div>
    <div class="tour-body">
      <div class="tour-dest">${{t.dest}}</div>
      ${{t.teacher ? '<div class="tour-teacher">✦ ' + t.teacher + '</div>' : ''}}
      <div class="tour-tagline">${{t.tagline}}</div>
    </div>
  </div>
`).join('');

// ── Render Teacher Chips ──
const teachers = {teachers_json};
document.getElementById('teacherCloud').innerHTML = teachers.map(t => `
  <div class="teacher-chip">
    <span class="tc-name">${{t.name}}</span>
    <span class="tc-topic">${{t.topic}}</span>
  </div>
`).join('');

// ── Render Article Cards ──
const articles = {articles_json};
document.getElementById('articleGrid').innerHTML = articles.map(a => `
  <div class="article-card">
    <div class="article-type">${{a.type}}</div>
    <div class="article-title">${{a.title}}</div>
    <div class="article-excerpt">${{a.excerpt}}</div>
  </div>
`).join('');

// ── Render TR35 Mini Cards ──
const TR35 = {scientists_json};
const SCI_COLORS = ['#4F46E5','#7C3AED','#059669','#D97706','#2563EB','#16A34A','#0891B2','#DC2626',
                     '#1E2761','#9333EA','#BE185D','#0D9488'];
const DOMAIN_SHORT = {{'人工智能与机器人':'AI','生物科技与医药':'生物','纳米技术与材料':'新材料','计算机与电子硬件':'电子','能源与可持续':'能源','通信':'通信','因特网与网络':'互联网','交通':'交通'}};

function getInitials(name) {{
  if (/[\\u4e00-\\u9fff]/.test(name)) return name.charAt(0);
  const p = name.trim().split(/\\s+/);
  return p.length>1 ? (p[0][0]+p[p.length-1][0]).toUpperCase() : name.slice(0,2).toUpperCase();
}}

// Show top 18 scientists
const top = TR35.filter(s => s.domain === '人工智能与机器人').slice(0, 5)
  .concat(TR35.filter(s => s.domain === '纳米技术与材料').slice(0, 4))
  .concat(TR35.filter(s => s.domain === '生物科技与医药').slice(0, 4))
  .concat(TR35.filter(s => s.domain === '计算机与电子硬件').slice(0, 3))
  .concat(TR35.filter(s => s.domain === '能源与可持续').slice(0, 2));

document.getElementById('tr35Mini').innerHTML = top.map((s,i) => {{
  const bg = s.photo ? 'background-image:url('+s.photo+');background-size:cover' : 'background:'+SCI_COLORS[i%SCI_COLORS.length];
  return `<div class="tm-card">
    <div class="tm-avatar" style="${{bg}}">${{s.photo ? '' : getInitials(s.name)}}</div>
    <div class="tm-info">
      <div class="tm-name">${{s.name}}</div>
      <div class="tm-domain">${{DOMAIN_SHORT[s.domain] || s.domain}} · ${{s.org ? s.org.substring(0,12) : ''}}</div>
    </div>
  </div>`;
}}).join('');

// Smooth scroll for nav links
document.querySelectorAll('a[href^="#"]').forEach(a => {{
  a.addEventListener('click', function(e) {{
    e.preventDefault();
    const t = document.querySelector(this.getAttribute('href'));
    if (t) t.scrollIntoView({{behavior:'smooth',block:'start'}});
  }});
}});
</script>
</body>
</html>'''

    out_path = os.path.join(SITE_DIR, "index.html")
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"✅ 网站已生成: {out_path}")
    print(f"   大小: {len(html):,} 字符 / {len(html.encode())/1024:.1f} KB")
    
    return out_path

if __name__ == '__main__':
    print("🚀 生成「黄师傅·科学与人文」网站…")
    build()
    print("完成!")
