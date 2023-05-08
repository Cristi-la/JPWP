#
# TODO: Stwórz metodę "from_coordinates" w klasie "Polyline":
#           1. Spraw aby możliwe było stworzenie identycznych obiektów "Polyline" na dwa sposoby:
#                   pline1 = Polyline( [Point(2, 8), Point(4, 10)] )              # Argumenty wejściowe: lista obiektów klasy Point
#                   pline2 = Polyline.from_coordinates( [(2, 8), (4, 10)] )       # Argumenty wejściowe: lista zawierające tuple z wartościami x i y
#           2. Użyj wbudowanego w pythona dekoratora @classmethod, który pozwala na definiowanie
#              metod klasy, czyli takich, które nie operują na instancjach klasy, ale na samych klasach.
#
#
#  PODPOWIEDZ: pierwszym argumentem wejściowym metody from_coordinates z dekoratorem  @classmethod będzie:
#                   argument reprentuje klasę, a nie instancję obiektu, który jest aktualnie tworzony.
#
#                   def test(cls, *args, **kwargs):
#                       cls(Point(2,8), Point(4,8)) # gdzie wywołanie "cls" to tak naprawdę to: Polyline(Point(2,8), Point(4,8))
#
import math


class Point:
    ''' Klasa punktu 2d '''
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def distance(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)


class Polyline:
    ''' Klasa lini łamanej 2d '''
    def __init__(self, points):
        self.points = points

    # Dokończ poniższą metode
    # def from_coordinates(...):

    def length(self):
        total_length = 0
        for i in range(len(self.points) - 1):
            total_length += self.points[i].distance(self.points[i + 1])
        return total_length


if __name__ == "__main__":
    pline1 = Polyline([Point(2, 8), Point(4, 10), Point(7, 1), Point(6, 9)])
    pline2 = Polyline.from_coordinates([(2, 8), (4, 10), (7, 1), (6, 9)])

    ''' 
    Instrukcja assert - 
        pozwala na weryfikację poprawności kodu w trakcie jego działania. 
        Instrukcja assert sprawdza, czy podane wyrażenie jest prawdziwe,
        jeśli nie jest prawdziwe wywołuje wyjątek "AssertionError".
    '''

    assert pline1.length() == pline2.length()
