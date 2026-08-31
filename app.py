import streamlit as st
import pandas as pd
import requests
import re
import html
import plotly.express as px
import plotly.graph_objects as go


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Sales Intelligence",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# PROFESSIONAL DARK THEME
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       PREMIUM DARK SALES INTELLIGENCE THEME
       ======================================================== */

    .stApp {
        background:
            radial-gradient(circle at 8% 0%, rgba(37,99,235,.10), transparent 28%),
            radial-gradient(circle at 92% 8%, rgba(139,92,246,.09), transparent 28%),
            #060B16;
        color: #F8FAFC;
    }

    header[data-testid="stHeader"] {
        background: rgba(6,11,22,.88) !important;
    }

    .main .block-container {
        max-width: 1500px;
        padding-top: 1.4rem;
        padding-bottom: 3rem;
    }

    /* ========================================================
       SIDEBAR
       ======================================================== */

    section[data-testid="stSidebar"] {
        background:
            linear-gradient(180deg, #0B1220 0%, #0A1020 55%, #080D18 100%) !important;
        border-right: 1px solid #24324A !important;
        box-shadow: 8px 0 30px rgba(0,0,0,.25);
    }

    section[data-testid="stSidebar"] > div {
        background: transparent !important;
    }

    section[data-testid="stSidebar"] h1,
    section[data-testid="stSidebar"] h2,
    section[data-testid="stSidebar"] h3 {
        color: #FFFFFF !important;
        font-weight: 800 !important;
    }

    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] .stCaption {
        color: #AAB8CC !important;
    }

    section[data-testid="stSidebar"] label {
        color: #F1F5F9 !important;
        font-weight: 750 !important;
        font-size: .92rem !important;
    }

    section[data-testid="stSidebar"] .stMultiSelect,
    section[data-testid="stSidebar"] .stDateInput {
        margin-bottom: .55rem;
    }

    /* ========================================================
       SIDEBAR INPUTS
       ======================================================== */

    section[data-testid="stSidebar"] div[data-baseweb="select"] > div {
        background: #172235 !important;
        border: 1px solid #334766 !important;
        border-radius: 11px !important;
        color: #FFFFFF !important;
        min-height: 44px !important;
        box-shadow: inset 0 1px 0 rgba(255,255,255,.025);
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"]:hover > div {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 0 1px rgba(56,189,248,.18);
    }

    section[data-testid="stSidebar"] div[data-baseweb="select"] span,
    section[data-testid="stSidebar"] div[data-baseweb="select"] input {
        color: #F8FAFC !important;
    }

    section[data-testid="stSidebar"] input {
        background: #172235 !important;
        color: #F8FAFC !important;
        border: 1px solid #334766 !important;
    }

    section[data-testid="stSidebar"] div[data-testid="stDateInput"] input {
        background: #172235 !important;
        color: #F8FAFC !important;
        border: 1px solid #334766 !important;
        border-radius: 11px !important;
        min-height: 44px;
    }

    section[data-testid="stSidebar"] div[data-testid="stDateInput"] input::placeholder {
        color: #AAB8CC !important;
    }

    /* Dropdown menu */
    div[data-baseweb="popover"],
    div[data-baseweb="menu"] {
        background: #101A2B !important;
        border: 1px solid #334766 !important;
    }

    div[role="option"] {
        background: #101A2B !important;
        color: #E5E7EB !important;
    }

    div[role="option"]:hover {
        background: #1D4ED8 !important;
        color: #FFFFFF !important;
    }

    /* ========================================================
       HERO / HEADINGS
       ======================================================== */

    h1 {
        color: #FFFFFF !important;
        font-size: 2.65rem !important;
        font-weight: 850 !important;
        letter-spacing: -1.2px;
    }

    h2 {
        color: #F8FAFC !important;
        font-weight: 850 !important;
        letter-spacing: -.5px;
        margin-top: 1.4rem !important;
    }

    h3 {
        color: #EAF2FF !important;
        font-weight: 800 !important;
    }

    .section-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #334766, transparent);
        margin: 18px 0 10px 0;
    }

    .hero {
        background:
            linear-gradient(135deg, rgba(15,23,42,.98), rgba(17,24,39,.94)),
            radial-gradient(circle at 85% 20%, rgba(6,182,212,.14), transparent 30%);
        border: 1px solid #2B3B55;
        border-radius: 20px;
        padding: 24px 28px;
        margin-bottom: 22px;
        box-shadow: 0 14px 40px rgba(0,0,0,.28);
        position: relative;
        overflow: hidden;
    }

    .hero:after {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        height: 3px;
        width: 100%;
        background: linear-gradient(90deg, #06B6D4, #3B82F6, #8B5CF6, #EC4899);
    }

    .hero-title {
        font-size: 2.35rem;
        font-weight: 850;
        color: #FFFFFF;
        letter-spacing: -.8px;
    }

    .hero-subtitle {
        margin-top: 6px;
        color: #B7C5D9;
        font-size: 1rem;
    }

    .live-pill {
        display: inline-block;
        margin-top: 13px;
        padding: 6px 11px;
        border-radius: 999px;
        background: rgba(16,185,129,.12);
        border: 1px solid rgba(16,185,129,.35);
        color: #34D399;
        font-size: .78rem;
        font-weight: 800;
    }

    /* ========================================================
       KPI CARDS — DIFFERENT COLOR ACCENTS
       ======================================================== */

    div[data-testid="stMetric"] {
        background:
            linear-gradient(145deg, #121C2D 0%, #0F1726 100%);
        border: 1px solid #2A3A54;
        border-radius: 16px;
        padding: 19px 20px;
        min-height: 116px;
        box-shadow: 0 9px 28px rgba(0,0,0,.22);
        transition: .2s ease;
        position: relative;
        overflow: hidden;
    }

    div[data-testid="stMetric"]:before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 4px;
        background: #38BDF8;
    }

    /* 1st / 2nd / 3rd / 4th cards in every row */
    .main div[data-testid="column"]:nth-child(1) div[data-testid="stMetric"]:before {
        background: #06B6D4;
    }
    .main div[data-testid="column"]:nth-child(2) div[data-testid="stMetric"]:before {
        background: #A855F7;
    }
    .main div[data-testid="column"]:nth-child(3) div[data-testid="stMetric"]:before {
        background: #10B981;
    }
    .main div[data-testid="column"]:nth-child(4) div[data-testid="stMetric"]:before {
        background: #F59E0B;
    }

    div[data-testid="stMetric"]:hover {
        transform: translateY(-2px);
        border-color: #4A638A;
        box-shadow: 0 12px 32px rgba(0,0,0,.32);
    }

    div[data-testid="stMetricLabel"] {
        color: #AAB8CC !important;
        font-size: .83rem !important;
        font-weight: 650 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #FFFFFF !important;
        font-size: 1.72rem !important;
        font-weight: 850 !important;
        text-shadow: 0 1px 12px rgba(255,255,255,.05);
    }

    div[data-testid="stMetricDelta"] {
        font-weight: 750 !important;
    }

    /* ========================================================
       METRIC TITLE VISIBILITY FIX
       Streamlit renders the metric label inside nested elements.
       Force the title text to remain bright and fully visible.
       ======================================================== */

    div[data-testid="stMetricLabel"],
    div[data-testid="stMetricLabel"] *,
    div[data-testid="stMetricLabel"] p,
    div[data-testid="stMetricLabel"] span,
    div[data-testid="stMetricLabel"] div {
        color: #DCE8F7 !important;
        -webkit-text-fill-color: #DCE8F7 !important;
        opacity: 1 !important;
        visibility: visible !important;
        font-size: .88rem !important;
        font-weight: 750 !important;
        line-height: 1.35 !important;
    }

    div[data-testid="stMetricLabel"] {
        min-height: 24px !important;
        margin-bottom: 6px !important;
    }

    div[data-testid="stMetricValue"],
    div[data-testid="stMetricValue"] *,
    div[data-testid="stMetricValue"] p,
    div[data-testid="stMetricValue"] span {
        color: #FFFFFF !important;
        -webkit-text-fill-color: #FFFFFF !important;
        opacity: 1 !important;
        visibility: visible !important;
    }

    div[data-testid="stMetricDelta"],
    div[data-testid="stMetricDelta"] * {
        opacity: 1 !important;
        visibility: visible !important;
    }

    /* Make metric titles readable even when Streamlit applies
       secondary/muted text styles internally. */
    div[data-testid="stMetric"] p,
    div[data-testid="stMetric"] label {
        opacity: 1 !important;
    }

    /* ========================================================
       CUSTOM KPI CARDS — GUARANTEED TITLE VISIBILITY
       ======================================================== */

    .custom-metric-card {
        position: relative;
        overflow: hidden;
        min-height: 116px;
        padding: 17px 20px 16px 22px;
        border-radius: 16px;
        border: 1px solid #2F425F;
        background: linear-gradient(145deg, #162238 0%, #101A2C 100%);
        box-shadow: 0 10px 28px rgba(0,0,0,.24), inset 0 1px 0 rgba(255,255,255,.035);
        transition: transform .18s ease, border-color .18s ease, box-shadow .18s ease;
        margin-bottom: 10px;
    }

    .custom-metric-card:hover {
        transform: translateY(-3px);
        border-color: #4D6A91;
        box-shadow: 0 14px 34px rgba(0,0,0,.34), 0 0 0 1px rgba(56,189,248,.08);
    }

    .custom-metric-card::before {
        content: "";
        position: absolute;
        left: 0;
        top: 0;
        bottom: 0;
        width: 5px;
        background: var(--metric-accent);
        box-shadow: 0 0 14px var(--metric-accent);
    }

    .custom-metric-title {
        display: block !important;
        color: #DCE8F7 !important;
        opacity: 1 !important;
        visibility: visible !important;
        font-size: .86rem !important;
        font-weight: 800 !important;
        line-height: 1.35 !important;
        letter-spacing: .15px;
        margin: 0 0 8px 0 !important;
        text-shadow: 0 1px 5px rgba(0,0,0,.35);
    }

    .custom-metric-value {
        display: block !important;
        color: #FFFFFF !important;
        opacity: 1 !important;
        visibility: visible !important;
        font-size: 1.62rem !important;
        font-weight: 900 !important;
        line-height: 1.15 !important;
        letter-spacing: -.35px;
        margin: 0 !important;
        text-shadow: 0 2px 12px rgba(255,255,255,.08);
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .custom-metric-delta {
        display: inline-block !important;
        margin-top: 8px !important;
        padding: 3px 9px !important;
        border-radius: 999px !important;
        background: rgba(16,185,129,.13) !important;
        color: #34D399 !important;
        border: 1px solid rgba(16,185,129,.16) !important;
        font-size: .76rem !important;
        font-weight: 800 !important;
    }

    /* Never allow Streamlit's muted text rules to affect custom cards. */
    .custom-metric-card,
    .custom-metric-card * {
        -webkit-text-fill-color: initial;
    }

    /* ========================================================
       CHART CARDS
       ======================================================== */

    div[data-testid="stPlotlyChart"] {
        background: linear-gradient(145deg, #0D1625, #0B1321) !important;
        border: 1px solid #263750 !important;
        border-radius: 16px !important;
        padding: 8px !important;
        box-shadow: 0 10px 30px rgba(0,0,0,.24) !important;
        margin-bottom: 12px !important;
    }

    /* ========================================================
       TABLES
       ======================================================== */

    .pro-table-wrap {
        background: linear-gradient(145deg, #0D1625, #0A1220);
        border: 1px solid #2A3A54;
        border-radius: 15px;
        overflow: hidden;
        box-shadow: 0 9px 28px rgba(0,0,0,.22);
        margin: 8px 0 18px 0;
    }

    .pro-table {
        width: 100%;
        border-collapse: collapse;
        color: #E8EEF7;
        font-size: .88rem;
    }

    .pro-table th {
        background: linear-gradient(90deg, #17253A, #1A2941);
        color: #FFFFFF;
        font-weight: 800;
        text-align: left;
        padding: 12px 13px;
        border-bottom: 1px solid #3A4C68;
        white-space: nowrap;
    }

    .pro-table td {
        padding: 11px 13px;
        border-bottom: 1px solid #1D2A3E;
        color: #DCE6F3;
    }

    .pro-table tr:nth-child(even) td {
        background: rgba(255,255,255,.018);
    }

    .pro-table tr:hover td {
        background: rgba(56,189,248,.07);
        color: #FFFFFF;
    }

    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button,
    .stDownloadButton > button {
        background: linear-gradient(135deg, #2563EB, #7C3AED) !important;
        color: #FFFFFF !important;
        border: 1px solid rgba(255,255,255,.12) !important;
        border-radius: 11px !important;
        font-weight: 800 !important;
        padding: .68rem 1.35rem !important;
        box-shadow: 0 7px 20px rgba(37,99,235,.22);
    }

    .stButton > button:hover,
    .stDownloadButton > button:hover {
        transform: translateY(-1px);
        box-shadow: 0 10px 25px rgba(124,58,237,.30);
        border-color: #60A5FA !important;
    }

    /* ========================================================
       TEXT AREA
       ======================================================== */

    textarea {
        background: #101A2B !important;
        color: #F8FAFC !important;
        border: 1px solid #334766 !important;
        border-radius: 12px !important;
    }

    textarea:focus {
        border-color: #38BDF8 !important;
        box-shadow: 0 0 0 1px #38BDF8 !important;
    }

    /* ========================================================
       INFO / AI / ALERT BOXES
       ======================================================== */

    .ai-box {
        background: linear-gradient(135deg, #111A32, #19133A);
        border: 1px solid #6941C6;
        border-left: 5px solid #A855F7;
        border-radius: 16px;
        padding: 20px 22px;
        margin: 15px 0 20px 0;
        box-shadow: 0 10px 30px rgba(124,58,237,.12);
    }

    .info-box {
        background: linear-gradient(135deg, #0E1828, #101A2B);
        border: 1px solid #29415F;
        border-left: 4px solid #06B6D4;
        border-radius: 13px;
        padding: 15px 18px;
        color: #C7D4E6;
        margin-bottom: 20px;
    }

    .insight-card {
        background: linear-gradient(145deg, #111C2E, #0E1727);
        border: 1px solid #2B3D59;
        border-radius: 16px;
        padding: 18px;
        min-height: 125px;
        box-shadow: 0 9px 25px rgba(0,0,0,.22);
    }

    hr {
        border-color: #1E2C42 !important;
    }

    /* Streamlit alerts */
    div[data-testid="stAlert"] {
        background: #101A2B !important;
        border-radius: 12px !important;
        border: 1px solid #2C3D58 !important;
    }

    /* Footer */
    .footer-note {
        text-align: center;
        color: #73839A;
        font-size: .82rem;
        padding: 12px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# CONFIGURATION
# ============================================================

DATA_FILE = "Data/AI_Sales_Intelligence_Dataset.xlsx"

# ============================================================
# CLOUD AI CONFIGURATION — GOOGLE GEMINI
# ============================================================
# IMPORTANT: Do NOT put the API key directly in this Python file.
# Add it in Streamlit Cloud -> App settings -> Secrets as:
# GEMINI_API_KEY = "your_api_key_here"

GEMINI_API_URL = (
    "https://generativelanguage.googleapis.com/v1beta/"
    "models/gemini-2.5-flash:generateContent"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():

    sales = pd.read_excel(
        DATA_FILE,
        sheet_name="Fact_Sales"
    )

    target = pd.read_excel(
        DATA_FILE,
        sheet_name="Fact_Target"
    )

    activity = pd.read_excel(
        DATA_FILE,
        sheet_name="Fact_Activity"
    )

    sales["Date"] = pd.to_datetime(
        sales["Date"]
    )

    activity["Date"] = pd.to_datetime(
        activity["Date"]
    )

    target["Month"] = pd.to_datetime(
        target["Month"]
    )

    return sales, target, activity


sales, target, activity = load_data()


# ============================================================
# CREATE STATE → REGION MAPPING
# ============================================================

# Fact_Target contains State_ID, while Fact_Sales contains
# State_ID + State + Region. Therefore State_ID is used
# as the common key for the mapping.

state_region_map = (
    sales[["State_ID", "State", "Region"]]
    .dropna()
    .drop_duplicates()
)

# Make sure the merge key has the same data type in both tables.
sales["State_ID"] = sales["State_ID"].astype(str).str.strip()
target["State_ID"] = target["State_ID"].astype(str).str.strip()
state_region_map["State_ID"] = (
    state_region_map["State_ID"].astype(str).str.strip()
)

target = target.merge(
    state_region_map,
    on="State_ID",
    how="left"
)


# ============================================================
# GEMINI AI FUNCTION
# ============================================================

def ask_ai(prompt):
    """Send the dashboard analysis prompt to Google Gemini.

    The API key is read securely from Streamlit Secrets so the
    deployed dashboard does NOT depend on Google Gemini running on the
    user's computer.
    """

    try:
        api_key = st.secrets["GEMINI_API_KEY"]
    except Exception:
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add GEMINI_API_KEY = \"your_key\" "
            "in Streamlit Cloud App settings -> Secrets."
        )

    api_key = str(api_key).strip()

    if not api_key:
        raise RuntimeError(
            "GEMINI_API_KEY is empty. Add a valid Gemini API key in Streamlit Secrets."
        )

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ],
        "generationConfig": {
            "temperature": 0.2
        }
    }

    response = requests.post(
        GEMINI_API_URL,
        params={"key": api_key},
        json=payload,
        timeout=120
    )

    if not response.ok:
        try:
            error_data = response.json()
            error_message = error_data.get("error", {}).get(
                "message",
                response.text
            )
        except Exception:
            error_message = response.text

        raise RuntimeError(
            f"Gemini API error ({response.status_code}): {error_message}"
        )

    data = response.json()

    try:
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError, TypeError):
        raise RuntimeError(
            "Gemini returned an unexpected response. Please try again."
        )



# ============================================================
# PREMIUM TABLE RENDERER
# ============================================================

def render_pro_table(df):
    """Render compact dashboard tables with a dark professional theme."""
    if df is None or df.empty:
        st.info("No data available for the selected filters.")
        return

    html = df.to_html(
        index=False,
        classes="pro-table",
        border=0,
        escape=True
    )

    st.markdown(
        f'<div class="pro-table-wrap">{html}</div>',
        unsafe_allow_html=True
    )


# ============================================================
# CUSTOM METRIC CARD RENDERER
# ============================================================

def render_metric_card(title, value, delta=None, accent="#38BDF8"):
    title_html = html.escape(str(title))
    value_html = html.escape(str(value))
    delta_html = ""
    if delta is not None and str(delta) != "":
        delta_html = f'<div class="custom-metric-delta">{html.escape(str(delta))}</div>'

    st.markdown(
        f"""
        <div class="custom-metric-card" style="--metric-accent:{accent};">
            <div class="custom-metric-title">{title_html}</div>
            <div class="custom-metric-value">{value_html}</div>
            {delta_html}
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🤖 AI Sales Intelligence Dashboard 🚀</div>
        <div class="hero-subtitle">
            Smart insights. Better decisions. Interactive sales performance intelligence.
        </div>
        <div class="live-pill">● LIVE ANALYTICS &nbsp; | &nbsp; Excel + Python + Streamlit + Plotly + Google Gemini</div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.markdown(
    "## 🎛️ Dashboard Filters"
)

st.sidebar.caption(
    "Use filters to analyze specific business segments."
)


# ============================================================
# DATE FILTER
# ============================================================

min_date = sales["Date"].min().date()

max_date = sales["Date"].max().date()

date_range = st.sidebar.date_input(
    "📅 Date Range",
    value=(min_date, max_date),
    min_value=min_date,
    max_value=max_date
)


# ============================================================
# EMPLOYEE FILTER
# ============================================================

employees = sorted(
    sales["Employee_ID"]
    .dropna()
    .unique()
    .tolist()
)

selected_employees = st.sidebar.multiselect(
    "👨‍💼 Employee",
    employees,
    default=[]
)


# ============================================================
# REGION FILTER
# ============================================================

regions = sorted(
    sales["Region"]
    .dropna()
    .unique()
    .tolist()
)

selected_regions = st.sidebar.multiselect(
    "🌎 Region",
    regions,
    default=[]
)


# ============================================================
# STATE FILTER
# ============================================================

states = sorted(
    sales["State"]
    .dropna()
    .unique()
    .tolist()
)

selected_states = st.sidebar.multiselect(
    "📍 State",
    states,
    default=[]
)


# ============================================================
# CATEGORY FILTER
# ============================================================

categories = sorted(
    sales["Category"]
    .dropna()
    .unique()
    .tolist()
)

selected_categories = st.sidebar.multiselect(
    "📦 Category",
    categories,
    default=[]
)


# ============================================================
# APPLY SALES FILTERS
# ============================================================

filtered_sales = sales.copy()


# ------------------------------------------------------------
# DATE
# ------------------------------------------------------------

if len(date_range) == 2:

    start_date = pd.Timestamp(
        date_range[0]
    )

    end_date = pd.Timestamp(
        date_range[1]
    ) + pd.Timedelta(days=1)

    filtered_sales = filtered_sales[
        (filtered_sales["Date"] >= start_date)
        &
        (filtered_sales["Date"] < end_date)
    ]


# ------------------------------------------------------------
# EMPLOYEE
# ------------------------------------------------------------

if selected_employees:

    filtered_sales = filtered_sales[
        filtered_sales["Employee_ID"].isin(
            selected_employees
        )
    ]


# ------------------------------------------------------------
# REGION
# ------------------------------------------------------------

if selected_regions:

    filtered_sales = filtered_sales[
        filtered_sales["Region"].isin(
            selected_regions
        )
    ]


# ------------------------------------------------------------
# STATE
# ------------------------------------------------------------

if selected_states:

    filtered_sales = filtered_sales[
        filtered_sales["State"].isin(
            selected_states
        )
    ]


# ------------------------------------------------------------
# CATEGORY
# ------------------------------------------------------------

if selected_categories:

    filtered_sales = filtered_sales[
        filtered_sales["Category"].isin(
            selected_categories
        )
    ]


# ============================================================
# TARGET FILTERING
# ============================================================

filtered_target = target.copy()


# ------------------------------------------------------------
# TARGET DATE
# ------------------------------------------------------------

if len(date_range) == 2:

    target_start = pd.Timestamp(
        date_range[0]
    ).replace(day=1)

    target_end = (
        pd.Timestamp(date_range[1])
        .replace(day=1)
        + pd.offsets.MonthBegin(1)
    )

    filtered_target = filtered_target[
        (filtered_target["Month"] >= target_start)
        &
        (filtered_target["Month"] < target_end)
    ]


# ------------------------------------------------------------
# TARGET EMPLOYEE
# ------------------------------------------------------------

if selected_employees:

    filtered_target = filtered_target[
        filtered_target["Employee_ID"].isin(
            selected_employees
        )
    ]


# ------------------------------------------------------------
# TARGET REGION
# ------------------------------------------------------------

if selected_regions:

    filtered_target = filtered_target[
        filtered_target["Region"].isin(
            selected_regions
        )
    ]


# ------------------------------------------------------------
# TARGET STATE
# ------------------------------------------------------------

if selected_states:

    filtered_target = filtered_target[
        filtered_target["State"].isin(
            selected_states
        )
    ]


# ------------------------------------------------------------
# TARGET CATEGORY
# ------------------------------------------------------------

if selected_categories:

    filtered_target = filtered_target[
        filtered_target["Category"].isin(
            selected_categories
        )
    ]


# ============================================================
# KPI CALCULATIONS
# ============================================================

primary_sales = (
    filtered_sales["Primary_Sales"].sum()
)

secondary_sales = (
    filtered_sales["Secondary_Sales"].sum()
)

units = (
    filtered_sales["Units"].sum()
)

orders = (
    filtered_sales["Orders"].sum()
)

target_value = (
    filtered_target["Target"].sum()
)


achievement = (
    primary_sales / target_value * 100
    if target_value != 0
    else 0
)


# ============================================================
# KPI SECTION
# ============================================================

st.markdown(
    "## 📊 Sales Performance"
)


col1, col2, col3, col4 = st.columns(4)


with col1:

    render_metric_card(
        "💰 Primary Sales",
        f"₹{primary_sales / 1e6:,.2f}M",
        accent="#06B6D4"
    )


with col2:

    render_metric_card(
        "🛒 Secondary Sales",
        f"₹{secondary_sales / 1e6:,.2f}M",
        accent="#A855F7"
    )


with col3:

    render_metric_card(
        "🎯 Achievement",
        f"{achievement:,.2f}%",
        accent="#10B981"
    )


with col4:

    render_metric_card(
        "📦 Orders",
        f"{orders:,}",
        accent="#F59E0B"
    )


col5, col6 = st.columns(2)


with col5:

    render_metric_card(
        "📈 Units Sold",
        f"{units:,}",
        accent="#EC4899"
    )


with col6:

    render_metric_card(
        "📋 Sales Records",
        f"{len(filtered_sales):,}",
        accent="#6366F1"
    )


st.divider()


# ============================================================
# TARGET VS ACTUAL
# ============================================================

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("🎯 Target vs Actual")

target_gap = primary_sales - target_value

if target_value > 0:

    if achievement >= 100:
        performance_status = "🟢 ABOVE TARGET"
        status_message = "Business is performing above the selected target."
    elif achievement >= 90:
        performance_status = "🟠 NEAR TARGET"
        status_message = "Business is close to the selected target."
    else:
        performance_status = "🔴 BELOW TARGET"
        status_message = "Business is currently below the selected target."

else:
    performance_status = "⚪ TARGET NOT AVAILABLE"
    status_message = "No target is available for the selected filters."


tv1, tv2, tv3, tv4 = st.columns(4)

with tv1:
    render_metric_card(
        "Actual Sales",
        f"₹{primary_sales / 1e6:,.2f}M",
        accent="#06B6D4"
    )

with tv2:
    render_metric_card(
        "Target",
        f"₹{target_value / 1e6:,.2f}M",
        accent="#8B5CF6"
    )

with tv3:
    render_metric_card(
        "Achievement",
        f"{achievement:,.2f}%",
        accent="#10B981"
    )

with tv4:
    render_metric_card(
        "Target Gap / Surplus",
        f"₹{target_gap / 1e6:,.2f}M",
        accent="#F59E0B"
    )


st.markdown(
    f"""
    <div style="
        background:#111827;
        border:1px solid #263244;
        border-left:5px solid {'#10B981' if achievement >= 100 else '#F59E0B' if achievement >= 90 else '#EF4444'};
        border-radius:14px;
        padding:16px 20px;
        margin:15px 0 20px 0;
    ">
        <div style="
            color:#F8FAFC;
            font-size:1.05rem;
            font-weight:750;
        ">
            {performance_status}
        </div>
        <div style="
            color:#94A3B8;
            margin-top:5px;
        ">
            {status_message}
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# Target vs Actual chart

comparison_df = pd.DataFrame({
    "Metric": ["Target", "Actual"],
    "Sales": [target_value, primary_sales]
})


fig_target = go.Figure()

fig_target.add_trace(
    go.Bar(
        x=comparison_df["Metric"],
        y=comparison_df["Sales"],
        text=[
            f"₹{target_value / 1e6:,.2f}M",
            f"₹{primary_sales / 1e6:,.2f}M"
        ],
        textposition="outside",
        marker_color=["#64748B", "#3B82F6"],
        hovertemplate=(
            "<b>%{x}</b><br>"
            "Value: ₹%{y:,.0f}"
            "<extra></extra>"
        )
    )
)

fig_target.update_layout(
    height=400,
    paper_bgcolor="#080D1A",
    plot_bgcolor="#111827",
    font=dict(
        color="#CBD5E1"
    ),
    showlegend=False,
    yaxis=dict(
        title="Sales",
        gridcolor="#263244"
    ),
    xaxis=dict(
        title=""
    ),
    margin=dict(
        l=20,
        r=20,
        t=40,
        b=20
    )
)

st.plotly_chart(
    fig_target,
    use_container_width=True
)


# ============================================================
# GROWTH INTELLIGENCE
# ============================================================

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("📈 Growth Intelligence")

# Monthly sales based on the currently filtered sales data.
growth_monthly = (
    filtered_sales
    .assign(
        Month=filtered_sales["Date"].dt.to_period("M")
    )
    .groupby(
        "Month",
        as_index=False
    )["Primary_Sales"]
    .sum()
    .sort_values("Month")
)

if len(growth_monthly) >= 1:

    growth_monthly["Month_Date"] = (
        growth_monthly["Month"].dt.to_timestamp()
    )

    # Month-over-Month Growth
    growth_monthly["MoM_Growth_%"] = (
        growth_monthly["Primary_Sales"]
        .pct_change()
        .mul(100)
    )

    # Best / lowest month
    best_month_row = growth_monthly.loc[
        growth_monthly["Primary_Sales"].idxmax()
    ]

    lowest_month_row = growth_monthly.loc[
        growth_monthly["Primary_Sales"].idxmin()
    ]

    # Current and previous month
    if len(growth_monthly) >= 2:

        current_month_sales = growth_monthly.iloc[-1]["Primary_Sales"]
        previous_month_sales = growth_monthly.iloc[-2]["Primary_Sales"]

        if previous_month_sales != 0:
            mom_growth = (
                (current_month_sales - previous_month_sales)
                / previous_month_sales
                * 100
            )
        else:
            mom_growth = 0

    else:

        current_month_sales = growth_monthly.iloc[-1]["Primary_Sales"]
        previous_month_sales = 0
        mom_growth = 0

    # YoY Growth
    monthly_yoy = growth_monthly.copy()

    monthly_yoy["YoY_Growth_%"] = (
        monthly_yoy["Primary_Sales"]
        .pct_change(periods=12)
        .mul(100)
    )

    if (
        len(monthly_yoy) >= 13
        and pd.notna(monthly_yoy.iloc[-1]["YoY_Growth_%"])
    ):

        yoy_growth = monthly_yoy.iloc[-1]["YoY_Growth_%"]

    else:

        yoy_growth = None


    # --------------------------------------------------------
    # Growth KPI cards
    # --------------------------------------------------------

    g1, g2, g3, g4 = st.columns(4)

    with g1:

        mom_display = (
            f"{mom_growth:+,.2f}%"
            if len(growth_monthly) >= 2
            else "N/A"
        )

        render_metric_card(
            "📈 MoM Growth",
            mom_display,
            accent="#06B6D4"
        )

    with g2:

        yoy_display = (
            f"{yoy_growth:+,.2f}%"
            if yoy_growth is not None
            else "N/A"
        )

        render_metric_card(
            "📊 YoY Growth",
            yoy_display,
            accent="#A855F7"
        )

    with g3:

        render_metric_card(
            "🏆 Best Month",
            best_month_row["Month"].strftime("%b %Y"),
            f"↑ ₹{best_month_row['Primary_Sales'] / 1e6:,.2f}M",
            accent="#10B981"
        )

    with g4:

        render_metric_card(
            "📉 Lowest Month",
            lowest_month_row["Month"].strftime("%b %Y"),
            f"↑ ₹{lowest_month_row['Primary_Sales'] / 1e6:,.2f}M",
            accent="#EF4444"
        )


    # --------------------------------------------------------
    # Growth trend chart
    # --------------------------------------------------------

    growth_chart = growth_monthly.copy()

    growth_chart["Month"] = (
        growth_chart["Month_Date"]
    )

    fig_growth = go.Figure()

    fig_growth.add_trace(
        go.Scatter(
            x=growth_chart["Month"],
            y=growth_chart["Primary_Sales"],
            mode="lines+markers",
            name="Primary Sales",
            fill="tozeroy",
            fillcolor="rgba(6,182,212,0.10)",
            line=dict(
                color="#22D3EE",
                width=3
            ),
            marker=dict(
                color="#22D3EE",
                size=8,
                line=dict(color="#E0F2FE", width=1)
            ),
            hovertemplate=(
                "<b>%{x|%b %Y}</b><br>"
                "Sales: ₹%{y:,.0f}"
                "<extra></extra>"
            )
        )
    )

    fig_growth.update_layout(
        height=420,
        paper_bgcolor="#080D1A",
        plot_bgcolor="#111827",
        font=dict(
            color="#CBD5E1"
        ),
        showlegend=False,
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        ),
        xaxis=dict(
            title="Month",
            gridcolor="#263244"
        ),
        yaxis=dict(
            title="Primary Sales",
            gridcolor="#263244"
        ),
        hovermode="x unified",
        hoverlabel=dict(
            bgcolor="#0B1220",
            bordercolor="#38BDF8",
            font=dict(color="#FFFFFF")
        )
    )

    st.subheader("Monthly Sales Growth Trend")

    st.plotly_chart(
        fig_growth,
        use_container_width=True
    )


    # --------------------------------------------------------
    # Growth table
    # --------------------------------------------------------

    growth_display = growth_monthly.copy()

    growth_display["Month"] = (
        growth_display["Month_Date"]
        .dt.strftime("%b %Y")
    )

    growth_display["Primary_Sales"] = (
        growth_display["Primary_Sales"]
        / 1e6
    ).round(2)

    growth_display["MoM_Growth_%"] = (
        growth_display["MoM_Growth_%"]
        .round(2)
    )

    growth_display = growth_display[
        [
            "Month",
            "Primary_Sales",
            "MoM_Growth_%"
        ]
    ]

    growth_display = growth_display.rename(
        columns={
            "Month": "Month",
            "Primary_Sales": "Sales (₹M)",
            "MoM_Growth_%": "MoM Growth %"
        }
    )

    render_pro_table(growth_display)

else:

    st.info(
        "Not enough sales data available for growth analysis."
    )


# ============================================================
# SALES TREND
# ============================================================

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("📈 Sales Trend")


if not filtered_sales.empty:

    monthly_sales = (
        filtered_sales
        .assign(
            Month=filtered_sales["Date"].dt.to_period("M")
        )
        .groupby(
            "Month",
            as_index=False
        )["Primary_Sales"]
        .sum()
    )

    monthly_sales["Month"] = (
        monthly_sales["Month"]
        .dt.to_timestamp()
    )

    fig_trend = go.Figure()

    fig_trend.add_trace(
        go.Scatter(
            x=monthly_sales["Month"],
            y=monthly_sales["Primary_Sales"],
            mode="lines+markers",
            name="Primary Sales",
            fill="tozeroy",
            fillcolor="rgba(59,130,246,0.10)",
            line=dict(
                width=3,
                color="#38BDF8"
            ),
            marker=dict(
                size=8,
                color="#60A5FA",
                line=dict(color="#E0F2FE", width=1)
            ),
            hovertemplate=(
                "<b>%{x|%b %Y}</b><br>"
                "Sales: ₹%{y:,.0f}"
                "<extra></extra>"
            )
        )
    )

    fig_trend.update_layout(
        height=420,
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        ),
        paper_bgcolor="#080D1A",
        plot_bgcolor="#111827",
        font=dict(
            color="#CBD5E1"
        ),
        xaxis=dict(
            title="Month",
            gridcolor="#263244"
        ),
        yaxis=dict(
            title="Primary Sales",
            gridcolor="#263244"
        ),
        hovermode="x unified",
        showlegend=False,
        hoverlabel=dict(
            bgcolor="#0B1220",
            bordercolor="#3B82F6",
            font=dict(color="#FFFFFF")
        )
    )

    st.plotly_chart(
        fig_trend,
        use_container_width=True
    )

else:

    st.warning(
        "No sales data available for the selected filters."
    )


# ============================================================
# REGION ANALYSIS
# ============================================================

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("🌎 Regional Performance")


region_sales = (
    filtered_sales
    .groupby(
        "Region",
        as_index=False
    )["Primary_Sales"]
    .sum()
    .sort_values(
        "Primary_Sales",
        ascending=False
    )
)


col1, col2 = st.columns(
    [1.5, 1]
)


with col1:

    st.subheader(
        "Sales by Region"
    )

    if not region_sales.empty:

        fig_region = px.bar(
            region_sales,
            x="Region",
            y="Primary_Sales",
            color="Region",
            text_auto=".2s",
            color_discrete_sequence=[
                "#3B82F6",
                "#8B5CF6",
                "#10B981",
                "#F59E0B",
                "#EF4444"
            ]
        )

        fig_region.update_layout(
            height=420,
            paper_bgcolor="#080D1A",
            plot_bgcolor="#111827",
            font=dict(
                color="#CBD5E1"
            ),
            showlegend=False,
            xaxis=dict(
                gridcolor="#263244"
            ),
            yaxis=dict(
                gridcolor="#263244",
                title="Primary Sales"
            )
        )

        fig_region.update_traces(
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Sales: ₹%{y:,.0f}"
                "<extra></extra>"
            )
        )

        st.plotly_chart(
            fig_region,
            use_container_width=True
        )


with col2:

    st.subheader(
        "Regional Sales Table"
    )

    region_display = region_sales.copy()

    region_display["Primary_Sales"] = (
        region_display["Primary_Sales"] / 1e6
    ).round(2)

    total_region_sales = (
        region_sales["Primary_Sales"].sum()
    )

    if total_region_sales != 0:

        region_display["Contribution %"] = (
            region_sales["Primary_Sales"]
            / total_region_sales
            * 100
        ).round(2)

    else:

        region_display["Contribution %"] = 0

    region_display = region_display.rename(
        columns={
            "Region": "Region",
            "Primary_Sales": "Sales (₹M)"
        }
    )

    render_pro_table(region_display)


# ============================================================
# CATEGORY ANALYSIS
# ============================================================

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("📦 Category Performance")


category_sales = (
    filtered_sales
    .groupby(
        "Category",
        as_index=False
    )["Primary_Sales"]
    .sum()
    .sort_values(
        "Primary_Sales",
        ascending=False
    )
)


col1, col2 = st.columns(
    [1.5, 1]
)


with col1:

    st.subheader(
        "Sales by Category"
    )

    if not category_sales.empty:

        fig_category = px.bar(
            category_sales,
            x="Category",
            y="Primary_Sales",
            color="Category",
            text_auto=".2s",
            color_discrete_sequence=[
                "#06B6D4",
                "#3B82F6",
                "#8B5CF6",
                "#EC4899",
                "#F59E0B",
                "#10B981",
                "#EF4444",
                "#6366F1",
                "#14B8A6",
                "#F97316"
            ]
        )

        fig_category.update_layout(
            height=450,
            paper_bgcolor="#080D1A",
            plot_bgcolor="#111827",
            font=dict(
                color="#CBD5E1"
            ),
            showlegend=False,
            xaxis=dict(
                tickangle=-35,
                gridcolor="#263244"
            ),
            yaxis=dict(
                gridcolor="#263244",
                title="Primary Sales"
            )
        )

        fig_category.update_traces(
            hovertemplate=(
                "<b>%{x}</b><br>"
                "Sales: ₹%{y:,.0f}"
                "<extra></extra>"
            )
        )

        st.plotly_chart(
            fig_category,
            use_container_width=True
        )


with col2:

    st.subheader(
        "Category Sales Table"
    )

    category_display = category_sales.copy()

    category_display["Primary_Sales"] = (
        category_display["Primary_Sales"]
        / 1e6
    ).round(2)

    total_category_sales = (
        category_sales["Primary_Sales"].sum()
    )

    if total_category_sales != 0:

        category_display["Contribution %"] = (
            category_sales["Primary_Sales"]
            / total_category_sales
            * 100
        ).round(2)

    else:

        category_display["Contribution %"] = 0

    category_display = category_display.rename(
        columns={
            "Category": "Category",
            "Primary_Sales": "Sales (₹M)"
        }
    )

    render_pro_table(category_display)


# ============================================================
# TOP EMPLOYEES
# ============================================================

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("🏆 Top Sales Employees")


employee_sales = (
    filtered_sales
    .groupby(
        "Employee_ID",
        as_index=False
    )["Primary_Sales"]
    .sum()
    .sort_values(
        "Primary_Sales",
        ascending=False
    )
    .head(10)
)


if not employee_sales.empty:

    fig_employee = px.bar(
        employee_sales.sort_values(
            "Primary_Sales"
        ),
        x="Primary_Sales",
        y="Employee_ID",
        orientation="h",
        text_auto=".2s",
        color="Primary_Sales",
        color_continuous_scale=[
            "#1D4ED8",
            "#3B82F6",
            "#60A5FA"
        ]
    )

    fig_employee.update_layout(
        height=450,
        paper_bgcolor="#080D1A",
        plot_bgcolor="#111827",
        font=dict(
            color="#CBD5E1"
        ),
        coloraxis_showscale=False,
        xaxis=dict(
            gridcolor="#263244",
            title="Primary Sales"
        ),
        yaxis=dict(
            gridcolor="#263244",
            title="Employee"
        )
    )

    fig_employee.update_traces(
        hovertemplate=(
            "<b>%{y}</b><br>"
            "Sales: ₹%{x:,.0f}"
            "<extra></extra>"
        )
    )

    st.plotly_chart(
        fig_employee,
        use_container_width=True
    )



# ============================================================
# MANAGEMENT ALERTS
# ============================================================

st.divider()

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("🚨 Management Alerts")

alert_items = []

if target_value > 0:

    if achievement >= 100:
        alert_items.append(
            ("🟢", "Target Status",
             f"Sales are above target by ₹{target_gap / 1e6:,.2f}M.")
        )
    elif achievement >= 90:
        alert_items.append(
            ("🟠", "Target Status",
             f"Sales are close to target with a gap of ₹{abs(target_gap) / 1e6:,.2f}M.")
        )
    else:
        alert_items.append(
            ("🔴", "Target Status",
             f"Sales are below target by ₹{abs(target_gap) / 1e6:,.2f}M.")
        )

if "mom_growth" in globals() and mom_growth is not None:
    if mom_growth < 0:
        alert_items.append(
            ("🔴", "MoM Trend",
             f"Latest month declined {abs(mom_growth):,.2f}% versus the previous month.")
        )
    else:
        alert_items.append(
            ("🟢", "MoM Trend",
             f"Latest month grew {mom_growth:,.2f}% versus the previous month.")
        )

if "yoy_growth" in globals() and yoy_growth is not None:
    if yoy_growth < 0:
        alert_items.append(
            ("🔴", "YoY Trend",
             f"Latest comparable month is down {abs(yoy_growth):,.2f}% YoY.")
        )
    else:
        alert_items.append(
            ("🟢", "YoY Trend",
             f"Latest comparable month is up {yoy_growth:,.2f}% YoY.")
        )

if not region_sales.empty:
    alert_items.append(
        ("⭐", "Regional Leader",
         f"{region_sales.iloc[0]['Region']} leads with ₹{region_sales.iloc[0]['Primary_Sales'] / 1e6:,.2f}M.")
    )

if not category_sales.empty:
    alert_items.append(
        ("📦", "Category Leader",
         f"{category_sales.iloc[0]['Category']} leads with ₹{category_sales.iloc[0]['Primary_Sales'] / 1e6:,.2f}M.")
    )

alert_cols = st.columns(min(4, max(1, len(alert_items))))

for idx, (icon, title, message) in enumerate(alert_items):

    with alert_cols[idx % len(alert_cols)]:

        border = (
            "#10B981" if icon in ["🟢", "⭐", "📦"]
            else "#F59E0B" if icon == "🟠"
            else "#EF4444"
        )

        st.markdown(
            f"""
            <div style="
                background:#111827;
                border:1px solid #263244;
                border-left:4px solid {border};
                border-radius:12px;
                padding:16px;
                min-height:125px;
                margin-bottom:14px;
            ">
                <div style="font-size:1.05rem;font-weight:750;color:#F8FAFC;">
                    {icon} {title}
                </div>
                <div style="color:#94A3B8;margin-top:10px;line-height:1.5;">
                    {message}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================================
# SALES DRILL-DOWN
# ============================================================

st.divider()

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("🔎 Sales Drill-Down")

st.caption(
    "Analyze the current filtered business at Region, State, Category or Employee level."
)

drill_level = st.selectbox(
    "Analysis Level",
    ["Region", "State", "Category", "Employee"],
    key="sales_drill_level"
)

drill_column_map = {
    "Region": "Region",
    "State": "State",
    "Category": "Category",
    "Employee": "Employee_ID"
}

drill_column = drill_column_map[drill_level]

if not filtered_sales.empty:

    sales_drill = (
        filtered_sales
        .groupby(drill_column, as_index=False)
        .agg(
            Sales=("Primary_Sales", "sum"),
            Secondary_Sales=("Secondary_Sales", "sum"),
            Orders=("Orders", "sum"),
            Units=("Units", "sum")
        )
    )

    # Add target at the same drill level whenever the target
    # contains the corresponding column.
    if drill_column in filtered_target.columns:

        target_drill = (
            filtered_target
            .groupby(drill_column, as_index=False)["Target"]
            .sum()
        )

        sales_drill = sales_drill.merge(
            target_drill,
            on=drill_column,
            how="left"
        )

    else:

        sales_drill["Target"] = 0

    sales_drill["Target"] = sales_drill["Target"].fillna(0)

    sales_drill["Achievement_%"] = (
        sales_drill["Sales"]
        .div(sales_drill["Target"].replace(0, pd.NA))
        .mul(100)
        .fillna(0)
    )

    drill_total = sales_drill["Sales"].sum()

    sales_drill["Contribution_%"] = (
        sales_drill["Sales"] / drill_total * 100
        if drill_total != 0
        else 0
    )

    sales_drill = sales_drill.sort_values(
        "Sales",
        ascending=False
    )

    sales_drill["Rank"] = range(
        1,
        len(sales_drill) + 1
    )

    drill_left, drill_right = st.columns([1.5, 1])

    with drill_left:

        drill_chart_data = (
            sales_drill
            .head(15)
            .sort_values("Sales")
        )

        fig_drill = px.bar(
            drill_chart_data,
            x="Sales",
            y=drill_column,
            orientation="h",
            text_auto=".2s",
            color="Sales",
            color_continuous_scale=[
                "#1D4ED8",
                "#3B82F6",
                "#60A5FA"
            ]
        )

        fig_drill.update_layout(
            height=500,
            paper_bgcolor="#080D1A",
            plot_bgcolor="#111827",
            font=dict(color="#CBD5E1"),
            coloraxis_showscale=False,
            margin=dict(l=20, r=20, t=30, b=20),
            xaxis=dict(
                title="Primary Sales",
                gridcolor="#263244"
            ),
            yaxis=dict(
                title=drill_level,
                gridcolor="#263244"
            )
        )

        fig_drill.update_traces(
            hovertemplate=(
                "<b>%{y}</b><br>"
                "Sales: ₹%{x:,.0f}"
                "<extra></extra>"
            )
        )

        st.plotly_chart(
            fig_drill,
            use_container_width=True
        )

    with drill_right:

        st.subheader(f"{drill_level} Performance")

        drill_display = sales_drill.copy()

        drill_display["Sales"] = (
            drill_display["Sales"] / 1e6
        ).round(2)

        drill_display["Target"] = (
            drill_display["Target"] / 1e6
        ).round(2)

        drill_display["Achievement_%"] = (
            drill_display["Achievement_%"]
        ).round(2)

        drill_display["Contribution_%"] = (
            drill_display["Contribution_%"]
        ).round(2)

        drill_display = drill_display.rename(
            columns={
                drill_column: drill_level,
                "Sales": "Sales (₹M)",
                "Target": "Target (₹M)",
                "Achievement_%": "Achievement %",
                "Contribution_%": "Contribution %"
            }
        )

        drill_display = drill_display[
            [
                "Rank",
                drill_level,
                "Sales (₹M)",
                "Target (₹M)",
                "Achievement %",
                "Contribution %",
                "Orders",
                "Units"
            ]
        ]

        render_pro_table(drill_display)

else:

    st.info(
        "No sales data available for the selected filters."
    )


# ============================================================
# EXECUTIVE OPPORTUNITY & RISK INTELLIGENCE
# ============================================================

st.divider()

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("🎯 Opportunity & Risk Intelligence")

# -----------------------------
# Region intelligence
# -----------------------------

region_intel = region_sales.copy()

if not region_intel.empty:

    total_region_sales = region_intel["Primary_Sales"].sum()

    region_intel["Contribution_%"] = (
        region_intel["Primary_Sales"]
        / total_region_sales
        * 100
        if total_region_sales != 0
        else 0
    )

    region_intel["Rank"] = range(
        1,
        len(region_intel) + 1
    )

    best_region_row = region_intel.iloc[0]
    weakest_region_row = region_intel.iloc[-1]

else:

    best_region_row = None
    weakest_region_row = None


# -----------------------------
# Category intelligence
# -----------------------------

category_intel = category_sales.copy()

if not category_intel.empty:

    total_category_sales = category_intel["Primary_Sales"].sum()

    category_intel["Contribution_%"] = (
        category_intel["Primary_Sales"]
        / total_category_sales
        * 100
        if total_category_sales != 0
        else 0
    )

    best_category_row = category_intel.iloc[0]
    weakest_category_row = category_intel.iloc[-1]

else:

    best_category_row = None
    weakest_category_row = None


# -----------------------------
# Executive cards
# -----------------------------

oi1, oi2, oi3, oi4 = st.columns(4)

with oi1:
    if best_region_row is not None:
        render_metric_card(
            "🏆 Strongest Region",
            str(best_region_row["Region"]),
            f"↑ ₹{best_region_row['Primary_Sales'] / 1e6:,.2f}M",
            accent="#10B981"
        )

with oi2:
    if weakest_region_row is not None:
        render_metric_card(
            "⚠️ Attention Region",
            str(weakest_region_row["Region"]),
            f"↑ ₹{weakest_region_row['Primary_Sales'] / 1e6:,.2f}M",
            accent="#F59E0B"
        )

with oi3:
    if best_category_row is not None:
        render_metric_card(
            "📦 Leading Category",
            str(best_category_row["Category"]),
            f"↑ ₹{best_category_row['Primary_Sales'] / 1e6:,.2f}M",
            accent="#8B5CF6"
        )

with oi4:
    if weakest_category_row is not None:
        render_metric_card(
            "🔎 Opportunity Category",
            str(weakest_category_row["Category"]),
            f"↑ ₹{weakest_category_row['Primary_Sales'] / 1e6:,.2f}M",
            accent="#EC4899"
        )


# -----------------------------
# Region contribution chart
# -----------------------------

if not region_intel.empty:

    st.subheader("🌎 Regional Contribution")

    region_contribution = region_intel.copy()

    fig_region_share = px.pie(
        region_contribution,
        names="Region",
        values="Primary_Sales",
        hole=0.58,
        color_discrete_sequence=[
            "#3B82F6",
            "#8B5CF6",
            "#10B981",
            "#F59E0B",
            "#EF4444",
            "#06B6D4",
            "#EC4899",
            "#14B8A6"
        ]
    )

    fig_region_share.update_layout(
        height=430,
        paper_bgcolor="#080D1A",
        plot_bgcolor="#111827",
        font=dict(color="#CBD5E1"),
        legend=dict(
            font=dict(color="#CBD5E1")
        ),
        margin=dict(
            l=20,
            r=20,
            t=30,
            b=20
        )
    )

    fig_region_share.update_traces(
        textinfo="percent+label",
        hovertemplate=(
            "<b>%{label}</b><br>"
            "Sales: ₹%{value:,.0f}<br>"
            "Share: %{percent}"
            "<extra></extra>"
        )
    )

    st.plotly_chart(
        fig_region_share,
        use_container_width=True
    )


# ============================================================
# EMPLOYEE INTELLIGENCE
# ============================================================

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("👨‍💼 Employee Intelligence")

if not employee_sales.empty:

    employee_intel = employee_sales.copy()

    employee_total = employee_intel["Primary_Sales"].sum()

    employee_intel["Contribution_%"] = (
        employee_intel["Primary_Sales"]
        / employee_total
        * 100
        if employee_total != 0
        else 0
    )

    employee_intel["Rank"] = range(
        1,
        len(employee_intel) + 1
    )

    top_employee_row = employee_intel.iloc[0]

    ei1, ei2, ei3 = st.columns(3)

    with ei1:
        render_metric_card(
            "🥇 Top Employee",
            str(top_employee_row["Employee_ID"]),
            accent="#06B6D4"
        )

    with ei2:
        render_metric_card(
            "💰 Top Employee Sales",
            f"₹{top_employee_row['Primary_Sales'] / 1e6:,.2f}M",
            accent="#A855F7"
        )

    with ei3:
        render_metric_card(
            "📊 Top Employee Contribution",
            f"{top_employee_row['Contribution_%']:.2f}%",
            accent="#10B981"
        )

    employee_chart = employee_intel.head(10).sort_values(
        "Primary_Sales"
    )

    fig_employee_intel = px.bar(
        employee_chart,
        x="Primary_Sales",
        y="Employee_ID",
        orientation="h",
        text_auto=".2s",
        color="Primary_Sales",
        color_continuous_scale=[
            "#1D4ED8",
            "#3B82F6",
            "#60A5FA"
        ]
    )

    fig_employee_intel.update_layout(
        height=450,
        paper_bgcolor="#080D1A",
        plot_bgcolor="#111827",
        font=dict(color="#CBD5E1"),
        coloraxis_showscale=False,
        xaxis=dict(
            title="Primary Sales",
            gridcolor="#263244"
        ),
        yaxis=dict(
            title="Employee",
            gridcolor="#263244"
        )
    )

    st.plotly_chart(
        fig_employee_intel,
        use_container_width=True
    )

    employee_table = employee_intel.copy()

    employee_table["Primary_Sales"] = (
        employee_table["Primary_Sales"] / 1e6
    ).round(2)

    employee_table["Contribution_%"] = (
        employee_table["Contribution_%"]
    ).round(2)

    employee_table = employee_table[
        [
            "Rank",
            "Employee_ID",
            "Primary_Sales",
            "Contribution_%"
        ]
    ].rename(
        columns={
            "Primary_Sales": "Sales (₹M)",
            "Contribution_%": "Contribution %"
        }
    )

    render_pro_table(employee_table)


# Safe defaults used by the AI sections
if "mom_growth" not in globals():
    mom_growth = None

if "yoy_growth" not in globals():
    yoy_growth = None


# ============================================================
# AUTOMATIC EXECUTIVE SUMMARY
# ============================================================

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("📋 Executive Summary")

if not filtered_sales.empty:

    summary_region = (
        best_region_row["Region"]
        if best_region_row is not None
        else "N/A"
    )

    summary_category = (
        best_category_row["Category"]
        if best_category_row is not None
        else "N/A"
    )

    summary_employee = (
        top_employee_row["Employee_ID"]
        if not employee_sales.empty
        else "N/A"
    )

    if achievement >= 100:
        achievement_message = (
            f"Sales are above target by "
            f"₹{(primary_sales - target_value) / 1e6:,.2f}M."
        )
    else:
        achievement_message = (
            f"Sales are below target by "
            f"₹{(target_value - primary_sales) / 1e6:,.2f}M."
        )

    st.markdown(
        f"""
        <div class="info-box">

        <b>Business Snapshot</b><br><br>

        • Primary Sales: <b>₹{primary_sales / 1e6:,.2f}M</b><br>
        • Target: <b>₹{target_value / 1e6:,.2f}M</b><br>
        • Achievement: <b>{achievement:.2f}%</b><br>
        • {achievement_message}<br>
        • Strongest Region: <b>{summary_region}</b><br>
        • Leading Category: <b>{summary_category}</b><br>
        • Top Employee: <b>{summary_employee}</b>

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# AUTOMATIC AI EXECUTIVE BRIEF
# ============================================================

st.divider()

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("🤖 Automatic AI Executive Brief")

st.caption(
    "AI-generated management insights based on the currently selected filters."
)


def build_executive_brief_prompt():

    strongest_region = (
        region_sales.iloc[0]["Region"]
        if not region_sales.empty
        else "N/A"
    )

    strongest_region_sales = (
        region_sales.iloc[0]["Primary_Sales"]
        if not region_sales.empty
        else 0
    )

    weakest_region = (
        region_sales.iloc[-1]["Region"]
        if not region_sales.empty
        else "N/A"
    )

    weakest_region_sales = (
        region_sales.iloc[-1]["Primary_Sales"]
        if not region_sales.empty
        else 0
    )

    strongest_category = (
        category_sales.iloc[0]["Category"]
        if not category_sales.empty
        else "N/A"
    )

    strongest_category_sales = (
        category_sales.iloc[0]["Primary_Sales"]
        if not category_sales.empty
        else 0
    )

    weakest_category = (
        category_sales.iloc[-1]["Category"]
        if not category_sales.empty
        else "N/A"
    )

    weakest_category_sales = (
        category_sales.iloc[-1]["Primary_Sales"]
        if not category_sales.empty
        else 0
    )

    top_employee = (
        employee_sales.iloc[0]["Employee_ID"]
        if not employee_sales.empty
        else "N/A"
    )

    top_employee_sales = (
        employee_sales.iloc[0]["Primary_Sales"]
        if not employee_sales.empty
        else 0
    )

    if "mom_growth" in globals():
        mom_value = mom_growth
    else:
        mom_value = None

    if "yoy_growth" in globals():
        yoy_value = yoy_growth
    else:
        yoy_value = None

    if achievement >= 100:
        performance = "Above Target"
    elif achievement >= 90:
        performance = "Near Target"
    else:
        performance = "Below Target"

    return f"""
You are the Executive AI Analyst for a sales organization.

Create a concise management brief using ONLY the verified data below.

CURRENT PERFORMANCE

Primary Sales: ₹{primary_sales / 1e6:,.2f}M
Target: ₹{target_value / 1e6:,.2f}M
Achievement: {achievement:.2f}%
Target Gap / Surplus: ₹{(primary_sales - target_value) / 1e6:,.2f}M
Performance Status: {performance}
Secondary Sales: ₹{secondary_sales / 1e6:,.2f}M
Orders: {orders:,}
Units: {units:,}

GROWTH

MoM Growth: {f"{mom_value:+.2f}%" if mom_value is not None else "N/A"}
YoY Growth: {f"{yoy_value:+.2f}%" if yoy_value is not None else "N/A"}

REGION

Strongest Region: {strongest_region}
Strongest Region Sales: ₹{strongest_region_sales / 1e6:,.2f}M

Weakest Region: {weakest_region}
Weakest Region Sales: ₹{weakest_region_sales / 1e6:,.2f}M

REGIONAL TABLE

{region_sales.to_string(index=False)}

CATEGORY

Strongest Category: {strongest_category}
Strongest Category Sales: ₹{strongest_category_sales / 1e6:,.2f}M

Weakest Category: {weakest_category}
Weakest Category Sales: ₹{weakest_category_sales / 1e6:,.2f}M

CATEGORY TABLE

{category_sales.to_string(index=False)}

TOP EMPLOYEE

{top_employee}
Sales: ₹{top_employee_sales / 1e6:,.2f}M

TOP EMPLOYEE TABLE

{employee_sales.head(10).to_string(index=False)}

RULES

1. Use ONLY the supplied data.
2. Never invent numbers.
3. Never claim a cause unless the data directly supports it.
4. Clearly distinguish facts from interpretation.
5. Do not make unsupported assumptions.
6. Focus on management-relevant insights.
7. Keep the response concise.

RETURN EXACTLY THIS STRUCTURE:

### Executive Summary
2-3 sentences.

### 🟢 Opportunities
Give the 2 most important data-supported opportunities.

### 🔴 Risks / Attention Areas
Give the 2 most important data-supported risks or attention areas.

### 🎯 Recommended Actions
Give 3 practical actions based only on the data.
"""


# Generate automatically only when the user clicks the button.
if st.button(
    "✨ Generate Executive AI Brief",
    type="secondary"
):

    if filtered_sales.empty:

        st.warning(
            "No sales data available for the selected filters."
        )

    else:

        with st.spinner(
            "🤖 AI is preparing the executive brief..."
        ):

            try:

                executive_prompt = (
                    build_executive_brief_prompt()
                )

                executive_answer = ask_ai(
                    executive_prompt
                )

                st.markdown(
                    """
                    <div class="ai-box">
                        <div style="
                            font-size:1.35rem;
                            font-weight:750;
                            color:#F8FAFC;
                        ">
                            💡 Executive AI Brief
                        </div>
                        <div style="
                            color:#A5B4FC;
                            margin-top:6px;
                        ">
                            Based on the current dashboard filters
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.write(
                    executive_answer
                )

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Gemini AI is unavailable. Please check your Gemini API key and Streamlit Secrets."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⏳ AI response timed out. Please try again."
                )

            except Exception as e:

                st.error(
                    f"❌ Executive AI analysis failed: {e}"
                )


# ============================================================
# AI SALES INTELLIGENCE
# ============================================================

st.header("🧠 AI Sales Intelligence")

st.markdown(
    """
    <div class="ai-box">
        <div style="font-size:1.35rem;font-weight:750;color:#F8FAFC;">
            🤖 AI Business Analyst
        </div>
        <div style="color:#A5B4FC;margin-top:6px;">
            Ask the AI to explain performance, identify risks,
            find opportunities or recommend management actions.
        </div>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# QUICK AI ANALYSIS
# ============================================================

st.markdown("**⚡ Quick Analysis**")

# Store the selected quick question in session state.
# This is important because Streamlit reruns the script whenever
# a button is clicked.
if "ai_question" not in st.session_state:
    st.session_state.ai_question = ""

if "run_ai_analysis" not in st.session_state:
    st.session_state.run_ai_analysis = False

if "quick_analysis_type" not in st.session_state:
    st.session_state.quick_analysis_type = ""


def set_quick_question(question, analysis_type):
    """
    Set the question and immediately trigger the AI analysis.
    The callback runs before Streamlit reruns the page.
    """
    st.session_state.ai_question = question
    st.session_state.quick_analysis_type = analysis_type
    st.session_state.run_ai_analysis = True


q1, q2, q3, q4 = st.columns(4)

with q1:
    st.button(
        "📊 Executive Summary",
        key="quick_executive_summary",
        use_container_width=True,
        on_click=set_quick_question,
        args=(
            "Give me an executive summary of the current sales performance.",
            "Executive Summary",
        ),
    )

with q2:
    st.button(
        "⚠️ Find Risks",
        key="quick_find_risks",
        use_container_width=True,
        on_click=set_quick_question,
        args=(
            "Identify the biggest business risks in the current filtered sales data. Rank the risks by importance and explain the data evidence for each risk.",
            "Risk Analysis",
        ),
    )

with q3:
    st.button(
        "🚀 Find Opportunities",
        key="quick_find_opportunities",
        use_container_width=True,
        on_click=set_quick_question,
        args=(
            "Identify the biggest sales opportunities in the current filtered data. Rank the opportunities by importance and explain the data evidence for each opportunity.",
            "Opportunity Analysis",
        ),
    )

with q4:
    st.button(
        "🎯 Target Analysis",
        key="quick_target_analysis",
        use_container_width=True,
        on_click=set_quick_question,
        args=(
            "Analyze target achievement using the current filtered data. Explain actual sales, target, achievement percentage, target gap or surplus, and what management should do next.",
            "Target Analysis",
        ),
    )


user_question = st.text_area(
    "💬 Ask your own question",
    key="ai_question",
    placeholder=(
        "Example: Which region needs attention and what should "
        "management do about it?"
    ),
    height=110,
)


# Manual AI button
manual_analyze = st.button(
    "🚀 Analyze with AI",
    type="primary",
    key="manual_ai_analysis",
    use_container_width=False,
)


# A quick-analysis button sets run_ai_analysis=True.
# The normal Analyze button also sets it for manual questions.
should_analyze = (
    st.session_state.get("run_ai_analysis", False)
    or manual_analyze
)


if should_analyze:

    if not user_question.strip():

        st.warning(
            "Please enter a question first."
        )

    elif filtered_sales.empty:

        st.warning(
            "No sales data available for the selected filters."
        )

    else:

        # ----------------------------------------------------
        # Format all sales context in ₹M before sending to AI.
        # This prevents Google Gemini from answering with raw/scientific
        # notation such as ₹1.812879e+09.
        # ----------------------------------------------------

        region_ai = region_sales.copy()
        region_ai["Primary_Sales"] = (
            region_ai["Primary_Sales"] / 1e6
        ).round(2)
        region_ai = region_ai.rename(
            columns={"Primary_Sales": "Sales (₹M)"}
        )

        category_ai = category_sales.copy()
        category_ai["Primary_Sales"] = (
            category_ai["Primary_Sales"] / 1e6
        ).round(2)
        category_ai = category_ai.rename(
            columns={"Primary_Sales": "Sales (₹M)"}
        )

        employee_ai = employee_sales.head(10).copy()
        employee_ai["Primary_Sales"] = (
            employee_ai["Primary_Sales"] / 1e6
        ).round(2)
        employee_ai = employee_ai.rename(
            columns={"Primary_Sales": "Sales (₹M)"}
        )

        region_context = region_ai.to_string(index=False)
        category_context = category_ai.to_string(index=False)
        employee_context = employee_ai.to_string(index=False)

        growth_context = (
            growth_monthly.tail(12).to_string(index=False)
            if "growth_monthly" in globals()
            else "Growth data unavailable."
        )

        filter_context = f"""
Date Range:
{date_range}

Employees:
{selected_employees if selected_employees else "All"}

Regions:
{selected_regions if selected_regions else "All"}

States:
{selected_states if selected_states else "All"}

Categories:
{selected_categories if selected_categories else "All"}
"""

        analysis_type = st.session_state.get(
            "quick_analysis_type",
            ""
        )

        prompt = f"""
You are an expert Business Intelligence and Sales Strategy Analyst.

Use ONLY the verified data supplied below.

ACTIVE FILTERS
{filter_context}

ANALYSIS TYPE
{analysis_type if analysis_type else "User Question"}

CURRENT KPIs
Primary Sales: ₹{primary_sales / 1e6:,.2f}M
Secondary Sales: ₹{secondary_sales / 1e6:,.2f}M
Target: ₹{target_value / 1e6:,.2f}M
Achievement: {achievement:.2f}%
Target Gap/Surplus: ₹{(primary_sales - target_value) / 1e6:,.2f}M
Orders: {orders:,}
Units: {units:,}

REGIONAL SALES
{region_context}

CATEGORY SALES
{category_context}

TOP EMPLOYEES
{employee_context}

RECENT MONTHLY SALES / GROWTH
{growth_context}

USER QUESTION
{user_question}

RULES
1. Answer the question directly.
2. Use actual numbers from the data.
3. Do not invent facts, causes, targets or numbers.
4. Separate data-supported facts from interpretation.
5. Identify risks and opportunities only when supported by the data.
6. Give practical management actions.
7. Keep the response concise and professional.
8. ALWAYS express every sales/revenue/target/gap amount in ₹M.
9. NEVER use scientific notation such as 1.812879e+09.
10. NEVER output raw rupee values for sales. Convert them to ₹M.
11. Use exactly 2 decimal places for ₹M values, e.g. ₹1,812.88M.
12. Orders and Units should remain whole numbers.

FORMAT

### Executive Answer
Direct answer in 2-4 sentences.

### Data Evidence
3-5 bullet points with actual numbers.

### Key Insight
Explain what the data indicates.

### Recommended Actions
3 practical actions.
"""

        with st.spinner(
            "🤖 AI is analyzing current sales performance..."
        ):

            try:

                answer = ask_ai(prompt)

                # Final safety formatting:
                # Convert scientific-notation / raw ₹ sales amounts
                # returned by the local LLM into ₹M.
                def normalize_ai_sales_units(text):
                    def sci_currency(match):
                        value = float(match.group(1))
                        return f"₹{value / 1e6:,.2f}M"

                    def raw_currency(match):
                        value = float(
                            match.group(1).replace(",", "")
                        )
                        return f"₹{value / 1e6:,.2f}M"

                    # ₹1.812879e+09 / ₹1.812879E+09
                    text = re.sub(
                        r"₹\s*([0-9]+(?:\.[0-9]+)?[eE][+-]?[0-9]+)",
                        sci_currency,
                        text
                    )

                    # ₹1812879000.00 or ₹1,812,879,000
                    text = re.sub(
                        r"₹\s*([0-9][0-9,]*(?:\.[0-9]+)?)",
                        raw_currency,
                        text
                    )

                    return text

                answer = normalize_ai_sales_units(answer)

                # Show which quick analysis was requested.
                display_type = (
                    analysis_type
                    if analysis_type
                    else "Custom AI Analysis"
                )

                st.markdown(
                    f"""
                    <div class="ai-box">
                        <div style="
                            font-size:1.35rem;
                            font-weight:750;
                            color:#F8FAFC;
                        ">
                            💡 {html.escape(display_type)}
                        </div>
                        <div style="
                            color:#A5B4FC;
                            margin-top:6px;
                        ">
                            Based on the current dashboard filters
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

                st.write(answer)

            except requests.exceptions.ConnectionError:

                st.error(
                    "❌ Gemini AI is unavailable. Please check your Gemini API key and Streamlit Secrets."
                )

            except requests.exceptions.Timeout:

                st.error(
                    "⏳ AI response timed out. Please try again."
                )

            except Exception as e:

                st.error(
                    f"❌ AI analysis failed: {e}"
                )

    # Reset the trigger after this run.
    # This prevents the same AI request from executing again
    # on the next unrelated Streamlit rerun.
    st.session_state.run_ai_analysis = False


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '<div class="footer-note">AI Sales Intelligence Dashboard • Built with ❤️ using Excel, Python, Streamlit, Plotly & Google Gemini</div>',
    unsafe_allow_html=True
)


# ============================================================
# PORTFOLIO / DATA EXPORT
# ============================================================

st.divider()

st.markdown('<div class="section-divider"></div>', unsafe_allow_html=True)

st.header("📥 Export & Project Information")

export_col1, export_col2 = st.columns([1, 2])

with export_col1:

    export_data = filtered_sales.copy()

    csv_data = export_data.to_csv(index=False).encode("utf-8")

    st.download_button(
        "⬇️ Download Filtered Sales CSV",
        data=csv_data,
        file_name="filtered_sales_data.csv",
        mime="text/csv",
        use_container_width=True
    )

with export_col2:

    st.markdown(
        """
        <div class="info-box">
            <b>AI Sales Intelligence</b><br><br>
            Portfolio project demonstrating interactive sales analytics,
            dynamic filtering, KPI intelligence, growth analysis,
            drill-down reporting and local LLM-powered business insights.
        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# FOOTER
# ============================================================

st.divider()

st.markdown(
    '<div class="footer-note">AI Sales Intelligence Dashboard • Built with ❤️ using Excel, Python, Streamlit, Plotly & Google Gemini</div>',
    unsafe_allow_html=True
)

