# SnapClass – AI Attendance System

A web app that takes classroom attendance using face recognition and voice verification. Built with Streamlit and Supabase, using dlib face embeddings, a scikit-learn classifier and Resemblyzer voice embeddings.

**Live demo:** https://snapclass-neeraj-main.streamlit.app
(Free hosting. If the app is asleep, click "Yes, get this app back up!" and wait 1-2 minutes.)

## What it does

1. Students sign in with their face (webcam). New students register with their name and, optionally, a voice sample.
2. Teachers sign up and log in with a username and password, then create subjects. Each subject gets a join code, a shareable link and a QR code.
3. Students enroll in a subject by entering the code, or by opening the join link or scanning the QR.
4. Teachers pick a subject, upload or capture classroom photos, and run face analysis. The app detects every enrolled student in the photos and marks them present or absent.
5. Teachers can also take attendance by voice, and the results are saved to the database.
6. Students see their enrolled subjects with total classes and classes attended.

## Tech stack

- **Frontend:** Streamlit
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

<img width="1515" height="1038" alt="Attendance_records" src="https://github.com/user-attachments/assets/e8d60adc-963b-44f0-aca2-64952c17d3b1" />
