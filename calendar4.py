import tkinter as tk
from tkinter import messagebox
import calendar

class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Year Input")

        self.create_widgets()

    def create_widgets(self):
        self.callable=tk.Label(self.root, text="CALENDAR")
        self.callable.pack(pady=15)

        
        # Year entry label
        self.year_label = tk.Label(self.root, text="Enter Year:")
        self.year_label.pack(pady=10)

        # Year entry field
        self.year_entry = tk.Entry(self.root)
        self.year_entry.pack(pady=5)
        self.show_button = tk.Button(self.root, text="Show Calendar", command=self.show_calendar)
        self.show_button.pack(pady=20)

    def show_calendar(self):
        try:
            year = int(self.year_entry.get())
            if year < 1:
                raise ValueError("Year must be greater than 0.")
            CalendarWindow(year)
        except ValueError as e:
            messagebox.showerror("Invalid input", f"Please enter a valid year.\n{e}")

class CalendarWindow:
    def __init__(self, year):
        self.year = year
        self.window = tk.Toplevel()
        self.window.title(f"Calendar for {self.year}")

        self.create_widgets()

    def create_widgets(self):
        cal = calendar.TextCalendar(calendar.SUNDAY)

        for month in range(1, 13):
            month_frame = tk.Frame(self.window, bd=2, relief='ridge')
            month_frame.grid(row=(month-1)//3, column=(month-1)%3, padx=5, pady=5)

            month_label = tk.Label(month_frame, text=calendar.month_name[month], font=('Helvetica', 12, 'bold'))
            month_label.pack()

            days_frame = tk.Frame(month_frame)
            days_frame.pack()

            # Create the day labels
            days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
            for day in days:
                tk.Label(days_frame, text=day, font=('Helvetica', 10)).grid(row=0, column=days.index(day))

            # Create the calendar days
            month_days = cal.monthdayscalendar(self.year, month)
            for row_idx, week in enumerate(month_days, start=1):
                for col_idx, day in enumerate(week):
                    day_text = str(day) if day != 0 else ''
                    tk.Label(days_frame, text=day_text, font=('Helvetica', 10)).grid(row=row_idx, column=col_idx)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalendarApp(root)
    root.mainloop()
