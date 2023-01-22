import PySimpleGUI as sg

WIDTH = 700
HEIGHT = 350
DROPDOWN = ["mins", "hours"]


class Home_window:

  def __init__(self):
    self.home_window = []

  def show(self):
    home_layout = [[
      sg.Text("Welcome", text_color='black', background_color='white')
    ], [sg.Button("Set/Update Reminders"),
        sg.Button("Look at Resources")], [sg.HSeparator()],
                   [sg.Button("Close")]]
    self.home_window = sg.Window("Home",
                                 home_layout,
                                 size=(WIDTH, HEIGHT),
                                 background_color='white')


#reminders window
'''
stretches = st
walk = wk
water = wt
eating = et
meditation = md
breathing exercises = br
'''


class Reminders_window:

  def __init__(self, defaults):
    self.defaults = defaults
    self.reminders_window = []

  def show(self):
    rem_column_physical = [[sg.Text("Physical")],
                           [
                             sg.Checkbox("Stretches",
                                         key="st_check",
                                         default=self.defaults["st_check"])
                           ],
                           [
                             sg.InputText(self.defaults["st_in"],
                                          size=(3, 1),
                                          key="st_in"),
                             sg.Combo(DROPDOWN,
                                      key="st_drop",
                                      default_value=self.defaults["st_drop"])
                           ],
                           [
                             sg.Checkbox("Take a Walk",
                                         key="wk_check",
                                         default=self.defaults["wk_check"])
                           ],
                           [
                             sg.InputText(self.defaults["wk_in"],
                                          size=(3, 1),
                                          key="wk_in"),
                             sg.Combo(DROPDOWN,
                                      key="wk_drop",
                                      default_value=self.defaults["wk_drop"])
                           ],
                           [
                             sg.Checkbox("Drink Water",
                                         key="wt_check",
                                         default=self.defaults["wt_check"])
                           ],
                           [
                             sg.InputText(self.defaults["wt_in"],
                                          size=(3, 1),
                                          key="wt_in"),
                             sg.Combo(DROPDOWN,
                                      key="wt_drop",
                                      default_value=self.defaults["wt_drop"])
                           ],
                           [
                             sg.Checkbox("Eat a Meal",
                                         key="et_check",
                                         default=self.defaults["et_check"])
                           ],
                           [
                             sg.InputText(self.defaults["et_in"],
                                          size=(3, 1),
                                          key="et_in"),
                             sg.Combo(DROPDOWN,
                                      key="et_drop",
                                      default_value=self.defaults["et_drop"])
                           ]]
    rem_column_mental = [
      [sg.Text("Mental")],
      [
        sg.Checkbox("Meditation",
                    key="md_check",
                    default=self.defaults["md_check"])
      ],
      [
        sg.InputText(self.defaults["md_in"], size=(3, 1), key="md_in"),
        sg.Combo(DROPDOWN,
                 key="md_drop",
                 default_value=self.defaults["md_drop"])
      ],
      [
        sg.Checkbox("Breathing Exercises",
                    key="br_check",
                    default=self.defaults["br_check"])
      ],
      [
        sg.InputText(self.defaults["br_in"], size=(3, 1), key="br_in"),
        sg.Combo(DROPDOWN,
                 key="br_drop",
                 default_value=self.defaults["br_drop"])
      ],
    ]
    reminders_layout = [[
      sg.Column(rem_column_physical,
                vertical_alignment='top',
                background_color='white'),
      sg.Column(rem_column_mental,
                vertical_alignment='top',
                background_color='white')
    ], [sg.HSeparator()], [sg.Button("Finish")]]

    self.reminders_window = sg.Window("Reminders",
                                      reminders_layout,
                                      size=(WIDTH, HEIGHT),
                                      background_color='white')


#alarm popup
class Alarm_window:

  def __init__(self, message):
    self.message = message
    self.alarm_window = []

  def show(self):
    alarm_format = [[sg.Text(self.message)], [sg.Button("OK")]]
    self.alarm_window = sg.Window("Alarm",
                                  alarm_format,
                                  size=(WIDTH, HEIGHT),
                                  background_color='white')


