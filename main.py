from mecaniques.combat import combat
from mecaniques.lastfight import lastfight
from functions.prompting import clear_screen
from functions.prompting import prompting
from classes.Pokemon import Pokemon
from classes.Dresseur import Dresseur
from classes.Equipe import Equipe
from classes.Entite import Entite
from lore.cynthiaLines import *
from lore.lore import *
from lore.interactionsLines import *
import time


Red = Dresseur("Red", 300, 20, 10, 10, Equipe([Pokemon("Dracofeu", 50, 9, 5, 10),Pokemon("Spectrum", 40, 6, 3, 10), Pokemon("Pikachu", 35, 12, 10, 25), Pokemon("Pingoléon", 50, 8, 2, 10), Pokemon("Gardevoir", 50, 8, 2, 10)]))
Cynthia = Dresseur("Cynthia",300, 17, 8, 0, Equipe([Pokemon("Bulbizarre", 35, 5, 3, 8),Pokemon("Tiplouf", 25, 8, 2, 10),Pokemon("Zarbi", 20, 5, 3, 8),Pokemon("Pichu", 35, 5, 3, 8),Pokemon("Metamorph", 30, 5, 3, 8),]))

clear_screen()
print(pokemon_logo)
time.sleep(3)
clear_screen()

time.sleep(1)
prompting(lore1)
time.sleep(1)
prompting(lore2)

time.sleep(3)
clear_screen()
prompting(lore3)

time.sleep(2)
clear_screen()
prompting("Cynthia :\n")
prompting(startDial)
time.sleep(1)
prompting(startDial2)
time.sleep(1)
prompting(startDial3)

time.sleep(1)
clear_screen()

prompting(initCombat)
time.sleep(1)
clear_screen()

prompting("Cynthia a choisi Bulbizarre !\n")
time.sleep(1)

combat(Red, Cynthia, 0)
lastfight(Red, Cynthia)