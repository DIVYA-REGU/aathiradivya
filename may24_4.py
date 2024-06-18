import tkinter as tk
import calendar
from tkinter import ttk
from datetime import datetime
class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Calendar")
        
        self.current_year = datetime.now().year
        self.current_month = datetime.now().month

        self.create_widgets()
        self.show_calendar(self.current_year, self.current_month)

    def create_widgets(self):
        # Frame for navigation buttons
        nav_frame = tk.Frame(self.root)
        nav_frame.pack(pady=10)

        self.prev_button = tk.Button(nav_frame, text="<", command=self.prev_month)
        self.prev_button.grid(row=0, column=0, padx=5)
        self.next_button = tk.Button(nav_frame, text=">", command=self.next_month)
        self.next_button.grid(row=0, column=2, padx=5)

        self.month_label = tk.Label(nav_frame, text="", width=15)
        self.month_label.grid(row=0, column=1)

        # Frame for calendar
        self.cal_frame = tk.Frame(self.root)
        self.cal_frame.pack()

    def show_calendar(self, year, month):
        # Clear the previous calendar
        for widget in self.cal_frame.winfo_children():
            widget.destroy()

        cal = calendar.TextCalendar(calendar.SUNDAY)
        month_days = cal.monthdayscalendar(year, month)

        self.month_label.config(text=f"{calendar.month_name[month]} {year}")

        # Create the day labels
        days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
        for i, day in enumerate(days):
            tk.Label(self.cal_frame, text=day).grid(row=0, column=i)

        # Create the calendar
        for row_idx, week in enumerate(month_days, start=1):
            for col_idx, day in enumerate(week):
                if day != 0:
                    tk.Label(self.cal_frame, text=day).grid(row=row_idx, column=col_idx, padx=5, pady=5)

    def prev_month(self):
        if self.current_month == 1:
            self.current_month = 12
            self.current_year -= 1
        else:
            self.current_month -= 1
        self.show_calendar(self.current_year, self.current_month)

    def next_month(self):
        if self.current_month == 12:
            self.current_month = 1
            self.current_year += 1
        else:
            self.current_month += 1
        self.show_calendar(self.current_year, self.current_month)
if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()