#resources window
class Resources_window:

  def __init__(self):
    self.resources_window = []

  def show(self):
    res_column_physical = [[sg.Text("Posture")], [sg.Button("Posture")],
                           [sg.Text("Stretches")], [sg.Button("Back")],
                           [sg.Button("Neck")], [sg.Button("Hands")],
                           [sg.Button("Legs")]]

    res_column_mental = [[sg.Text("Mental Exercises")],
                         [sg.Button("Breathing")], [sg.Button("Meditation")]]
    resources_layout = [[
      sg.Column(res_column_physical,
                vertical_alignment='top',
                background_color='white'),
      sg.Column(res_column_mental,
                vertical_alignment='top',
                background_color='white')
    ], [sg.HSeparator()], [sg.Button("Finish")]]
    self.resources_window = sg.Window("Resources",
                                      resources_layout,
                                      size=(WIDTH, HEIGHT),
                                      background_color='white')


'''resources'''


#postures
class Posture_window:

  def __init__(self):
    self.posture_window = []

  def show(self):
    posture_layout = [
      [
        sg.Text(
          "- Keep both feet supported naturally on the floor; This will take pressure off your lower back"
        )
      ],
      [
        sg.Text(
          "- Avoid reaching, leaning, or twisting in your chair; Put frequently used items in your reach"
        )
      ],
      [
        sg.Text(
          "- Keep your shoulders relaxed,  with elbows close to your body")
      ],
      [
        sg.Text(
          "- Don't rest your arms on any hard surface, use pads if needed")
      ], [sg.Text("- Elbows should be kept at an angle of 100-110 degrees")],
      [sg.Text("- Wrists should be kept in a neutral or straight positions")],
      [sg.HSeparator()], [sg.Button("Finish")]
    ]
    self.posture_window = sg.Window("Posture",
                                    posture_layout,
                                    size=(WIDTH, HEIGHT),
                                    background_color='white')


class Back_window:

  def __init__(self):
    self.back_window = []

  def show(self):
    back_col1 = [
      [sg.Text("Seated Spinal Rotation")],
      [sg.Text("At your desk, take your hand")],
      [sg.Text("and put it on your opposite")],
      [sg.Text("shoulder. Now do the same")],
      [sg.Text("with your other hand so your")],
      [sg.Text("arms are crossed. From your")],
      [sg.Text("waist, turn your upper body")],
      [sg.Text("from left to right, as much")],
      [sg.Text("as you feel fit.")],
    ]
    back_col2 = [
      [sg.Text("Posterior Shoulder Stretch")],
      [sg.Text("Take one arm and hold it ")],
      [sg.Text("across your chest,")],
      [sg.Text("perpendicular to the rest of")],
      [sg.Text("your body. With your other ")],
      [sg.Text("hand, pull your elbow into")],
      [sg.Text("your chest.")],
    ]
    back_col3 = [[sg.Text("Sitting Back Extensions")],
                 [sg.Text("While sitting, put your feet")],
                 [sg.Text("together and straighten your")],
                 [sg.Text("back. Take the palms of your ")],
                 [sg.Text("hands and put them on the ")],
                 [sg.Text("small of your back. Lean back ")],
                 [sg.Text("over your hands.")]]
    back_layout = [[
      sg.Column(back_col1, vertical_alignment='top'),
      sg.Column(back_col2, vertical_alignment='top'),
      sg.Column(back_col3, vertical_alignment='top')
    ], [sg.HSeparator()], [sg.Button("Finish")]]
    self.back_window = sg.Window("Back Stretches",
                                 back_layout,
                                 size=(WIDTH, HEIGHT),
                                 background_color='white')


class Neck_window:

  def __init__(self):
    self.neck_window = []

  def show(self):
    neck_col1 = [
      [sg.Text("Neck Rotations")],
      [sg.Text("Lift your head up and face ")],
      [sg.Text("forward. Slowly look to your ")],
      [sg.Text("right and left, trying to push ")],
      [sg.Text("past your shoulders.")],
    ]
    neck_col2 = [[sg.Text("Upper Shoulder/Neck Stretch")],
                 [sg.Text("While sitting on one hand,")],
                 [sg.Text("tilt your head in the ")],
                 [sg.Text("direction opposite to that")],
                 [sg.Text("hand. Now tilt your head  ")],
                 [sg.Text("slightly forwards toward ")],
                 [sg.Text("your shoulder. switch which")],
                 [sg.Text("hand you are sitting on and")],
                 [sg.Text("repeat.")]]
    neck_col3 = [[sg.Text("Chin to Shoulder Points")],
                 [sg.Text("Point your chin to your right ")],
                 [sg.Text("shoulder and tilt it slightly ")],
                 [sg.Text("down. Take your right hand ")],
                 [sg.Text("and gently place it on the left")],
                 [sg.Text("side of your head, and pull it toward")],
                 [sg.Text("your shoulder. Hold for 5-10")],
                 [sg.Text("seconds and repeat on the other")],
                 [sg.Text("side.")]]
    neck_layout = [[
      sg.Column(neck_col1, vertical_alignment='top'),
      sg.Column(neck_col2, vertical_alignment='top'),
      sg.Column(neck_col3, vertical_alignment='top')
    ], [sg.HSeparator()], [sg.Button("Finish")]]
    self.neck_window = sg.Window("Neck Stretches",
                                 neck_layout,
                                 size=(WIDTH, HEIGHT),
                                 background_color='white')


