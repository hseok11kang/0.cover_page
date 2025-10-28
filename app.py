# 0_cover_page.py (타이포·아이콘·카드 사이즈 증대 버전)
import math
import streamlit as st

st.set_page_config(
    page_title="0. Cover Page | AI Agents Portal",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ===== Title Gradient Colors (Blue → Violet → Pink) =====
C1 = "#3B82F6"   # blue-500
C2 = "#8B5CF6"   # violet-500
C3 = "#EC4899"   # pink-500
CARD_BG = "rgba(255,255,255,1)"
BORDER = "rgba(0,0,0,.06)"

# ⬇️ 폰트/아이콘/카드 전반 크기를 키움 (웹 확대 없이도 보기 좋게)
st.markdown(
    f"""
    <style>
      .block-container {{ padding-top: 1rem !important; padding-bottom: 1.25rem !important; text-align: center; }}

      /* 헤더 타이틀/서브타이틀 조금 더 큼 */
      h1.hero-title {{
        font-weight: 900; font-size: clamp(36px, 6.2vw, 72px); line-height: 1.04; margin: 0 0 .25rem 0;
        background: linear-gradient(90deg, {C1} 0%, {C2} 52%, {C3} 100%);
        -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent; color: transparent;
      }}
      p.hero-sub {{ font-size: clamp(16px, 2.1vw, 22px); opacity: .85; margin: .25rem 0 1.0rem 0; }}
      .divider-min {{ font-size:24px; opacity:.55; margin:.2rem 0 1rem 0; }}

      .st-emotion-cache-ocqkz7, .st-emotion-cache-1vbkxwb {{ gap: 0.7rem !important; }}

      /* 카드 자체를 조금 더 큼 + 여백 확대 */
      a.agent-card {{
        display:flex; flex-direction:column; align-items:center; justify-content:center;
        text-decoration:none !important; color:inherit !important;
        background:{CARD_BG}; border:1px solid {BORDER}; border-radius:16px;
        padding:20px 18px 22px 18px; box-shadow:0 8px 22px rgba(0,0,0,.07);
        transition: transform .12s ease, box-shadow .12s ease, border-color .12s ease;
        aspect-ratio: 3 / 2; text-align:center; margin-bottom: 0.8rem; overflow:hidden;
      }}
      a.agent-card:hover {{ transform:translateY(-2px); box-shadow:0 14px 28px rgba(0,0,0,.10); border-color:rgba(0,0,0,.10); }}
      a.agent-card:active {{ transform:translateY(0); }}

      /* 아이콘 컨테이너/이모지 크기 ↑ (반응형 clamp로 폭에 맞춰 자연스레 커지도록) */
      .ic-wrap {{
        width:clamp(48px, 5.2vw, 64px); height:clamp(48px, 5.2vw, 64px);
        border-radius:14px; display:flex; align-items:center; justify-content:center;
        font-size:clamp(24px, 3.2vw, 34px); color:white; margin:0 auto 8px auto;
      }}

      /* 제목/설명 폰트 확대 */
      .agent-title {{ font-weight:800; font-size:clamp(17px, 1.6vw, 20px); margin:8px 0 12px 0; line-height:1.1; }}
      .agent-desc  {{ font-size:clamp(14px, 1.25vw, 15.5px); opacity:.85; min-height:40px; line-height:1.45; }}
    </style>
    """,
    unsafe_allow_html=True,
)

AGENTS = [
    {"name": "Product USP Analyzer",  "emoji": "⚡", "color": "#0EA5E9", "desc": "Agent가 제품의 PDP를 인식하여 Unique Selling Point를 도출하고 비교해줍니다.", "url": "https://1uspanalyzer-l5ft4zd63p7prwxz2csy9k.streamlit.app/"},
    {"name": "Competitors Finder",  "emoji": "🔎", "color": "#F97316", "desc": "Agent가 경쟁 제품을 다각도로 리서치하여 판단, 그 결과를 제시합니다.", "url": "https://2competitorsfinder-nisnoepugznnhhs2znxhk4.streamlit.app/"},
    {"name": "Brand Fit Auditor",  "emoji": "🧭", "color": "#10B981", "desc": "Agent가 마케팅 소재와 Brand의 적합성 여부를 판단하여 평가 및 수정사항을 제안합니다.", "url": "https://3brandfitauditor-kggk6gexhuxsaqdppnfzfi.streamlit.app/"},
    {"name": "Social Marcom Ideamaker",  "emoji": "💡", "color": "#8B5CF6", "desc": "Agent가 특정 기간의 로컬 Event를 기반으로 마케팅 방향성을 제안합니다.", "url": "https://4marcomideamaker-vstu5yvn8tkd2xumvrq9nc.streamlit.app/"},
    {"name": "Social Analyzer",  "emoji": "📊", "color": "#14B8A6", "desc": "Sprinklr 연계를 기반으로 소셜리스닝 및 소셜마케팅 성과분석 대시보드를 제공합니다.", "url": "https://5socialanalyzer-peczsbixd46ewvvilrchfg.streamlit.app/"},
    {"name": "Creative Risk Auditor",  "emoji": "⚠️",  "color": "#EF4444", "desc": "Agent가 마케팅/광고에 사용될 소재의 정치/사회/문화/환경 측면 리스크를 진단합니다.", "url": "https://6creativeriskauditor-x9rtbb4ysbzednb3oc7pjs.streamlit.app/"},
    {"name": "Product Visual Optimizer","emoji":"📸",  "color": "#2563EB", "desc": "Agent가 제품 Key Visual 이미지를 마케팅/광고 목적에 맞게 수정/변경합니다.","url": "https://7appuctkvgenerator-ytyxho7ywsmfdi93erhifr.streamlit.app/"},
    {"name": "Market Researcher(준비중)","emoji":"🌏", "color": "#22C55E", "desc": "Agent가 국내/외 다양한 카테고리의 시장조사를 수행합니다", "url": "https://market-research-service-644231591371.asia-northeast3.run.app/"},
    {"name": "YouTube Analyzer(준비중)","emoji":"🎞️", "color": "#F43F5E", "desc": "Agent가 자/타사 YouTube 채널의 커뮤니케이션 방향성과 퍼포먼스를 조사합니다.", "url": "#"},
    {"name": "Agent10(준비중)", "emoji": "💬", "color": "#6366F1", "desc": "Agent 준비중입니다.", "url": "#"},
    {"name": "Agent11(준비중)", "emoji": "🌐", "color": "#0EA5E9", "desc": "Agent 준비중입니다.", "url": "#"},
    {"name": "Agent12(준비중)", "emoji": "🧪", "color": "#FB923C", "desc": "Agent 준비중입니다.", "url": "#"},
]

st.markdown('<h1 class="hero-title">Introducing our AI Agents</h1>', unsafe_allow_html=True)
st.markdown('<p class="hero-sub">Your AI Marketing Stack — 마케터의 하루를 자동화하는 AI 에이전트 허브!</p>', unsafe_allow_html=True)
st.markdown('<div style="height: 12px;"></div>', unsafe_allow_html=True)  # 카드 위 여백 한칸 추가

def render_agent_card(agent: dict, idx: int):
    # 요청사항: Agent 8~12 카드는 옅은 회색 배경 적용
    pending = 8 <= (idx + 1) <= 12
    pending_bg = "rgba(243,244,246,1)"  # gray-100
    card_bg = pending_bg if pending else CARD_BG

    st.markdown(
        f"""
        <a class="agent-card" href="{agent.get('url','#')}" target="_blank" rel="noopener noreferrer" style="background:{card_bg};">
            <div class="ic-wrap" style="background:{agent.get('color','#111827')};">{agent.get('emoji','🤖')}</div>
            <div class="agent-title">{agent.get('name','Agent')}</div>
            <div class="agent-desc">{agent.get('desc','설명 준비중입니다.')}</div>
        </a>
        """,
        unsafe_allow_html=True,
    )

cols_per_row = 4
rows = math.ceil(len(AGENTS) / cols_per_row)
i = 0
for _ in range(rows):
    cols = st.columns(cols_per_row, gap="small")
    for c in cols:
        if i >= len(AGENTS): break
        with c: render_agent_card(AGENTS[i], i)
        i += 1

st.markdown("<div style='opacity:.55; font-size:12.5px; margin-top:.6rem;'>© 2025 디마 Agents · All Agents Portal</div>", unsafe_allow_html=True)

