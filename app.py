import streamlit as st
import pandas as pd
import datetime

# Page Configuration
st.set_page_config(
    page_title="Manish's Financial & Trading Intelligence Hub",
    page_icon="📈",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a module", [
    "Daily Market Intelligence",
    "Top Gainers & Losers Analysis",
    "Trading Journal",
    "Trading & Finance Education"
])

# --- PAGE 1: DAILY MARKET INTELLIGENCE ---
if page == "Daily Market Intelligence":
    st.title("📊 Daily Financial Market Intelligence Centre")
    st.markdown(f"*Today's Date: {datetime.date.today().strftime('%B %d, %Y')}*")
    
    st.subheader("1. What Changed Since Yesterday?")
    st.info("Use this section to record global overnight cues, Federal Reserve/RBI updates, and major macroeconomic shifts.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("NIFTY 50", "24,350.20", "+0.45%")
    col2.metric("BANK NIFTY", "52,120.80", "+0.78%")
    col3.metric("India VIX", "13.45", "-2.10%")
    
    st.markdown("---")
    st.subheader("Structured Analyst Breakdown")
    news_headline = st.text_input("Enter Key News Headline:", "RBI maintains repo rate at 6.5% with a neutral stance.")
    
    with st.expander("View 14-Point Analyst Breakdown Framework", expanded=True):
        st.markdown("**1. NEWS:** " + news_headline)
        st.markdown("**2. FACT:** Monetary Policy Committee voted unanimously to hold rates.")
        st.markdown("**3. ROOT CAUSE:** Inflation converging towards the 4% target but food price volatility remains a transient risk.")
        st.markdown("**4. MECHANISM:** Stable rates $\rightarrow$ Lower cost of capital borrowing pressure $\rightarrow$ Supportive for Banking, Auto, and Real Estate sectors.")
        st.markdown("**5. TRADER'S PERSPECTIVE:** Neutral-to-bullish for rate-sensitive stocks; focus on price action near major support zones.")

# --- PAGE 2: TOP GAINERS & LOSERS ---
elif page == "Top Gainers & Losers Analysis":
    st.title("🔥 Daily Top Movers & Root Cause Analysis")
    st.markdown("Track the top 10 gainers and losers of the day along with the underlying fundamental or technical catalyst.")
    
    tab1, tab2 = st.tabs(["Top Gainers", "Top Losers"])
    
    with tab1:
        st.subheader("Top 10 Gainers (NIFTY 500 / F&O)")
        gainers_data = {
            "Stock": ["TATASTEEL", "INFY", "AXISBANK", "RELIANCE", "SUNPHARMA"],
            "Change (%)": ["+4.2%", "+3.5%", "+2.9%", "+2.4%", "+2.1%"],
            "Primary Catalyst": ["Strong European demand outlook", "Large deal win announced", "Block deal institutional buying", "Energy margin expansion", "USFDA approval clearance"]
        }
        st.table(pd.DataFrame(gainers_data))
        
    with tab2:
        st.subheader("Top 10 Losers (NIFTY 500 / F&O)")
        losers_data = {
            "Stock": ["HINDUNILVR", "ITC", "TITAN", "NTPC", "MARUTI"],
            "Change (%)": ["-2.1%", "-1.8%", "-1.5%", "-1.3%", "-1.1%"],
            "Primary Catalyst": ["Rural volume growth concerns", "Higher input raw material costs", "Weak discretionary retail demand", "Profit booking after recent rally", "Supply chain component delay"]
        }
        st.table(pd.DataFrame(losers_data))

# --- PAGE 3: TRADING JOURNAL ---
elif page == "Trading Journal":
    st.title("📓 My Trading Journal & Performance Review")
    st.markdown("Log your trades, evaluate execution discipline, and separate process from outcome.")
    
    with st.form("journal_form"):
        col1, col2 = st.columns(2)
        with col1:
            trade_date = st.date_input("Trade Date")
            instrument = st.text_input("Instrument (e.g., NIFTY 24500 CE)")
            setup_type = st.selectbox("Strategy Setup", ["Opening Range Breakout (ORB)", "Support/Resistance Rejection", "Trend Continuation", "Mean Reversion"])
            entry_price = st.number_input("Entry Price")
            stop_loss = st.number_input("Stop Loss")
        with col2:
            target_price = st.number_input("Target Price")
            position_size = st.number_input("Position Size / Quantity")
            pnl = st.number_input("Realized P&L (₹)")
            followed_rules = st.selectbox("Did I follow my trading rules?", ["Yes", "No - Broke Rules"])
            
        emotion = st.selectbox("Emotional State", ["Calm & Patient", "Anxious / FOMO", "Rushed", "Revenge Trading Tendency"])
        notes = st.text_area("Lessons Learned & Mistake Analysis")
        
        submitted = st.form_submit_button("Save Trade Entry")
        if submitted:
            st.success(f"Trade for {instrument} logged successfully! Discipline check: {followed_rules}.")

# --- PAGE 4: EDUCATION HUB ---
elif page == "Trading & Finance Education":
    st.title("📚 Trading & Finance Knowledge Base")
    st.markdown("Structured learning modules combining technical analysis, institutional behavior, and corporate finance.")
    
    module = st.selectbox("Select Learning Module", [
        "Module 1: Market Structure & Liquidity",
        "Module 2: Price Action & Candlestick Mechanics",
        "Module 3: Futures & Options Greeks",
        "Module 4: Financial Statement & WACC Analysis"
    ])
    
    if "Module 1" in module:
        st.subheader("Module 1: Understanding Market Structure & Liquidity")
        st.write("""
        **1. Concept:** Market structure defines how price moves through swing highs and swing lows, indicating trend direction (Higher Highs/Higher Lows in an uptrend).
        
        **2. Why it matters:** Retail traders often look at indicators in isolation, whereas institutional players look at liquidity pools (where stop-losses sit above swing highs or below swing lows).
        
        **3. Practical Application:** Never enter a breakout blindly without checking if liquidity has been built up and swept prior to expansion.
        """)