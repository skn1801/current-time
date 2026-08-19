import streamlit as st
import datetime
import time

st.set_page_config(page_title="Current Time", page_icon="🕒")

st.title("🕒 Current Time")

# Placeholder for the time so it can be updated
placeholder = st.empty()

# Option to auto-refresh
auto_refresh = st.checkbox("Auto-refresh every second", value=True)

if st.button("Refresh now"):
    st.rerun()

if auto_refresh:
    for _ in range(3600):  # runs for up to an hour before needing manual refresh
        now = datetime.datetime.now()
        placeholder.markdown(
            f"""
            <div style="text-align:center;">
                <h1 style="font-size:60px;">{now.strftime('%H:%M:%S')}</h1>
                <p style="font-size:20px; color:gray;">{now.strftime('%A, %B %d, %Y')}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        time.sleep(1)
else:
    now = datetime.datetime.now()
    placeholder.markdown(
        f"""
        <div style="text-align:center;">
            <h1 style="font-size:60px;">{now.strftime('%H:%M:%S')}</h1>
            <p style="font-size:20px; color:gray;">{now.strftime('%A, %B %d, %Y')}</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