class Hands_window:

  def __init_(self):
    self.hands_window = []

  def show(self):
    hands_col1 = [[sg.Text("Wrist Stretch")],
                  [sg.Text("Take both palms and push ")],
                  [sg.Text("them together in front of")],
                  [sg.Text("your chest for 15 seconds.")],
                  [sg.Text("Now take the back of your ")],
                  [sg.Text("hands and push them ")],
                  [sg.Text("together the same way and ")],
                  [sg.Text("hold for 15 seconds. Repeat")],
                  [sg.Text("the above 5 times.")]]
    hands_col2 = [[sg.Text("Wrist Circles")],
                  [sg.Text("Extend both arms straight in ")],
                  [sg.Text("front of you. Make a fist with ")],
                  [sg.Text("both of your hands. Rotate your ")],
                  [sg.Text("right wrist clockwise and your ")],
                  [sg.Text("left wrist in the opposite ")],
                  [sg.Text("direction. Do this three to four")],
                  [sg.Text("times. Now alternate the ")],
                  [sg.Text("direction for another three to ")],
                  [sg.Text("four times.")]]
    hands_col3 = [[sg.Text("Thumb Touches")],
                  [sg.Text("Hold your hands outwards with")],
                  [sg.Text("your palms facing the ceiling.")],
                  [sg.Text("With your right hand, slowly")],
                  [sg.Text("touch your thumb to the tip of")],
                  [sg.Text("each finger. Repeat on the other")],
                  [sg.Text("hand, and return to the hand")],
                  [sg.Text("outwards, palm up position.")],
                  [sg.Text("Repeat with both hands.")]]
    hands_layout = [[
      sg.Column(hands_col1, vertical_alignment='top'),
      sg.Column(hands_col2, vertical_alignment='top'),
      sg.Column(hands_col3, vertical_alignment='top')
    ], [sg.HSeparator()], [sg.Button("Finish")]]
    self.hands_window = sg.Window("Neck Stretches",
                                  hands_layout,
                                  size=(WIDTH, HEIGHT),
                                  background_color='white')


class Legs_window:

  def __init_(self):
    self.legs_window = []

  def show(self):
    legs_col1 = [
      [sg.Text("Hamstring Reach")],
      [sg.Text("Sit on the edge of your seat,")],
      [sg.Text("feet flat on the floor. Extend")],
      [sg.Text("one leg with your knee as")],
      [sg.Text("straight as possible Bend at the.")],
      [sg.Text("waist and reach forwards. Gently")],
      [sg.Text("push down on your thigh or knee.")],
      [sg.Text("Maintain this position for at")],
      [sg.Text("least 10 seconds, keeping your")],
      [sg.Text("back straight the whole time.")],
      [sg.Text("Repeat 5 times per leg.")],
    ]
    legs_col2 = [[sg.Text("Knee Raises")],
                 [sg.Text("Lift your leg up while sitting")],
                 [sg.Text("and pull your knee towards your")],
                 [sg.Text("chest as close as you can. Hold")],
                 [sg.Text("for 10 seconds and repeat with")],
                 [sg.Text("the other leg.")]]
    legs_col3 = [[sg.Text("Leg Cross")],
                 [sg.Text("While seated, rest your leg ")],
                 [sg.Text("across your knee. Take a deep")],
                 [sg.Text("breath and push down gently on")],
                 [sg.Text("your knee. Hold for 5-10 ")],
                 [sg.Text("seconds then repeat on the ")],
                 [sg.Text("other leg.")]]
    legs_layout = [[
      sg.Column(legs_col1, vertical_alignment='top'),
      sg.Column(legs_col2, vertical_alignment='top'),
      sg.Column(legs_col3, vertical_alignment='top')
    ], [sg.HSeparator()], [sg.Button("Finish")]]
    self.legs_window = sg.Window("Neck Stretches",
                                 legs_layout,
                                 size=(WIDTH, HEIGHT),
                                 background_color='white')


