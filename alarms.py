from datetime import datetime, timedelta
import GUI


class alarm():
  '''
  A class to set an alarm.
  _________________________________________________
  Attributes
    freq : 0
      Sets how frequently the alarm will go off
    state : bool
      Is alarm active or not?
    startTime : int
      The time when the alarm was set
  _________________________________________________
  Methods
      __init__(self) :
          Initializes all the Class' attributes
      activeAlarm(self) :
          Checks to see if alarm needs to go off yet.
      popUp(self) :
          Displays popup window to tell user that the alarm has gone off
      startAlarm(self, amount, type) :
          Sets the intervals of time and when the alarm was set
  _________________________________________________
  '''

  def __init__(self, name):
    self.name = name
    self.freq = 0
    self.state = False
    self.startTime = 0

  def activeAlarm(self):
    if self.state == True:

      now = datetime.now()
      current_hour = now.strftime("%H")
      current_min = now.strftime("%M")
      if current_min == (self.startTime + timedelta(minutes=self.freq)).strftime("%M") and current_hour == (self.startTime + timedelta(minutes=self.freq)).strftime("%H"):

        self.state = False
        self.startTime = now
        self.popUp()
        
        

  def popUp(self):
    alarm_popup = GUI.Alarm_window(self.name)
    alarm_popup.show()
    while True:
      if GUI.sg.WIN_CLOSED:
        break
      event = alarm_popup.alarm_window.read()
      # if event == "OK":
      alarm_popup.alarm_window.close()
      break

  def startAlarm(self, amount, type):
    if type == "hour":
      amount = int(amount) * 60
    self.freq = int(amount)
    self.startTime = datetime.now()
    self.state = True
