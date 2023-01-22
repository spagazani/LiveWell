import GUI
import alarms
import tkthread


def Home(default_reminders):
  # 
  
  # print("con")
  # Opens the home page
  home = GUI.Home_window()
  home.show()

  while True:
    
    if GUI.sg.WIN_CLOSED:
      break
    alwaysAct()
    event, values = home.home_window.read() 
    
    # If clicked go to set/update reminders page
    if event == "Set/Update Reminders":
      Reminders(default_reminders)
      home.home_window.close()
      break
    # If clicked go to Look at Resources page
    if event == "Look at Resources":
      Resources(default_reminders)
      home.home_window.close()
      break
    # If clicked, close the home page
    if event == "Close":
      home.home_window.close()
      break
    

def Reminders(default_reminders):
  reminders = GUI.Reminders_window(default_reminders)
  reminders.show()
  while True:
   
    if GUI.sg.WIN_CLOSED:
      break 
    alwaysAct()
    event, values = reminders.reminders_window.read()
    
    # if finish button is pressed, update/create new alarms
    if event == "Finish":
      default_reminders = values

      # start stretch alarm
      if values["st_check"] == True:
        st.startAlarm(values["st_in"], values["st_drop"])
    
      # start walk alarm
      if values["wk_check"] == True:
        wk.startAlarm(values["wk_in"], values["wk_drop"])

      # start water alarm
      if values["wt_check"] == True:
        wt.startAlarm(values["wt_in"], values["wt_drop"])

      # start eating alarm
      if values["et_check"] == True:
        et.startAlarm(values["et_in"], values["et_drop"])

      # start meditation alarm
      if values["md_check"] == True:
        md.startAlarm(values["md_in"], values["md_drop"])

      # start breath alarm
      if values["br_check"] == True:
        br.startAlarm(values["br_in"], values["br_drop"])
      
      # Close window and return to homescreen

      Home(default_reminders)
      reminders.reminders_window.close()
      break



def Resources(default_reminders):
  # Open resource page and perform checks on if each button has been pressed yet
  resources = GUI.Resources_window()
  resources.show()
  while True:
    
    if GUI.sg.WIN_CLOSED:
      break
    
    event, values = resources.resources_window.read()
    alwaysAct()
    if event == "Posture":
      Posture(default_reminders)
      resources.resources_window.close()
      break
    if event == "Back":
      back(default_reminders)
      resources.resources_window.close()
      break
    if event == "Neck":
      neck(default_reminders)
      resources.resources_window.close()
      break
    if event == "Hands":
      hands(default_reminders)
      resources.resources_window.close()
      break
    if event == "Legs":
      legs(default_reminders)
      resources.resources_window.close()
      break
    if event == "Breathing":
      breathing(default_reminders)
      resources.resources_window.close()
      break
    if event == "Meditation":
      meditation(default_reminders)
      resources.resources_window.close()
      break
    if event == "Finish":
      resources.resources_window.close()
      Home(default_reminders)
      break

    

'''Resource pages'''


def Posture(default_reminders):
  # opens posture page
  posture = GUI.Posture_window()
  posture.show()
  while True:

    if GUI.sg.WIN_CLOSED:
      break
    alwaysAct()
    event, values = posture.posture_window.read()
    if event == "Finish":
      posture.posture_window.close()
      Resources(default_reminders)
      break

    

def back(default_reminders):
  back = GUI.Back_window()
  back.show()
  while True:
    alwaysAct()
    if GUI.sg.WIN_CLOSED:
      break
    event, values = back.back_window.read()
    if event == "Finish":
      back.back_window.close()
      Resources(default_reminders)
      break
    

def neck(default_reminders):
  neck = GUI.Neck_window()
  neck.show()
  while True:
    alwaysAct()
    if GUI.sg.WIN_CLOSED:
      break
    event, values = neck.neck_window.read()
    if event == "Finish":
      neck.neck_window.close()
      Resources(default_reminders)
      break
    

def hands(default_reminders):
  hands = GUI.Hands_window()
  hands.show()
  while True:
    alwaysAct()
    if GUI.sg.WIN_CLOSED:
      break
    event, values = hands.hands_window.read()
    if event == "Finish":
      hands.hands_window.close()
      Resources(default_reminders)
      break

    

def legs(default_reminders):
  legs = GUI.Legs_window()
  legs.show()
  while True:
    alwaysAct()
    if GUI.sg.WIN_CLOSED:
      break
    event, values = legs.legs_window.read()
    if event == "Finish":
      legs.legs_window.close()
      Resources(default_reminders)
      break

    

def breathing(default_reminders):
  breath = GUI.Breath_window()
  breath.show()
  while True:
    alwaysAct()
    if GUI.sg.WIN_CLOSED:
      break
    event, values = breath.breath_window.read()
    if event == "Finish":
      breath.breath_window.close()
      Resources(default_reminders)
      break
    
    

def meditation(default_reminders):
  meditation = GUI.Meditation_window()
  meditation.show()
  while True:
    alwaysAct()
    if GUI.sg.WIN_CLOSED:
      break
    event, values = meditation.meditation_window.read()
    if event == "Finish":
      meditation.meditation_window.close()
      Resources(default_reminders)
      break
    
    
def alwaysAct():
  st.activeAlarm()
  wk.activeAlarm()
  wt.activeAlarm()
  et.activeAlarm()
  md.activeAlarm()
  br.activeAlarm()
  
     

'''main'''
default_reminders = {
  'st_check': False,
  'st_in': '3',
  'st_drop': 'hours',
  'wk_check': False,
  'wk_in': '6',
  'wk_drop': 'hours',
  'wt_check': False,
  'wt_in': '15',
  'wt_drop': 'mins',
  'et_check': False,
  'et_in': '4',
  'et_drop': 'hours',
  'md_check': False,
  'md_in': '6',
  'md_drop': 'hours',
  'br_check': False,
  'br_in': '1',
  'br_drop': 'hour'
}

global st
global wk
global wt
global et
global md
global br
st = alarms.alarm("Do a stretch!")
wk = alarms.alarm("Take a walk!")
wt = alarms.alarm("Drink some water!")
et = alarms.alarm("Eat a meal!")
md = alarms.alarm("Do some meditation!")
br = alarms.alarm("Do a breathing exercise!")

Home(default_reminders)