class Breath_window:

  def __init__(self):
    self.breathing_window = []

  def show(self):
    breath_col1 = [[sg.Text("Square Breathing")],
                   [sg.Text("Start by exhaling all the air")],
                   [sg.Text("you have left in your lungs.")],
                   [sg.Text("Now inhale for 4 seconds. Hold ")],
                   [sg.Text("your breath for 4 seconds.")],
                   [sg.Text("Exhale for 4 seconds. Hold for")],
                   [sg.Text("4 seconds. Then repeat, ")],
                   [sg.Text("starting at the second step. ")],
                   [sg.Text("Picture a square which your")],
                   [sg.Text("breath follows.")]]
    breath_col2 = [[sg.Text("Pursed Lip Breathing")],
                   [sg.Text("Relax your neck and ")],
                   [sg.Text("shoulders. Keeping your")],
                   [sg.Text("mouth closed, inhale slowly")],
                   [sg.Text("through your nose for 2 ")],
                   [sg.Text("counts. Purse your lips as if")],
                   [sg.Text("you are going to whistle. ")],
                   [sg.Text("Exhale slowly by blowing air ")],
                   [sg.Text("through your pursed lips for")],
                   [sg.Text("a count of 4.")]]
    breath_col3 = [[sg.Text("Equal Breathing")],
                   [sg.Text("Breathe in through your nose ")],
                   [sg.Text("to the count of 5. Now breath")],
                   [sg.Text("out through your nose for 5")],
                   [sg.Text("seconds. Repeat, and as you ")],
                   [sg.Text("do increase the amount of ")],
                   [sg.Text("time you are breathing for")],
                   [sg.Text("(i.e. 5 seconds to 6 seconds).")]]
    breath_layout = [[
      sg.Column(breath_col1, vertical_alignment='top'),
      sg.Column(breath_col2, vertical_alignment='top'),
      sg.Column(breath_col3, vertical_alignment='top')
    ], [sg.HSeparator()], [sg.Button("Finish")]]
    self.breath_window = sg.Window("Neck Stretches",
                                   breath_layout,
                                   size=(WIDTH, HEIGHT),
                                   background_color='white')


class Meditation_window:

  def __init__(self):
    self.meditation_window = []

  def show(self):
    meditation_col1 = [[sg.Text("Walking Meditation")],
                       [sg.Text("Find a peaceful location away")],
                       [sg.Text("from distractions. Walk a few ")],
                       [sg.Text("paces and then stop, and ")],
                       [sg.Text("breathe for as long as you’d ")],
                       [sg.Text("like. Look around you and take")],
                       [sg.Text("a mental note of your ")],
                       [sg.Text("surroundings. As you start ")],
                       [sg.Text("walking again, continue to ")],
                       [sg.Text("observe how your environment")],
                       [sg.Text("changes.")]]
    meditation_col2 = [
      [sg.Text("Gratitude Meditation")],
      [sg.Text("Start by closing your eyes")],
      [sg.Text("and taking a deep breath. ")],
      [sg.Text("Mentally list 5-7 you feel")],
      [sg.Text("grateful for. Repeat as ")],
      [sg.Text("often as you like.")],
    ]
    meditation_col3 = [[sg.Text("The Blank Screen")],
                       [sg.Text("Imagine you are staring at a")],
                       [sg.Text("blank screen or wall. Now try to")],
                       [sg.Text("clear your mind of everything.")],
                       [sg.Text("Anytime a stray thought pops")],
                       [sg.Text("up, visualize yourself erasing it.")],
                       [sg.Text("This will help clear your mind ")],
                       [sg.Text("to better focus on your goals.")]]

    meditation_layout = [[
      sg.Column(meditation_col1, vertical_alignment='top'),
      sg.Column(meditation_col2, vertical_alignment='top'),
      sg.Column(meditation_col3, vertical_alignment='top')
    ], [sg.HSeparator()], [sg.Button("Finish")]]
    self.meditation_window = sg.Window("Neck Stretches",
                                       meditation_layout,
                                       size=(WIDTH, HEIGHT),
                                       background_color='white')
