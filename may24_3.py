import tkinter as tk
import calendar
from tkinter import ttk
from datetime import datetime
class calendarapp:
    def __init__(self,root):
        self.root=root
        self.root.title("CALENDAR")
        self.create_widgets()

    def create_widgets(self):
        self.year_label=tk.Label(self.root, text="enter year")
        self.year_label.pack()

        self.year_entry=tk.Entry(self.root)
        self.year_entry.pack()

        self.show_button=tk.Button(self.root,text="show calendar",command=self.show_calendar)
        self.show_button.pack()
    def show_calendar(self):
        try:
            year=int(self.year_entry.get())
            if year < 1:
                raise ValueError("year must be greater than 0")
            CalendarWindow(year)
        except ValueError as e:
            tk.messagebox.showerror("invalid input")
class CalendarWindow:
    def __init__(self,year):
        self.year=year
        self.window=tk.Toplevel()
        self.create_widgets()
    def create_widgets(self):
        cal=calendar.TextCalendar(calendar.SUNDAY)

        for month in range(1,13):
            month_frame=tk.Frame(self.window,bd=2,relief='ridge')
            month_frame.grid(row=(month-1)//3,column=(month-1)%3,padx=5,pady=5)
            month_label=tk.Label(month_frame,text=calendar.month_name[month],font=('Helvetica', 12, 'bold'))
            month_label.pack()
            month_days=cal.monthdayscalendar(self.year,month)
            days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
            for day in days:
                tk.Label(month_frame, text=day, font=('Helvetica', 10)).pack(side='left', padx=2, pady=2)

            # Create the calendar days
            for week in month_days:
                week_frame = tk.Frame(month_frame)
                week_frame.pack()
                for day in week:
                    day_label = tk.Label(week_frame, text=str(day) if day != 0 else '', font=('Helvetica', 10))
                    day_label.pack(side='left', padx=2, pady=2)
if __name__ == "__main__":
    root = tk.Tk()
    app = calendarapp(root)
    root.mainloop()




   


