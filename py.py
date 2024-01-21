from datetime import datetime
date = datetime.now()
f = "%Y-%m-%d %H:%M:%S"
date = date.strftime(f)
print(date)
print(type(date))