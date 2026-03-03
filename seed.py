import requests, sys

BASE = "http://127.0.0.1:5000"

USERS = [
    {"username": "faculty1", "name": "Dr. Smith",     "role": "faculty", "password": "faculty123", "email": "smith@college.edu"},
    {"roll_number": "CS2024001", "username": "CS2024001", "name": "Mohan Saini", "role": "student", "password": "student123"},
    {"roll_number": "CS2024002", "username": "CS2024002", "name": "Anshul Kapil",  "role": "student", "password": "student123"},
    {"roll_number": "CS2024003", "username": "CS2024003", "name": "Shivam", "role": "student", "password": "student123"},
{"roll_number": "CS2024004", "username": "CS2024004", "name": "Rohit", "role": "student", "password": "student123"},
  {"roll_number": "CS2024005", "username": "CS2024005", "name": "Rahul", "role": "student", "password": "student123"},
   
    ]

print(f"Seeding {len(USERS)} users...\n")
for u in USERS:
    try:
        r = requests.post(f"{BASE}/api/auth/register", json=u, timeout=10)
        icon = "✅" if r.status_code in (201, 409) else "❌"
        print(f"{icon} [{r.status_code}] {u.get('name'):20s} ({u.get('role'):7s}) → {r.json().get('message') or r.json().get('error')}")
    except Exception as e:
        print(f"❌ {e}"); sys.exit(1)

print("\n✅ Done!")
print("  Faculty  → username: faculty1   | password: faculty123")
print("  Student  → roll no:  CS2024001  | password: student123")