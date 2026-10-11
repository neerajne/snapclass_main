import streamlit as st

try:
    from supabase import create_client, Client
except Exception:
    import traceback

    st.code(traceback.format_exc())
    st.stop()

supabase: Client = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])