# Display
MASTER_VOLUMEN = 0.1
RESOLUTION_1080 = False

WIDTH  = 1920
HEIGHT = 1080

NEXT_WEEK_SPEED = 0.2
AMOUNT_CLIENTS = 3
MAX_EMAILS = 9
VIP_PROBABILITY = 0.3

MONTH_NAMES = [
"enero",
"febero",
"marzo",
"abril"
"mayo",
"junio",
"julio",
"agosto",
"septiembre",
"octubre",
"noviembre",
"diciembre"
]

INITIAL_REPUTATION = 505
INITIAL_MONEY = 0

NAMES = ["Pepe", "Florentino", "Josefa", "Tontomás"]
ROOM_ELEMENTS = ["Cama", "Puerta", "Ducha"]

DISTANCE_DOWN_BUTTON_NEXT_DAY = HEIGHT # 720

LOCATION_BUTTON_PLAY = (960, 512)  # 720
LOCATION_BUTTON_CREDITS = (960, 624)  # 720
LOCATION_BUTTON_TUTORIAL = (960, 736)  # 720

LOCATION_BUTTON_PC = (931, 500) # 720
LOCATION_BUTTON_NEXT_WEEK = (WIDTH / 2, 148) # 720

#Icons in the coumputer screen for Mail, Reviews, Bookings and Upgrades.
# Locations buttons
LOCATION_BUTTON_EMAIL = (760, 500)  # 720
LOCATION_BUTTON_REVIEW = (1160, 500)  # 720
LOCATION_BUTTON_BOOKING = (760, 800)  # 720
LOCATION_BUTTON_UPGRADES = (1160, 795)  # 720
LOCATION_BUTTON_CLOSE = (20,20)  # 720

#Buttons of the emails you receive
LOCATION_BUTTON_CHANGE_EMAIL = (483, 205)  # 720
DISPLACEMENT_BUTTON_CHANGE_EMAIL = (0, 75)  # 720

#User name inside email button
DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL = (-60, -15)  # 720


#Content of the emails
LOCATION_EMAIL_CONTENT = (889, 539)  # 720
LOCATION_EMAIL_TEXT_SUBJECT = (696, 213)  # 720
LOCATION_EMAIL_TEXT_SENDER = (696, 261)  # 720
LOCATION_EMAIL_TEXT_BODY = (739, 354)  # 720
DISPLACEMENT_EMAIL_TEXT_BODY = (0, 25)

#Response for the emails, Accept o Decline the booking
LOCATION_BUTTON_ACCEPT_BOOKING = (839, 791)  # 720
LOCATION_BUTTON_DECLINE_BOOKING = (997, 791)  # 720

#Calendar and buttons to change the month displayed
LOCATION_CALENDAR = (1395, 391) # 720
LOCATION_BUTTON_NEXT_MONTH = (1536, 411)  # 720
LOCATION_BUTTON_PREVIOUS_MONTH = (1254, 411)  # 720

#Marker that selects the week you want to book
LOCATION_CALENDAR_MARKER_0 = (1396, 375)  # 720
LOCATION_CALENDAR_MARKER_1 = (1396, 403)  # 720
LOCATION_CALENDAR_MARKER_2 = (1396, 431)  # 720
LOCATION_CALENDAR_MARKER_3 = (1396, 459)  # 720


#Radio button of each week
LOCATION_BUTTON_CALENDAR_MARKER_0 = (1323, 669) # 720
LOCATION_BUTTON_CALENDAR_MARKER_1 = (1323, 699) # 720
LOCATION_BUTTON_CALENDAR_MARKER_2 = (1323, 729) # 720
LOCATION_BUTTON_CALENDAR_MARKER_3 = (1323, 759) # 720


SIZE_TEXT_USER_NAME = 18
SIZE_TEXT_SUBJECT = 22
SIZE_TEXT_SENDER = 18
SIZE_TEXT_BODY = 16




# Level config

# HUB









