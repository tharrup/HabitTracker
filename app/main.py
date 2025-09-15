from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty, ListProperty
from kivy.clock import Clock
import json, os, datetime

KV_PATH = os.path.join(os.path.dirname(__file__), "kv", "main.kv")
DATA_PATH = os.path.join(os.path.dirname(__file__), "habits.json")

def load_kv():
    with open(KV_PATH, "r", encoding="utf-8") as f:
        return f.read()

def now_date():
    return datetime.date.today().isoformat()

class HabitApp(MDApp):
    title = "Habit Tracker"
    habits = ListProperty([])
    status_msg = StringProperty("Ready")

    def build(self):
        self.theme_palette = "Teal"
        self.theme_style = "Light"
        self.load_data()
        return Builder.load_string(load_kv())

    def on_start(self):
        Clock.schedule_once(lambda *_: self.refresh_list())

    # Data handling
    def load_data(self):
        if os.path.exists(DATA_PATH):
            try:
                with open(DATA_PATH, "r", encoding="utf-8") as f:
                    self.habits = json.load(f)
            except Exception:
                self.habits = []
        else:
            self.habits = []

    def save_data(self):
        with open(DATA_PATH, "w", encoding="utf-8") as f:
            json.dump(self.habits, f, indent=2)

    # UI actions
    def add_habit(self, text):
        text = (text or "").strip()
        if not text:
            self.status_msg = "Enter a habit name"
            return
        self.habits.append({
            "name": text,
            "created": now_date(),
            "streak": 0,
            "xp": 0,
            "last_completed": None
        })
        self.save_data()
        self.refresh_list()
        self.root.ids.input.text = ""
        self.status_msg = f"Added '{text}'"

    def complete_habit(self, index):
        try:
            h = self.habits[index]
        except IndexError:
            return
        today = now_date()
        if h.get("last_completed") == today:
            self.status_msg = "Already completed today"
            return
        # Streak logic
        last = h.get("last_completed")
        if last:
            last_date = datetime.date.fromisoformat(last)
            if last_date == datetime.date.today() - datetime.timedelta(days=1):
                h["streak"] = h.get("streak", 0) + 1
            else:
                h["streak"] = 1
        else:
            h["streak"] = 1
        h["xp"] = h.get("xp", 0) + 10
        h["last_completed"] = today
        self.save_data()
        self.refresh_list()
        self.status_msg = f"Completed '{h['name']}' (+10 XP)"

    def delete_habit(self, index):
        try:
            name = self.habits[index]["name"]
            del self.habits[index]
            self.save_data()
            self.refresh_list()
            self.status_msg = f"Deleted '{name}'"
        except IndexError:
            pass

    def refresh_list(self):
        rv = self.root.ids.rv
        rv.data = []
        for i, h in enumerate(self.habits):
            rv.data.append({
                "index": i,
                "name": h["name"],
                "streak": h.get("streak", 0),
                "xp": h.get("xp", 0),
                "last_completed": h.get("last_completed") or "—",
                "complete_cb": lambda idx=i: self.complete_habit(idx),
                "delete_cb": lambda idx=i: self.delete_habit(idx),
            })

if __name__ == "__main__":
    HabitApp().run()
