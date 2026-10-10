import streamlit as st


def footer_home():

    st.markdown(
        """
        <div style ="margin-top :2rem;display:flex;justify-content:center;align-items:center;">
        <p style =" font-weight : bold; color:white;">&copy; 2026 snapclass.All right reserved.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )


def footer_dashboard():

    st.markdown(
        """
        <div style ="margin-top :2rem;display:flex;justify-content:center;align-items:center;">
        <p style =" font-weight : bold; color:black;">&copy; 2026 snapclass.All right reserved.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
