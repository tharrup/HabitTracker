# Habit Tracker (Kivy/KivyMD)

Lightweight habit tracker with XP/leveling, reminders, and local JSON storage. Built for mobile/desktop using Kivy + KivyMD.

## Features (v0)
- Create, complete, and delete habits
- Streaks + XP system (level up as you go)
- Local JSON data store (no external DB)
- Clean KivyMD UI

## Quickstart
```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
pip install -r requirements.txt
python app/main.py
```

## Project Structure
```
app/
  main.py
  kv/
    main.kv
  assets/
    .gitkeep
tests/
  test_smoke.py
requirements.txt
```

## GitHub: First Push
```bash
git init
git add .
git commit -m "feat: initial Kivy/KivyMD habit tracker scaffold"
git branch -M main
# Create an empty repo on GitHub named HabitTracker (no README)
git remote add origin https://github.com/<your-username>/HabitTracker.git
git push -u origin main
```

## Roadmap
- Notifications (plyer)
- Weekly insights dashboard
- Import/export JSON
- Optional cloud sync

---

**Author:** Tory • MIT License
