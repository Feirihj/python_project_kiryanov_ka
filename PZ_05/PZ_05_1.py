# C помощью функций получить вертикальную и горизонтальную линии.
# Линия проводится многократной печатью символа.
# Заключить слово в рамку из полученных линий.


def Ramka(word):
    length = len(word)
    def horlin(length):
        print("#"*(length+2))
    horlin(length)
    print("#"+word+"#")
    horlin(length)

while True:
    try:
        word = input("Введите слово: ")
    except:
        print("invalid input")
    Ramka(word)