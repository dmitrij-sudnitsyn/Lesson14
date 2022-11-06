import pickle

name = "Nikolay"
age = 29

# setup = {
#     "lang":"Uk",
#     "timeZone":"+2"
# }

# with open("test.dll", mode="wb") as file:
#     # pickle.dump(setup, file)
#     pass


with open("test.dll", mode="rb+") as file:
    try:
        setup = pickle.load(file)
        print(setup)
    except:
        setup = {
            "lang":"Uk",
            "timeZone":"+2"
            }
        pickle.dump(setup, file)

print("End")

setup = {}
with open("test.dll", mode="rb+") as file:
    setup = pickle.load(file)
    setup['lang'] = 'En'

with open("test.dll", mode="wb+") as file:
    pickle.dump(setup, file)

import json

# setup = {
#     "lang":"Uk",
#     "timeZone":"+2"
# }
# with open("test.json", mode="w") as file:
#     json.dump(setup, file)
setup2 = None
with open("test.json", mode="r") as file:
    setup2 = json.load(file)
    print(setup2)

with open("test.json", mode="w") as file:
    json.dump(setup2, file)


#Удаление заданной  по номеру строки из файла
n = 4
st = []

with open("todo2.txt", mode="r", encoding="utf") as file:
    st = file.readlines()

st.pop(n-1)

with open("todo2.txt", mode="w", encoding="utf") as file:
    file.writelines(st)

import datetime

class LogMsg:
    def __init__(self, typeMsg, msg):
        self.typeMsg = typeMsg
        self.msg = msg
        self.time = datetime.datetime.now()

    def __str__(self):
        return f"{self.time} {self.typeMsg} {self.msg}"


log = LogMsg("Info", "Create file")
print(log)
#log
# Дата/Время Warning Text
def log_write(log):
    # date = datetime.datetime.now()
    with open("log.txt", mode="a", encoding="utf") as file:
        file.writelines(f"{log.time} {log.typeMsg} {log.msg}\n")

log_write(log)

