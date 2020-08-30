import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *

from src.parameters import *
from src.client import create_client
from src.ui import *


class GameMaster():
    def __init__(self):        
        self.week = 0
        self.suite = 5
        self.reputation = INITIAL_REPUTATION
        self.money = INITIAL_MONEY
        self.client_emails = []
        self.clients_rest = [create_client() for i in range(AMOUNT_CLIENTS)]
        # Meter contactos
        self.clients_wanna_booking = []
        self.clients_with_booking = []  # Tuples (week, client)
        self.change_opinion()
        self.generate_emails()

    def change_opinion(self):
        auxiliar_clients_wanna_booking = self.clients_wanna_booking[:]
        for client in auxiliar_clients_wanna_booking:
            if not client.try_booking():
                self.clients_wanna_booking.remove(client)
                self.clients_rest.append(client)

        auxiliar_clients_rest = self.clients_rest[:]
        for client in auxiliar_clients_rest:
            if client.try_booking():
                self.clients_rest.remove(client)
                self.clients_wanna_booking.append(client)


    def change_week(self):
        self.get_notifications()
        self.change_opinion()
        self.week += 1
        self.generate_emails()

    def get_petitions(self):
        return self.clients_wanna_booking

    def get_notifications(self):
        #import pdb; pdb.set_trace()
        ocuped = False
        money = 0
        score = 0
        auxiliar_clients_with_booking = self.clients_with_booking[:]
        for client in auxiliar_clients_with_booking:
            if client[0] == self.week:
                if ocuped:
                    score = client[1].opine(0)
                    client[1].broadcast(score)
                    # La reseña
                else:
                    score = client[1].opine(0)
                    client[1].broadcast(score)
                    money = client[1].spend(self.suite)
                    # La reseña
                    ocuped = True
                self.clients_with_booking.remove(client)
                self.clients_rest.append(client[1])

        self.reputation += score
        self.money += money
        print(score, money)
        return(score, money)

    def decline_booking(self, client):
        self.clients_wanna_booking.remove(client)
        self.clients_wanna_booking.append(client)

    def accept_booking(self, client):
        self.clients_wanna_booking.remove(client)
        month, week = client.get_next_holiday(self.week)
        self.clients_with_booking.append((month * 4 + week, client))

    def generate_emails(self):
        self.client_emails.clear()
        emails_amount = min(len(self.clients_wanna_booking), MAX_EMAILS)
        for client in self.clients_wanna_booking[:emails_amount]:
            month, week = client.get_next_holiday(self.week)
            self.client_emails.append((client, Email(
                "Reserva para {} la {}ª de {}".format(
                    1, week, MONTH_NAMES[month]),
                client.name,
                (week, MONTH_NAMES[month], client.name))))