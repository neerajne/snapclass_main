import streamlit as st


def style_background_home():
    st.markdown(
        """
        <style>
            .stApp {
                background: #5865F2 !important;
            }
            .stApp div[data-testid='stColumn']{
            background-color : #E0E3FF !important;
            padding:2.5rem !important;
            border-radius:5rem !important;
            }
            .stApp div[data-testid='stColumn'] h2 {
    color: #303246 !important;
}

        </style>
        """,
        unsafe_allow_html=True,
    )


def style_background_dashboard():
    st.markdown(
        """
        <style>
        .stApp {
                        background: #E0E3FF !important;
                    }
        </style>
        """,
        unsafe_allow_html=True,
    )


def style_base_layout():
    st.markdown(
        """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            h1{
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 3.5rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }
            h2 {
                font-family: 'Climate Crisis', sans-serif !important;
                font-size: 1.5rem !important;
                line-height: 0.9 !important;
                margin-bottom: 0rem !important;
            }

            h3,h4,p{
                font-family : 'Outfit',sans-serif !important;
            }

            button[kind="primary"] {
                border-radius: 1.5rem !important;
                background: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="secondary"] {
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind="tertiary"] {
                border-radius: 1.5rem !important;
                background: black !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }
            button:hover{
                transform:scale(1.05)!important;
            }

            /* Text input wrapper (removes black border) */
            .stTextInput div[data-baseweb="input"] {
                background-color: #F0F1FA !important;
                border-radius: 1.2rem !important;
                border: none !important;
                box-shadow: none !important;
            }

            .stTextInput div[data-baseweb="base-input"] {
                background-color: #F0F1FA !important;
                border: none !important;
            }

            .stTextInput input {
                background-color: #F0F1FA !important;
                color: #303246 !important;
                border: none !important;
                box-shadow: none !important;
                padding: 12px 16px !important;
            }

            .stTextInput input::placeholder {
                color: #9999A8 !important;
            }

            /* Password show/hide icon button */
            .stTextInput button[title="Show password text"],
            .stTextInput button[title="Hide password text"] {
                background: #5865F2 !important;
                border-radius: 0.8rem !important;
                border: none !important;
                margin-right: 6px !important;
                padding: 8px 10px !important;
            }

            /* Password eye button (new Streamlit) */
            .stTextInput div[data-baseweb="input"] button,
            .stTextInput [data-testid="stTextInputRootElement"] button {
                background: #5865F2 !important;
                border-radius: 0.8rem !important;
                border: none !important;
                margin-right: 6px !important;
                padding: 8px 10px !important;
            }

            .stTextInput div[data-baseweb="input"] button svg,
            .stTextInput [data-testid="stTextInputRootElement"] button svg {
                fill: white !important;
                color: white !important;
            }

            /* Camera input - Take Photo button */
            [data-testid="stCameraInputWebcamStyledButton"],
            .stCameraInput button {
                background: #5865F2 !important;
                color: white !important;
                border-radius: 1.5rem !important;
                border: none !important;
                padding: 10px 20px !important;
                transition: transform 0.25s ease-in-out !important;
            }

            [data-testid="stCameraInputWebcamStyledButton"]:hover,
            .stCameraInput button:hover {
                transform: scale(1.05) !important;
            }
            .stTextInput button svg {
                fill: white !important;
            }

            /* Labels above inputs */
            .stTextInput label p {
                font-family: 'Outfit', sans-serif !important;
                font-size: 0.85rem !important;
                color: #303246 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )