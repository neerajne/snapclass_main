import streamlit as st

try:
    from supabase import create_client, Client
except Exception:
    import sys
    import traceback
    from importlib.metadata import distributions

    st.code(traceback.format_exc())
    st.write("Python:", sys.executable, sys.version)
    names = sorted(d.metadata["Name"] for d in distributions() if d.metadata["Name"])
    st.write("Installed packages:", names)
    st.stop()

supabase: Client = create_client(st.secrets["SUPABASE_URL"], st.secrets["SUPABASE_KEY"])
