#Дана строка-предложение на русском языке. Подсчитать количество содержащихся в строке гласных букв.
while True:
    try:
        text = input("Введите строку: ")
    except:
        print("invalid input")
    #строка со всеми гласными
    gl="аеёиоуыэюяАЕЁИОУЫЭЮЯ"
    count = 0
    for i in text:
        #если символ из text есть в gl:
        if i in gl:
            count +=1
    print(count)