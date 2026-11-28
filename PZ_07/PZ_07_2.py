#Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке гласных букв.
def glas(text):
    gl="аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for i in text:
        if i in gl:
            count +=1
    return count

text = input("Введите строку: ")
print(glas(text))