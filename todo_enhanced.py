# ============================================================
# 📝 Enhanced To-Do List — Python Program
# Author: Vishvi
# Features: Add, View, Delete, Mark Complete,
#            Priority Levels, Due Dates, Save, Load
# ============================================================

import json
from datetime import datetime

FILENAME = "tasks.json"

def load_tasks():
    """Load tasks from JSON file."""
    try:
        with open(FILENAME, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)
    print("💾 Tasks saved successfully!")

def add_task(tasks):
    """Add a new task with priority and due date."""
    title = input("📌 Task title: ").strip()
    if not title:
        print("⚠️  Task title cannot be empty.")
        return

    priority = input("🔺 Priority (High / Medium / Low) [default: Medium]: ").strip().capitalize()
    if priority not in ["High", "Medium", "Low"]:
        priority = "Medium"

    due_date = input("📅 Due date (DD-MM-YYYY) or press Enter to skip: ").strip()
    try:
        datetime.strptime(due_date, "%d-%m-%Y")
    except ValueError:
        due_date = None

    task = {
        "title": title,
        "priority": priority,
        "due_date": due_date,
        "done": False,
        "created_at": datetime.now().strftime("%d-%m-%Y %H:%M")
    }
    tasks.append(task)
    print(f"✅ Task added: {title}")

def view_tasks(tasks):
    """Display all tasks in a formatted list."""
    if not tasks:
        print("📋 No tasks yet. Add one!")
        return

    priority_icon = {"High": "🔴", "Medium": "🟡", "Low": "🟢"}
    print("\n" + "="*55)
    print(f"  {'#':<4} {'Status':<8} {'Pri':<6} {'Due':<14} Task")
    print("="*55)
    for i, t in enumerate(tasks, 1):
        status = "✅ Done" if t["done"] else "⏳ Todo"
        icon   = priority_icon.get(t["priority"], "⚪")
        due    = t["due_date"] or "No date"
        print(f"  {i:<4} {status:<8} {icon} {t['priority']:<5} {due:<14} {t['title']}")
    print("="*55 + "\n")

def mark_complete(tasks):
    """Mark a task as done."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("✅ Enter task number to mark complete: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print(f"🎉 Marked as done: {tasks[num-1]['title']}")
        else:
            print("⚠️  Invalid number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")

def delete_task(tasks):
    """Delete a task by number."""
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("🗑️  Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"🗑️  Deleted: {removed['title']}")
        else:
            print("⚠️  Invalid number.")
    except ValueError:
        print("⚠️  Please enter a valid number.")

def show_menu():
    print("\n========= 📝 TO-DO LIST MENU =========")
    print("  1. ➕ Add task")
    print("  2. 📋 View all tasks")
    print("  3. ✅ Mark task as complete")
    print("  4. 🗑️  Delete task")
    print("  5. 💾 Save tasks")
    print("  6. ❌ Exit")
    print("=======================================")

def main():
    print("\n🚀 Welcome to your Enhanced To-Do List!")
    tasks = load_tasks()
    print(f"📂 Loaded {len(tasks)} task(s) from file.\n")

    while True:
        show_menu()
        choice = input("👉 Choose an option (1-6): ").strip()

        if   choice == "1": add_task(tasks)
        elif choice == "2": view_tasks(tasks)
        elif choice == "3": mark_complete(tasks)
        elif choice == "4": delete_task(tasks)
        elif choice == "5": save_tasks(tasks)
        elif choice == "6":
            save_tasks(tasks)
            print("👋 Goodbye! Keep crushing your tasks!")
            break
        else:
            print("⚠️  Invalid choice. Please enter 1-6.")

if __name__ == "__main__":
    main()
