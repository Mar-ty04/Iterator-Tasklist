class Task:
  def __init__(self, desc, date, time):
  #assign the parameters to the attributes
    self._description = desc
    self._date = date
    self._time = time

  def __str__(self):
  #returns a string used to display the task’s information to the user.
    return f"{self._description} - Due: {self._date} at {self._time}"

  def __repr__(self):
  #returns a string used to write the task to the file
    return f"{self._description}, {self._date}, {self._time}\n"

  def __lt__(self, other):
  #returns true if the self task is less than the other task
  #Compare by year, then month, then day, then hour, then minute, 
  #then the task description in alphabetical order
    m1, d1, y1 = self._date.split("/")
    m2, d2, y2 = other._date.split("/")
    #comparing by the year 
    if y1 != y2:
      return y1 < y2

    #comparing by the month
    if m1 != m2:
      return m1 < m2

    #comparing by the day
    if d1 != d2:
      return d1 < d2

    h1, mi1 = self._time.split(":")
    h2, mi2 = other._time.split(":")

    #comparing by the hour
    if h1 != h2:
      return h1 < h2

    #comparing by the minute
    if mi1 != mi2:
      return mi1 < mi2

    #comparing by the task description
    return self._description < other._description