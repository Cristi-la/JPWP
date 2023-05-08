#
# TODO: Stwórz sparametryzowany dekorator który opóźni wykonanie funkcji:
#       "make_coffe" o 2 sekund,
#       "hard_work" o 4 sekund i
#       "break_free" o 6 sekund
#
# WAŻNE: nie zmieniaj działanie tych funkcji - tylko dekorator powinien wpływać na ich działanie
#
# PODPOWIEDZ: biblioteka asyncio posiada funkcję sleep: await asyncio.sleep(time)
#
# Oczekiwany OUTPUT:
#    await - oznacza, że czekamy na zakończenie funkcji sleep(...)
#    Coffee making, bleep bloop
#    Working very hard, clank clank, buzz buzz, hiss hiss, zzzzt zzzzt
#    Free at last, free at last. Thank God almighty we are free at last. Whirrrr, beep beep, clank

import asyncio

# ---------------------------------------
# -------- Miejsce na twój kod ----------


# ---------------------------------------


# @sleep(time=2)
async def make_coffee():
    print('Coffee making, bleep bloop')

# @sleep(time=4)
async def hard_work():
    print('Working, very, hard, clank clank, buzz buzz, hiss hiss, zzzzt zzzzt')

# @sleep(time=6)
async def break_free():
    print('Free at last, free at last. Thank God almighty we are free at last. Whirrrr, beep beep, clank')


if __name__ == "__main__":

    #
    # UWAGA! Poniższe informację sa zbędne do rozwiązanie powyższego zadanie.
    #        Zostały umieszczony tylko w celu wyjaśnienia kodu, DLA CHĘTNYCH
    #

    ''' 
    Tworzenie pętli asynchronicznej - 
        to mechanizm w Pythonie, który umożliwia wykonywanie
        wielu zadań asynchronicznie i równolegle, bez 
        konieczności oczekiwania na zakończenie
    '''
    loop = asyncio.get_event_loop()

    '''
    Tworzenie listy obiektów funkcji
    
    Czemu funkcje nie wykonują się w liscie tasks, przecież mają "()" ???
        Nawiasy te oznaczają tylko to, że mamy do czynienia z obiektami funkcji, a nie ich wykonaniem.
        Poniższe (asynchroniczne) funkcje nie wykonują się natychmiast po ich 
        wywołaniu, ale zamiast tego zwracają obiekt coroutine,który może być 
        uruchomiony w pętli asynchronicznej
    
        print(tasks)
        # tasks = [
        #    <coroutine object make_coffe at 0x000001C1E14D65C0>,
        #    <coroutine object hard_work at 0x000001C1E14F9D40>,
        #    <coroutine object break_free at 0x000001C1E154BEC0>
        # ]
    '''
    tasks = [break_free(), make_coffee(), hard_work()]

    '''
     Uruchomienie pętli i czekanie, aż wszystkie zadania w tasks zostaną zakończone
    '''
    loop.run_until_complete(asyncio.gather(*tasks))

    '''
    Zamyka pętlę asynchroniczną, aby zwolnić zasoby systemowe
    '''
    loop.close()
