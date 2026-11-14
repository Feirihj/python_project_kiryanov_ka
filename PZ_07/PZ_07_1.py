#Дана строка. Подсчитать количество содержащихся в ней прописных латинских букв.
while True:
    try:
        text = input("Введите строку: ")
    except:
        print("invalid input")
    count = 0
    for i in text:
        if 'A' <= i <= 'Z':
            count +=1
    print(count)