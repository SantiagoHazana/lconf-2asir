months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
weekDays = ("Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo")

print(months)
print(weekDays)

print("---------------------------")
print(months[3])
print(weekDays[3])

print("---------------------------")
months.append("Neptuno")
print(months)

temp = list(weekDays)
temp.append("Neptune")
weekDays = tuple(temp)
print(weekDays)

print("---------------------------")
months.insert(5, "Urano")
print(months)

temp = list(weekDays)
temp.insert(5, "Urano")
weekDays = tuple(temp)
print(weekDays)

print("---------------------------")
months.pop()
print(months)

temp = list(weekDays)
temp.pop()
weekDays = tuple(temp)
print(weekDays)

print("---------------------------")
months.sort()
print(months)
months.reverse()
print(months)

print("---------------------------")
months.pop(4)
print(months)

temp = list(weekDays)
temp.pop(4)
weekDays = tuple(temp)
print(weekDays)

print("---------------------------")
months.clear()
print(months)

temp = list(weekDays)
temp.clear()
weekDays = tuple(temp)
print(weekDays)

print('------Conjuntos------')
semana = {"Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"}
print(semana)
for i in semana:
    print(i)
