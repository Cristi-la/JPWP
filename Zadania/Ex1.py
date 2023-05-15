#
# TODO: Stwórz trzy dekoratory, które ozdobią tekst zwracany przez funkcję "hello_word"
#       tagami html'a: pogrubienie (<b></b>), kursywa (<i></i>) i podkreślenie (<ins></ins>)
#
# WAŻNE: nie zmieniaj działania funkcji "hello_word" - tylko dekorator powinien wpływać na jej działanie
#
# Oczekiwany OUTPUT:
#   <b><i><ins>hello world</ins></i></b>

# ---------------------------------------
# -------- Miejsce na twój kod ----------


# ---------------------------------------

# @make_bold      # <b>...</b>
# @make_italic    # <i>...</i>
# @make_underline # <ins>...</ins>
def hello_word():
    return "hello world"


if __name__ == "__main__":
    print(hello_word())
