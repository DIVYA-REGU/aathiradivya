from datetime import datetime
date_input = input()
date_obj = datetime.strptime(date_input, '%m %d %Y')
day_of_week = date_obj.strftime('%A').upper()
print(day_of_week)
