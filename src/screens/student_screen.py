import streamlit as st
import numpy as np
from PIL import Image
from src.components.header import header_dashboard
from src.ui.base_layout import (
    style_background_dashboard,
    style_base_layout,
)
from src.components.footer import footer_dashboard
from src.pipelines.face_pipeline import (
    predict_attendance,
    get_face_embeddings,
    train_classifier,
)
from src.pipelines.voice_pipeline import get_voice_embedding
from src.database.db import get_all_students, create_student
from src.components.dialog_enroll import enroll_dialog

from src.database.db import get_student_subjects
from src.database.db import get_student_attendence
from src.components.subject_card import subject_card
from src.database.db import unenroll_student_to_subject
import time


def student_dashboard():
    student_data = st.session_state.user_data
    student_id = student_data["student_id"]
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")
    with c1:
        header_dashboard()
    with c2:
        st.subheader(f"Welcome, {student_data['name']}!", anchor=False)
        if st.button(
            "Logout",
            type="secondary",
            key="loginbckbtn",
            shortcut="control+backspace",
        ):
            st.session_state["is_logged_in"] = False
            del st.session_state["user_data"]
            st.session_state["login_type"] = None
            st.rerun()

    st.space()

    c1, c2 = st.columns(2)
    with c1:
        st.header("Your Enrolled Subjects", anchor=False)

    with c2:
        if st.button("Enroll in Subject", type="primary", width="stretch"):
            enroll_dialog()

    st.divider()

    with st.spinner("Loading your subjects..."):
        subjects = get_student_subjects(student_id)
        logs = get_student_attendence(student_id)

    stats_map = {}

    for log in logs:
        sid = log["subject_id"]

        if sid not in stats_map:
            stats_map[sid] = {"total": 0, "attended": 0}

        stats_map[sid]["total"] += 1

        if log.get("is_present"):
            stats_map[sid]["attended"] += 1

    cols = st.columns(2)
    for i, sub_node in enumerate(subjects):
        sub = sub_node["subjects"]
        sid = sub["subject_id"]

        stats = stats_map.get(sid, {"total": 0, "attended": 0})

        def unenroll_button():
            if st.button(
                "Unenroll from this course",
                type="tertiary",
                width="stretch",
                icon=":material/delete_forever:",
                key=f"unenroll_{sid}",
            ):
                unenroll_student_to_subject(student_id, sid)
                st.toast(f'Unenrolled from {sub["name"]} successfully')
                st.rerun()

        with cols[i % 2]:
            subject_card(
                name=sub["name"],
                code=sub["subject_code"],
                section=sub["section"],
                stats=[
                    ("📅", "Total", stats["total"]),
                    ("✅", "Attended", stats["attended"]),
                ],
                footer_callback=unenroll_button,
            )

    footer_dashboard()


def student_screen():
    style_background_dashboard()
    style_base_layout()

    if "user_data" in st.session_state:
        student_dashboard()
        return
    c1, c2 = st.columns(2, vertical_alignment="center", gap="xxlarge")

    with c1:
        header_dashboard()

    with c2:
        if st.button(
            "Go Back to Home",
            type="secondary",
            key="loginbckbtn",
            shortcut="control+backspace",
        ):
            st.session_state["login_type"] = None
            st.rerun()

    st.header("Login using face id", text_alignment="center", anchor=False)
    st.space(2)

    photo_source = st.camera_input("Position your face in the center")

    show_registration = False
    if photo_source:
        img = np.array(Image.open(photo_source))

        with st.spinner("Identifying..."):
            detected, all_ids, num_faces = predict_attendance(img)

            if num_faces > 1:
                st.warning("Multiple faces found")

            if detected:
                student_id = list(detected.keys())[0]
                all_students = get_all_students()

                student = None

                for s in all_students:
                    if s["student_id"] == student_id:
                        student = s
                        break

                if student:
                    st.session_state.is_logged_in = True
                    st.session_state.user_role = "student"
                    st.session_state.user_data = student

                    st.toast(f"Welcome Back {student['name']}")

                    time.sleep(1)

                    st.rerun()

            else:
                st.info("Face not recognized ! you might be a new student")
                show_registration = True

    if show_registration:
        with st.container(border=True):
            st.header("Register new Profile", anchor=False)
            new_name = st.text_input("Enter your name", placeholder="Eg.alan ritchson")

            st.subheader("Optional : voice enrollment", anchor=False)
            st.info("Enroll your voice only attendence")

            audio_data = None

            try:
                audio_data = st.audio_input(
                    "Record a short phrase like i am present , My name is bob"
                )
            except Exception:
                st.error("Audio data failed !")

            if st.button("Create Account", type="primary"):
                if new_name:
                    with st.spinner("Creating profile... !"):
                        try:
                            img = np.array(Image.open(photo_source))
                            encodings = get_face_embeddings(img)
                            if encodings:
                                face_emb = encodings[0].tolist()

                                voice_emb = None
                                if audio_data:
                                    voice_emb = get_voice_embedding(audio_data.read())

                                response_data = create_student(
                                    new_name,
                                    face_embedding=face_emb,
                                    voice_embedding=voice_emb,
                                )

                                if response_data:
                                    train_classifier()
                                    st.session_state.is_logged_in = True
                                    st.session_state.user_role = "student"
                                    st.session_state.user_data = response_data[0]
                                    st.toast(f"Profile created Hii {new_name}")
                                    time.sleep(1)
                                    st.rerun()
                                else:
                                    st.error(
                                        "Profile creation failed (no data returned)"
                                    )
                            else:
                                st.error("No face detected, please retake the photo")
                        except Exception as e:
                            st.error(f"Error: {e}")
                else:
                    st.error("Please enter your name to register !")

    st.divider()

    btnc1, btnc2 = st.columns(2)

    with btnc1:
        if st.button(
            "Login",
            icon=":material/passkey:",
            shortcut="control+enter",
            width="stretch",
        ):
            if not photo_source:
                st.error("Please take a photo first to login!")

    with btnc2:
        if st.button(
            "Login with Password Instead",
            type="primary",
            icon=":material/passkey:",
            width="stretch",
        ):
            st.info("Password login coming soon!")

    footer_dashboard()
