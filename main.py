import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class SalaryCounter:
    def __init__(self, root):
        self.root = root
        self.root.title("Monatlicher Gehalts-Counter")
        self.root.geometry("420x220")
        self.root.resizable(False, False)

        self.monthly_salary = 0.0
        self.payday = 1
        self.running = False

        self.create_widgets()

    def create_widgets(self):
        frame = ttk.Frame(self.root, padding=15)
        frame.pack(fill="both", expand=True)

        ttk.Label(frame, text="Monatsbrutto (€):").grid(row=0, column=0, sticky="w")
        self.salary_entry = ttk.Entry(frame)
        self.salary_entry.grid(row=0, column=1, pady=5)

        ttk.Label(frame, text="Gehalts-Zahltag (1-31):").grid(row=1, column=0, sticky="w")
        self.payday_entry = ttk.Entry(frame)
        self.payday_entry.grid(row=1, column=1, pady=5)

        self.start_button = ttk.Button(frame, text="Start", command=self.start_counter)
        self.start_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.counter_label = ttk.Label(
            frame, text="0.000000 €", font=("Consolas", 24, "bold")
        )
        self.counter_label.grid(row=3, column=0, columnspan=2, pady=15)

    def get_salary_period(self):
        now = datetime.now()
        year = now.year
        month = now.month

        payday_this_month = datetime(year, month, self.payday)

        if now < payday_this_month:
            last_month = payday_this_month - timedelta(days=30)
            start = datetime(last_month.year, last_month.month, self.payday)
            end = payday_this_month
        else:
            next_month = payday_this_month + timedelta(days=32)
            next_month = datetime(next_month.year, next_month.month, self.payday)
            start = payday_this_month
            end = next_month

        return start, end

    def start_counter(self):
        try:
            self.monthly_salary = float(self.salary_entry.get())
            self.payday = int(self.payday_entry.get())
            self.running = True
            self.update_counter()
        except:
            self.counter_label.config(text="Ungültige Eingabe")

    def update_counter(self):
        if not self.running:
            return

        start, end = self.get_salary_period()
        now = datetime.now()

        total_seconds = (end - start).total_seconds()
        elapsed_seconds = (now - start).total_seconds()

        elapsed_seconds = max(0, min(elapsed_seconds, total_seconds))

        earned = (elapsed_seconds / total_seconds) * self.monthly_salary
        self.counter_label.config(text=f"{earned:,.6f} €")

        self.root.after(100, self.update_counter)

if __name__ == "__main__":
    root = tk.Tk()
    app = SalaryCounter(root)
    root.mainloop()
