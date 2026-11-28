#Дана строка. Подсчитать количество содержащихся в ней прописных латинских букв.
def Propis(text):
    count = 0
    for i in text:
        if i.isupper():
            count +=1
    return count

text = input("Введите строку: ")
print(Propis(text))