import streamlit as st
from src.database.db import create_subject
from src.pipelines.voice_pipeline import process_bulk_audio
from src.database.config import supabase
from datetime import datetime
import pandas as pd
from src.components.dialog_attendence_result import show_attendence_results


@st.dialog("Voice Attendence")
def voice_attendence_dialog(selected_subject_id):
    st.write("Record students saying “I am present”, then let AI recognize them.")

    audio_data = st.audio_input("Record audio")

    if st.button("Analyse audio", type="primary", width="stretch"):
        if audio_data is None:
            st.warning("Please record audio first.")
            return

        with st.spinner("Processing audio"):
            enrolled_res = (
                supabase.table("subject_students")
                .select("*,students(*)")
                .eq("subject_id", selected_subject_id)
                .execute()
            )
            enrolled_students = enrolled_res.data
            if not enrolled_students:
                st.warning("No data available")
                return

            candidates_dict = {
                s["students"]["student_id"]: s["students"]["voice_embedding"]
                for s in enrolled_students
                if s["students"].get("voice_embedding")
            }

            if not candidates_dict:
                st.error("No voice profiles are registered for the enrolled students.")
                return

            audio_bytes = audio_data.read()
            detected_scores = process_bulk_audio(audio_bytes, candidates_dict)

            results, attendance_to_log = [], []

            current_timestamp = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

            for node in enrolled_students:
                student = node["students"]
                score = detected_scores.get(student["student_id"], 0.0)
                is_present = bool(score > 0)

                results.append(
                    {
                        "Name": student["name"],
                        "ID": student["student_id"],
                        "Source": score if is_present else "_",
                        "Status": ("✅ Present" if is_present else "❌ Absent"),
                    }
                )

                attendance_to_log.append(
                    {
                        "student_id": student["student_id"],
                        "subject_id": selected_subject_id,
                        "timestamp": current_timestamp,
                        "is_present": bool(is_present),
                    }
                )

            st.session_state.voice_attendence_results = (
                pd.DataFrame(results),
                attendance_to_log,
            )

    if st.session_state.get("voice_attendence_results"):
        st.divider()
        df_results, logs = st.session_state.voice_attendence_results
        show_attendence_results(df_results, logs)
