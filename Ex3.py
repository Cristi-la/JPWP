#
# TODO: Stwórz sparametryzowany dekorator który wyśietli następujące informację
#       PO WYKONANIU funkcji 'make_donuts_great_again':
#           1. Czas wykonanie funkcji:
#           2. Parmatery wejściowe funkcji:
#           3. Wartość zwracana
#           4. Comentarz przekazany na wejściu dekoratora
#
# WAŻNE: nie zmieniaj działanie funkcji "make_donuts_great_again" - tylko dekorator powinien wpływać na jej działanie
#
# PODPOWIEDZ: w Pythonie argumenty przekazywane do funkcji są przekazywane przez referencję,
#             co oznacza, że zmiany wprowadzone do argumentów wewnątrz funkcji będą wprowadzone
#             do oryginalnych argumentów przekazywanych do funkcji.
#             Funkcja copy.deepcopy() może okazać się pomocna w tym zadaniu. (import copy)
#
# Oczekiwany OUTPUT:
#
#   I'm going in to fix the donut's chakra!
#   Watch out, I'm about to stuff this donut like a Thanksgiving turkey! What now America!
#   -----------------------------------------------
#   Komentarz: Bardzo dobry pączek!
#   Parametry wejściowe funkcji: args: American Style Donut
#   Czas wykonania funkcji: 2.00190s
#   Wartość zwracana: European Style Donut
#
import time
# import copy

# ---------------------------------------
# -------- Miejsce na twój kod ----------


# ---------------------------------------


class Donut:
    def __init__(self):
        self.is_american_style = True
        self.has_hole = True

    def __str__(self):
        if self.is_american_style or self.has_hole:
            return 'American Style Donut'
        else:
            return 'European Style Donut'

    def fix_the_center(self):
        print("I'm going in to fix the donut's chakra!")
        time.sleep(1)
        self.has_hole = False

    def add_stuffing(self):
        print("Watch out, I'm about to stuff this donut like a Thanksgiving turkey! What now America!")
        time.sleep(1)
        self.is_american_style = False


# @get_information('Bardzo dobry pączek!')
def make_donuts_great_again(donut_object):
    # We're gonna build a "dobry pączek", and make the Americans pay for it!

    donut_object.fix_the_center()
    donut_object.add_stuffing()

    return donut_object


if __name__ == "__main__":
    my_precious_secret = Donut()
    make_donuts_great_again(my_precious_secret)
