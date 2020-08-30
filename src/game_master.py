import pygame, os, random, time as tim
from pygame.locals import *
from src.helpers import *

from src.parameters import *
from src.client import create_client


class GameMaster():
    def __init__(self):
        
        self.week = 0
        self.clients_rest = [create_client() for i in range(AMOUNT_CLIENTS)]
        self.clients_with_booking = []
        self.clients_wanna_booking = []

    def change_opinion(self):
        auxiliar_clients_wanna_booking = self.clients_wanna_booking[:]
        for client in auxiliar_clients_wanna_booking:
            if not client.try_booking(month, week):
                self.clients_wanna_booking.remove(client)
                self.clients_rest.append(client)

        auxiliar_clients_rest = self.clients_rest[:]
        for client in auxiliar_clients_rest:
            if not client.try_booking(month, week):
                self.clients_rest.remove(client)
                self.clients_wanna_booking.append(client)


    def change_week(self):
        self.week += 1
        self.change_opinion()

    def get_petitions(self):
        return self.clients_wanna_booking

    def decline_booking(self, client):
        self.clients_wanna_booking.remove(client)
        self.clients_wanna_booking.append(client)

    def accept_booking(self, client):
        self.clients_wanna_booking.remove(client)
        self.clients_with_booking.append(client)
