class Client():
    def __init__(self, name, purchasing_power, travel_frequency,
                opinion, minimum_expectation, influenceable,
                preferences, deterioration, vip):
        self.name = name
        self.purchasing_power = purchasing_power
        self.travel_frequency = travel_frequency
        self.opinion = opinion
        self.minimum_expectation = minimum_expectation
        self.influenceable = influenceable
        self.preferences = preferences
        self.deterioration = deterioration
        self.vip = vip
        self.contacts = []

    def set_cotacts(self, contacts):
        self.contacts = contacts

    def broadcast(self, score):
        for contact in self.contacts:
            contact.listen(score)

    def broke(self, suite_state):
        for element, state in suite_state:  # Maybe all room
            suite_state[element] = state * self.deterioration[element]

    def spend(self, suite_state):
        pass


    # INSISTIR Y PREPARAR PARA RESERVAS DE VARIASPERSONAS
    def try_booking(self, month, day):
        if self.holidays(month, day) and self.opinion >= self.minimum_expectation:
            return (self.name, self.vip)
        else:
            return False

    def holidays(self, month, day):
        selector = random.random()
        if self.travel_frequency[month][day] < selector:
            return True
        else:
            return False

    def opine(self, suite_state):
        score = 0
        for issue, value in suite_state:
            score += self.preferences[issue] * value
        self.opinion += score
        self.opinion -= 3 * len(suite_state)
        return score




def create_client():
    name = NAMES.pop()
    purchasing_power = random.randrange(3) # Poco, medio, bastante
    travel_frequency = [[random.random() for ii in range(4)] for i in range(12)]
    opinion = random.range(50)
    minimum_expectation = random.range(100)
    influenceable = random.range(1,3)
    preferences = {}
    deterioration = {}
    for element in ROOM_ELEMENTS:
        preferences[element] = random.random(1,11)
        deterioration[element] = random.random(30)
    vip = True if random.random() < VIP_PROBABILITY else False

    return Client(name, purchasing_power, travel_frequency,
                opinion, minimum_expectation, influenceable,
                preferences, deterioration, vip)
