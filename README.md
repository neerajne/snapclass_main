# SnapClass – AI Attendance System

A web app that takes classroom attendance using face recognition and voice verification. Built with Streamlit and Supabase, using dlib face embeddings, a scikit-learn classifier and Resemblyzer voice embeddings.

**Live demo:** https://snapclass-neeraj-main.streamlit.app
(Free hosting. If the app is asleep, click "Yes, get this app back up!" and wait 1-2 minutes.)

## What it does

1. Students sign in with their face (webcam). New students register with their name and, optionally, a voice sample.
2. An SVM classifier trained on the face embeddings stored in the database predicts which registered student the face belongs to, and the app logs in that matching student.
3. Teachers sign up and log in with a username and password, then create subjects. Each subject gets a join code, a shareable link and a QR code.
4. Students enroll in a subject by entering the code, or by opening the join link or scanning the QR.
5. Teachers pick a subject, upload or capture classroom photos, and run face analysis. The app detects every enrolled student in the photos and marks them present or absent.
6. Teachers can also take attendance by voice, and the results are saved to the database.
7. Students see their enrolled subjects with total classes and classes attended.

## Tech stack

- **Frontend:** Streamlit
- **Face recognition:** dlib (dlib-bin) face embeddings, SVM classifier (scikit-learn)
- **Face recognition:** dlib (dlib-bin), face_recognition_models, scikit-learn classifier
- **Voice recognition:** Resemblyzer, librosa, PyTorch (CPU)
- **Auth and database:** Supabase (PostgreSQL), bcrypt for teacher passwords
- **QR codes:** segno
- **Deployment:** Streamlit Community Cloud

## Project structure

```
snapclass/
├── app.py                 Entry point and routing (home, teacher, student)
├── src/
│   ├── components/        Dialogs, subject card, header, footer
│   ├── database/          Supabase client (config.py) and queries (db.py)
│   ├── pipelines/         Face and voice recognition pipelines
│   ├── screens/           Home, teacher and student screens
│   └── ui/                Shared layout and styling
├── .streamlit/
│   └── config.toml        Light theme
└── requirements.txt       Python dependencies
```

## Setup

### 1. Clone and create a virtual environment

```bash
git clone https://github.com/neerajne/snapclass_main.git
cd snapclass_main
python -m venv venv
source venv/bin/activate         # Windows (Git Bash): source venv/Scripts/activate
```

Use Python 3.12. Newer versions may not have prebuilt wheels for the face and voice packages.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

`requirements.txt` installs the CPU-only build of PyTorch to keep the deployment small.

`setuptools<70` is pinned because `face_recognition_models` depends on `pkg_resources`.

### 3. Configure secrets

Create `.streamlit/secrets.toml`:

```toml
SUPABASE_URL = "https://your-project.supabase.co"
SUPABASE_KEY = "your-supabase-key"
```

You need a Supabase project with these tables:

- `teachers`
- `students` (with `face_embedding` and `voice_embedding` columns)
- `subjects`
- `subject_students` (enrollments)
- `attendance_logs`

Never commit `secrets.toml`. It is already in `.gitignore`.

### 4. Run the app

```bash
python -m streamlit run app.py
```

The app opens at `http://localhost:8501`.

## Deployment

1. Push the repo to GitHub.
2. On Streamlit Community Cloud, create an app from the repo, branch `main`, main file `app.py`.
3. In Advanced settings, choose **Python 3.12** and paste the secrets from step 3.
4. Update `app_domain` in `src/components/dialog_share_subject.py` to your live app URL so share links and QR codes point to it.

## Notes

- The first load after the app has been idle can take a minute or two because the machine restarts and the heavy packages (PyTorch, librosa) load again.
- Face and voice data are personal data. Use test accounts and consent when trying it with real people.

## Screenshots

<img width="400" height="300" alt="Attendance_records" src="https://github.com/user-attachments/assets/e8d60adc-963b-44f0-aca2-64952c17d3b1" />
<img width="400" height="300" alt="Attendance_report" src="https://github.com/user-attachments/assets/a7f62830-e948-405b-9171-f6f44da9c75b" />
<img width="400" height="300" alt="capture_or_upload_photos" src="https://github.com/user-attachments/assets/99e29ace-d432-449e-844b-8a3a93859c4a" />
<img width="400" height="300" alt="create_new_subject" src="https://github.com/user-attachments/assets/e6980f8f-0c55-401a-bd5f-b1eca06ff8c2" />
<img width="400" height="300" alt="voice_enrollment" src="https://github.com/user-attachments/assets/dcd423f7-1f19-4d9f-9161-7fb99bcebdc0" />
<img width="400" height="300" alt="voice_attendence" src="https://github.com/user-attachments/assets/e6f71a44-f97a-4f20-b824-e79ab0874a55" />
<img width="400" height="300" alt="view_attendence" src="https://github.com/user-attachments/assets/9b8e7be2-afdd-4b65-95aa-8a0414a28e65" />
<img width="400 " height="300" alt="share_qr_code" src="https://github.com/user-attachments/assets/3bee723b-7397-4233-9829-412e77e8dec0" />
<img width="400" height="300" alt="register_teacher" src="https://github.com/user-attachments/assets/735c978d-c59c-4603-b095-202dd7a25490" />
<img width="400" height="300" alt="manage_subjects" src="https://github.com/user-attachments/assets/936bf32b-101b-49c5-a975-0feb8f2c59c6" />
<img width="400" height="300" alt="login_teacher" src="https://github.com/user-attachments/assets/306e6ace-4a06-4712-9281-f9f81eabf5f4" />
<img width="400" height="300" alt="homesnapclass" src="https://github.com/user-attachments/assets/eeab5fa8-5ff6-454b-a2b8-7c779cb3ee3e" />
<img width="400" height="300" alt="enroll_in_subject_student" src="https://github.com/user-attachments/assets/1fcad7fb-dbfe-4740-8da5-ae7a8c98074b" />



