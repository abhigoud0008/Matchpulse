import streamlit as st
import pandas as pd

from agents.event_agent import load_events
from agents.stats_agent import get_match_stats
from agents.narrative_agent import generate_narrative
from agents.explainability_agent import explain_moment
from agents.personalization_agent import (
    analyst_view,
    fan_view,
    player_view,
    studio_view
)
from agents.recap_agent import generate_recap

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------

st.set_page_config(
    page_title="MatchPulse",
    page_icon="⚽",
    layout="wide"
)

# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

events = load_events("data/synthetic_events.json")
stats = get_match_stats("data/synthetic_events.json")

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("⚽ MatchPulse")
st.subheader(
    "AI-Powered Football Intelligence Platform"
)

st.markdown("---")

# --------------------------------------------------
# MATCH INTELLIGENCE
# --------------------------------------------------

st.header("📊 Match Intelligence")

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric(
        "Possession",
        f"{stats['possession']}%"
    )

with col2:
    st.metric(
        "Pass Accuracy",
        f"{stats['pass_accuracy']}%"
    )

with col3:
    st.metric(
        "Goals",
        stats["goals"]
    )

with col4:
    st.metric(
        "Shots",
        stats["shots"]
    )

with col5:
    st.metric(
        "Pressure Index",
        stats["pressure_index"]
    )

# --------------------------------------------------
# LIVE FEED AND INSIGHTS
# --------------------------------------------------

left, right = st.columns(2)

with left:

    st.header("⚽ Live Match Feed")

    for event in events:

        st.write(
            f"{event['minute']}' | "
            f"{event['team']} | "
            f"{event['player']} | "
            f"{event['event'].upper()}"
        )

with right:

    st.header("🧠 AI Narrative")

    narrative = generate_narrative(stats)

    st.success(narrative)

    st.header("❓ Why It Matters")

    explanation = explain_moment()

    st.info(explanation)

# --------------------------------------------------
# MOMENTUM CHART
# --------------------------------------------------

st.header("📈 Match Momentum")

momentum_data = pd.DataFrame(
    {
        "Minute": [10,20,30,40,50,60,70,80,90],
        "Momentum": [20,35,45,60,72,80,85,90,95]
    }
)

st.line_chart(
    momentum_data.set_index("Minute")
)

# --------------------------------------------------
# TEAM COMPARISON
# --------------------------------------------------

st.header("⚽ Team Comparison")

team1, team2 = st.columns(2)

with team1:
    st.metric(
        "Blue FC Possession",
        f"{stats['possession']}%"
    )

with team2:
    st.metric(
        "Red FC Possession",
        f"{100 - stats['possession']}%"
    )

# --------------------------------------------------
# PLAYER SPOTLIGHT
# --------------------------------------------------

st.header("⭐ Player Spotlight")

st.success(
    """
Player of the Match

Alex

⚽ Goals: 1
🎯 Shots: 2

Key Contribution:
Scored the decisive goal and led multiple attacks.
"""
)

# --------------------------------------------------
# PERSONALIZATION
# --------------------------------------------------

st.header("👤 Personalized Experience")

mode = st.radio(
    "Select User Mode",
    [
        "Analyst",
        "Fan",
        "Player",
        "Studio"
    ]
)

if mode == "Analyst":

    st.code(
        analyst_view(stats)
    )

elif mode == "Fan":

    st.success(
        fan_view()
    )

elif mode == "Player":

    st.info(
        player_view()
    )

elif mode == "Studio":

    st.warning(
        studio_view()
    )

# --------------------------------------------------
# MULTI LANGUAGE
# --------------------------------------------------

st.header("🌍 Multi-Language Storytelling")

language = st.selectbox(
    "Choose Language",
    [
        "English",
        "Telugu",
        "Hindi"
    ]
)

if language == "English":

    st.write(
        "Blue FC is dominating possession and controlling the rhythm of the match."
    )

elif language == "Telugu":

    st.write(
        "బ్లూ ఎఫ్‌సీ మ్యాచ్‌పై ఆధిపత్యం చెలాయిస్తూ ఆటను నియంత్రిస్తోంది."
    )

elif language == "Hindi":

    st.write(
        "ब्लू एफसी मैच की गति और गेंद पर नियंत्रण बनाए हुए है।"
    )

# --------------------------------------------------
# BROADCAST STUDIO INSIGHT
# --------------------------------------------------

st.header("📺 Broadcast Studio Insight")

st.info(
    f"""
Blue FC maintained {stats['possession']}% possession.

Pressure Index: {stats['pressure_index']}

Suggested Broadcast Overlay:

'Blue FC Dominating Through Sustained Possession'

Recommended Display Duration:
8 Seconds
"""
)

# --------------------------------------------------
# MATCH RECAP
# --------------------------------------------------

st.header("📝 Automated Match Recap")

recap = generate_recap(stats)

st.warning(recap)

# --------------------------------------------------
# MULTI AGENT WORKFLOW
# --------------------------------------------------

st.header("🤖 Multi-Agent Architecture")

st.markdown("""
### Workflow

Synthetic Match Events

⬇️

Event Agent

⬇️

Stats Agent

⬇️

Gemini Narrative Agent

⬇️

Gemini Explainability Agent

⬇️

Personalization Agent

⬇️

Gemini Recap Agent

⬇️

Streamlit Dashboard
""")

# --------------------------------------------------
# HACKATHON COVERAGE
# --------------------------------------------------

st.header("✅ Hackathon Requirements Coverage")

st.markdown("""
✅ Real-Time Event Ingestion

✅ Match Intelligence

✅ Narrative Generation

✅ Explainability

✅ Multi-Agent Workflow

✅ Personalization

✅ Broadcast Insights

✅ Automated Match Recaps

✅ Multi-Language Storytelling

✅ Synthetic Football Data
""")

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown("---")

st.caption(
    "MatchPulse | Built for Microsoft Premier League Hackathon"
)