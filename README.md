# ExamPro – Online Examination System

## Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Edit .env — add your real MongoDB Atlas URI
# 3. Start server
python app.py

# 4. Open new terminal — seed users
python seed.py

# 5. Open browser
# http://localhost:5000/login
```

## Credentials

| Role    | Field      | Value       | Password     |
|---------|-----------|-------------|--------------|
| Faculty | Username  | `faculty1`  | `faculty123` |
| Student | Roll No.  | `CS2024001` | `student123` |
| Student | Roll No.  | `CS2024002` | `student123` |
| Student | Roll No.  | `CS2024003` | `student123` |

## Project Structure

```
project/
├── app.py
├── .env
├── requirements.txt
├── seed.py
├── README.md
├── flask_session/          ← auto-created
├── templates/
│   ├── login.html
│   ├── student_dashboard.html
│   ├── faculty_dashboard.html
│   ├── exam.html
│   ├── answer_checking.html
│   ├── results.html
│   ├── ranking.html
│   └── analytics.html
└── static/js/
    ├── app.js
    ├── exam.js
    ├── proctor.js
    ├── notifications.js
    └── toast.js
```