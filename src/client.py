from src.parameters import *
import random
import pprint

aux_names = NAMES[:]

class Client():
    def __init__(self, name, purchasing_power, travel_frequency,
                opinion, minimum_expectation, influenceable,
                preferences, deterioration, vip):
        self.name = name
        self.purchasing_power = purchasing_power
        self.travel_frequency = travel_frequency
        self.holidays = []
        self.set_holidays_calendar()
        self.opinion = opinion
        self.minimum_expectation = minimum_expectation
        self.influenceable = influenceable
        self.preferences = preferences
        self.deterioration = deterioration
        self.vip = vip
        self.contacts = []

    def set_cotacts(self, contacts):
        self.contacts = contacts

    def set_holidays_calendar(self):
        self.holidays = []
        for i in range(12):
            aux = []
            for ii in range(4):
                aux.append(random.random() < self.travel_frequency)
            self.holidays.append(aux)

    def broadcast(self, score):
        for contact in self.contacts:
            contact.listen(score)

    def broke(self, suite_state):
        for element, state in suite_state:  # Maybe all room
            suite_state[element] = state * self.deterioration[element]

    def spend(self, suite_state):
        pass


    # INSISTIR Y PREPARAR PARA RESERVAS DE VARIASPERSONAS
    def try_booking(self):
        return True if self.opinion >= self.minimum_expectation else False

    def get_next_holiday(self, week):
        current_month = int(week / 4)
        for month in range(current_month+1,12):
            for week in range(4):
                if self.holidays[month * week]:
                    return (month, week)
        return False

    def opine(self, suite_state):
        score = 0
        for issue, value in suite_state:
            score += self.preferences[issue] * value
        self.opinion += score
        self.opinion -= 3 * len(suite_state)
        return score




def create_client():
    name = aux_names.pop()
    purchasing_power = random.randrange(3) # Poco, medio, bastante
    travel_frequency = random.random()
    opinion = random.randrange(50,200)
    minimum_expectation = random.randrange(100)
    influenceable = random.randrange(1,3)
    preferences = {}
    deterioration = {}
    for element in ROOM_ELEMENTS:
        preferences[element] = random.randrange(1,11)
        deterioration[element] = random.randrange(30)
    vip = True if random.random() < VIP_PROBABILITY else False

    pepe = Client(name, purchasing_power, travel_frequency,
                opinion, minimum_expectation, influenceable,
                preferences, deterioration, vip)

    return pepe