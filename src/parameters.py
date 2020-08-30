# Display
MASTER_VOLUMEN = 0.1
RESOLUTION_1080 = False
WIDTH  = 1920
HEIGHT = 1080

#WIDTH  = 1280
#HEIGHT = 720
ASPECT_RELATION_PLAYER = 2.4
ASPECT_RELATION_CHAT = 0.6
WIDTH_PLAYER_SPRITE = 100
HEIGHT_CHAT = 680
WIDTH_OBJECT = 100
WIDTH_OBJECT_ICON = 20

PLAYER_SURFACE = (WIDTH_PLAYER_SPRITE, int(WIDTH_PLAYER_SPRITE * ASPECT_RELATION_PLAYER))
CHAT_SURFACE = (int(HEIGHT_CHAT * ASPECT_RELATION_CHAT), HEIGHT_CHAT)
OBJECT_SURFACE = (WIDTH_OBJECT, WIDTH_OBJECT)
OBJECT_SURFACE_ICON = (WIDTH_OBJECT_ICON, WIDTH_OBJECT_ICON)



AMOUNT_CLIENTS = 13
MAX_EMAILS = 9
#Icons in the coumputer screen for Mail, Reviews, Bookings and Upgrades.
# Locations buttons
LOCATION_BUTTON_EMAIL = (760, 500)  # 720
LOCATION_BUTTON_REVIEW = (1160, 500)  # 720
LOCATION_BUTTON_BOOKING = (760, 800)  # 720
LOCATION_BUTTON_UPGRADES = (1160, 795)  # 720

#Buttons of the emails you receive
LOCATION_BUTTON_CHANGE_EMAIL = (483, 205)  # 720
DISPLACEMENT_BUTTON_CHANGE_EMAIL = (0, 75)  # 720

#User name inside email button
DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL = (0, 0)  # 720


#Content of the emails
LOCATION_EMAIL_CONTENT = (889, 539)  # 720
LOCATION_EMAIL_TEXT_SUBJECT = (696, 213)  # 720
LOCATION_EMAIL_TEXT_SENDER = (696, 261)  # 720
LOCATION_EMAIL_TEXT_BODY = (739, 354)  # 720

#Response for the emails, Accept o Decline the booking
LOCATION_BUTTON_ACCEPT_BOOKING = (839, 791)  # 720
LOCATION_BUTTON_DECLINE_BOOKING = (997, 791)  # 720

#Calendar and buttons to change the month displayed
LOCATION_CALENDAR = (1395, 391)
LOCATION_BUTTON_NEXT_MONTH = (1536, 411)  # 720
LOCATION_BUTTON_PREVIOUS_MONTH = (1254, 411)  # 720

#Marker that selects the week you want to book
LOCATION_CALENDAR_MARKER_0 = (1395, 374)  # 720
LOCATION_CALENDAR_MARKER_1 = (1395, 402)  # 720
LOCATION_CALENDAR_MARKER_2 = (1395, 430)  # 720
LOCATION_CALENDAR_MARKER_3 = (1395, 458)  # 720



LOCATION_BUTTON_CALENDAR_MARKER_0 = (1395, 374)
LOCATION_BUTTON_CALENDAR_MARKER_1 = (1395, 402)
LOCATION_BUTTON_CALENDAR_MARKER_2 = (1395, 430)
LOCATION_BUTTON_CALENDAR_MARKER_3 = (1395, 458)


SIZE_TEXT_USER_NAME = 18
SIZE_TEXT_SUBJECT = 24
SIZE_TEXT_SENDER = 18
SIZE_TEXT_BODY = 14




# Level config

# HUB









## 720
if not RESOLUTION_1080:
	LOCATION_BUTTON_EMAIL = (int(LOCATION_BUTTON_EMAIL[0] / 1.5), int(LOCATION_BUTTON_EMAIL[1] / 1.5))
if not RESOLUTION_1080:
	LOCATION_BUTTON_REVIEW = (int(LOCATION_BUTTON_REVIEW[0] / 1.5), int(LOCATION_BUTTON_REVIEW[1] / 1.5))
if not RESOLUTION_1080:
	LOCATION_BUTTON_BOOKING = (int(LOCATION_BUTTON_BOOKING[0] / 1.5), int(LOCATION_BUTTON_BOOKING[1] / 1.5))
if not RESOLUTION_1080:
	LOCATION_BUTTON_UPGRADES = (int(LOCATION_BUTTON_UPGRADES[0] / 1.5), int(LOCATION_BUTTON_UPGRADES[1] / 1.5))

if not RESOLUTION_1080:
    LOCATION_BUTTON_CHANGE_EMAIL = (int(LOCATION_BUTTON_CHANGE_EMAIL[0] /1.5), int(LOCATION_BUTTON_CHANGE_EMAIL[1] / 1.5))
if not RESOLUTION_1080:
    DISPLACEMENT_BUTTON_CHANGE_EMAIL = (int(DISPLACEMENT_BUTTON_CHANGE_EMAIL[0] /1.5), int(DISPLACEMENT_BUTTON_CHANGE_EMAIL[1] / 1.5))
if not RESOLUTION_1080:
    DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL = (int(DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL[0] /1.5), int(DISPLACEMENT_NAME_BUTTON_CHANGE_EMAIL[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_EMAIL_CONTENT = (int(LOCATION_EMAIL_CONTENT[0] /1.5), int(LOCATION_EMAIL_CONTENT[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_EMAIL_TEXT_SUBJECT = (int(LOCATION_EMAIL_TEXT_SUBJECT[0] /1.5), int(LOCATION_EMAIL_TEXT_SUBJECT[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_EMAIL_TEXT_SENDER = (int(LOCATION_EMAIL_TEXT_SENDER[0] /1.5), int(LOCATION_EMAIL_TEXT_SENDER[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_EMAIL_TEXT_BODY = (int(LOCATION_EMAIL_TEXT_BODY[0] /1.5), int(LOCATION_EMAIL_TEXT_BODY[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_BUTTON_ACCEPT_BOOKING = (int(LOCATION_BUTTON_ACCEPT_BOOKING[0] /1.5), int(LOCATION_BUTTON_ACCEPT_BOOKING[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_BUTTON_DECLINE_BOOKING = (int(LOCATION_BUTTON_DECLINE_BOOKING[0] /1.5), int(LOCATION_BUTTON_DECLINE_BOOKING[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_BUTTON_NEXT_MONTH = (int(LOCATION_BUTTON_NEXT_MONTH[0] /1.5), int(LOCATION_BUTTON_NEXT_MONTH[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_BUTTON_PREVIOUS_MONTH = (int(LOCATION_BUTTON_PREVIOUS_MONTH[0] /1.5), int(LOCATION_BUTTON_PREVIOUS_MONTH[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_CALENDAR_MARKER_0 = (int(LOCATION_CALENDAR_MARKER_0[0] /1.5), int(LOCATION_CALENDAR_MARKER_0[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_CALENDAR_MARKER_1 = (int(LOCATION_CALENDAR_MARKER_1[0] /1.5), int(LOCATION_CALENDAR_MARKER_1[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_CALENDAR_MARKER_2 = (int(LOCATION_CALENDAR_MARKER_2[0] /1.5), int(LOCATION_CALENDAR_MARKER_2[1] / 1.5))
if not RESOLUTION_1080:
    LOCATION_CALENDAR_MARKER_3 = (int(LOCATION_CALENDAR_MARKER_3[0] /1.5), int(LOCATION_CALENDAR_MARKER_3[1] / 1.5))