## 720
if not RESOLUTION_1080:
    #WIDTH = (int(WIDTH[0] / 1.5), int(WIDTH[1] / 1.5))
    #HEIGHT = (int(HEIGHT[0] / 1.5), int(HEIGHT[1] / 1.5))
    LOCATION_BUTTON_PLAY = (int(LOCATION_BUTTON_PLAY[0] / 1.5), int(LOCATION_BUTTON_PLAY[1] / 1.5))
    LOCATION_BUTTON_CREDITS = (int(LOCATION_BUTTON_CREDITS[0] / 1.5), int(LOCATION_BUTTON_CREDITS[1] / 1.5))
    LOCATION_BUTTON_TUTORIAL = (int(LOCATION_BUTTON_TUTORIAL[0] / 1.5), int(LOCATION_BUTTON_TUTORIAL[1] / 1.5))
    DISTANCE_DOWN_BUTTON_NEXT_DAY = int(DISTANCE_DOWN_BUTTON_NEXT_DAY / 1.5)
    LOCATION_BUTTON_EMAIL = (int(LOCATION_BUTTON_EMAIL[0] / 1.5), int(LOCATION_BUTTON_EMAIL[1] / 1.5))
    LOCATION_BUTTON_REVIEW = (int(LOCATION_BUTTON_REVIEW[0] / 1.5), int(LOCATION_BUTTON_REVIEW[1] / 1.5))
    LOCATION_BUTTON_BOOKING = (int(LOCATION_BUTTON_BOOKING[0] / 1.5), int(LOCATION_BUTTON_BOOKING[1] / 1.5))
    LOCATION_BUTTON_UPGRADES = (int(LOCATION_BUTTON_UPGRADES[0] / 1.5), int(LOCATION_BUTTON_UPGRADES[1] / 1.5))
    LOCATION_BUTTON_CLOSE = (int(LOCATION_BUTTON_CLOSE[0] / 1.5), int(LOCATION_BUTTON_CLOSE[1] / 1.5))

    LOCATION_BUTTON_CHANGE_EMAIL = (int(LOCATION_BUTTON_CHANGE_EMAIL[0] / 1.5), int(LOCATION_BUTTON_CHANGE_EMAIL[1] / 1.5))
    DISPLACEMENT_BUTTON_CHANGE_EMAIL = (int(DISPLACEMENT_BUTTON_CHANGE_EMAIL[0] / 1.5), int(DISPLACEMENT_BUTTON_CHANGE_EMAIL[1] / 1.5))
    DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL = (int(DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL[0] / 1.5), int(DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL[1] / 1.5))
    LOCATION_EMAIL_CONTENT = (int(LOCATION_EMAIL_CONTENT[0] / 1.5), int(LOCATION_EMAIL_CONTENT[1] / 1.5))
    LOCATION_EMAIL_TEXT_SUBJECT = (int(LOCATION_EMAIL_TEXT_SUBJECT[0] / 1.5), int(LOCATION_EMAIL_TEXT_SUBJECT[1] / 1.5))
    LOCATION_EMAIL_TEXT_SENDER = (int(LOCATION_EMAIL_TEXT_SENDER[0] / 1.5), int(LOCATION_EMAIL_TEXT_SENDER[1] / 1.5))
    LOCATION_EMAIL_TEXT_BODY = (int(LOCATION_EMAIL_TEXT_BODY[0] / 1.5), int(LOCATION_EMAIL_TEXT_BODY[1] / 1.5))
    DISPLACEMENT_EMAIL_TEXT_BODY = (int(DISPLACEMENT_EMAIL_TEXT_BODY[0] / 1.5), int(DISPLACEMENT_EMAIL_TEXT_BODY[1] / 1.5))
    LOCATION_BUTTON_ACCEPT_BOOKING = (int(LOCATION_BUTTON_ACCEPT_BOOKING[0] / 1.5), int(LOCATION_BUTTON_ACCEPT_BOOKING[1] / 1.5))
    LOCATION_BUTTON_DECLINE_BOOKING = (int(LOCATION_BUTTON_DECLINE_BOOKING[0] / 1.5), int(LOCATION_BUTTON_DECLINE_BOOKING[1] / 1.5))
    LOCATION_BUTTON_NEXT_MONTH = (int(LOCATION_BUTTON_NEXT_MONTH[0] / 1.5), int(LOCATION_BUTTON_NEXT_MONTH[1] / 1.5))
    LOCATION_BUTTON_PREVIOUS_MONTH = (int(LOCATION_BUTTON_PREVIOUS_MONTH[0] / 1.5), int(LOCATION_BUTTON_PREVIOUS_MONTH[1] / 1.5))
    LOCATION_CALENDAR_MARKER_0 = (int(LOCATION_CALENDAR_MARKER_0[0] / 1.5), int(LOCATION_CALENDAR_MARKER_0[1] / 1.5))
    LOCATION_CALENDAR_MARKER_1 = (int(LOCATION_CALENDAR_MARKER_1[0] / 1.5), int(LOCATION_CALENDAR_MARKER_1[1] / 1.5))
    LOCATION_CALENDAR_MARKER_2 = (int(LOCATION_CALENDAR_MARKER_2[0] / 1.5), int(LOCATION_CALENDAR_MARKER_2[1] / 1.5))
    LOCATION_CALENDAR_MARKER_3 = (int(LOCATION_CALENDAR_MARKER_3[0] / 1.5), int(LOCATION_CALENDAR_MARKER_3[1] / 1.5))

    LOCATION_BUTTON_CALENDAR_MARKER_0 = (int(LOCATION_BUTTON_CALENDAR_MARKER_0[0] / 1.5), int(LOCATION_BUTTON_CALENDAR_MARKER_0[1] / 1.5))
    LOCATION_BUTTON_CALENDAR_MARKER_1 = (int(LOCATION_BUTTON_CALENDAR_MARKER_1[0] / 1.5), int(LOCATION_BUTTON_CALENDAR_MARKER_1[1] / 1.5))
    LOCATION_BUTTON_CALENDAR_MARKER_2 = (int(LOCATION_BUTTON_CALENDAR_MARKER_2[0] / 1.5), int(LOCATION_BUTTON_CALENDAR_MARKER_2[1] / 1.5))
    LOCATION_BUTTON_CALENDAR_MARKER_3 = (int(LOCATION_BUTTON_CALENDAR_MARKER_3[0] / 1.5), int(LOCATION_BUTTON_CALENDAR_MARKER_3[1] / 1.5))
    LOCATION_CALENDAR = (int(LOCATION_CALENDAR[0] / 1.5), int(LOCATION_CALENDAR[1] / 1.5))

    LOCATION_BUTTON_PC = (int(LOCATION_BUTTON_PC[0] / 1.5), int(LOCATION_BUTTON_PC[1] / 1.5))
    LOCATION_BUTTON_NEXT_WEEK = (int(LOCATION_BUTTON_NEXT_WEEK[0] / 1.5), int(LOCATION_BUTTON_NEXT_WEEK[1] / 1.5))