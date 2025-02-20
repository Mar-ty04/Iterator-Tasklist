import task


class TaskList:
  n = 0
  def __init__(self):
    #read in the list of tasks from file and store them in the tasklist by opening the
    #file and reading each line that consists of the task desctiption, date, and time
    #separated by commas. Construsting the task object by
    #appending it to the list an then sorting the list
    self._tasklist = []
    file = open("tasklist.txt")
    for line in file:
      items = line.strip().split(",")
      description, due_date, time = items 
      self.add_task(description, due_date, time)
    self._tasklist.sort()

  def add_task(self, desc, date, time):
    #constructs a new task using the parameters, appends it to 
    #the tasklist, and then sorts the list
    new_task = task.Task(desc, date, time)
    self._tasklist.append(new_task)
    self._tasklist.sort()

  def get_current_task(self):
    #returns the first task object in the list
    if self._tasklist:  # Check if tasklist is not empty
      return self._tasklist[0]
    else:
      return None

  def mark_complete(self):
    #remove and return the current task from the tasklist
    current = self.get_current_task()
    self._tasklist.remove(current)
    return current

  def save_file(self):
    #write contents of the tasklist back to file using 
    #task's repr method (description, date, and time separated by commas)
    file = open("tasklist.txt", "w")
    for task in self:
      file.write(task.__repr__())

    file.close()

  def __len__(self):
    #returns number of items in the tasklist
    return len(self._tasklist)

  def __iter__(self):
    #initialize the iterator attribute n and return self 
    self._n = 0 
    return self

  def __next__(self):
    #iterate the iterator one positiotn at a time
    #raise a stopiteration when iterator reaches end of tasklist 
    #otherwise return task obeject at iterators current position 
    if self._n > len(self._tasklist) - 1:
      raise StopIteration
    else:
      value = self._tasklist[self._n]
    self._n += 1 
    return value