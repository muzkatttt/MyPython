# 3: Создайте программу “Медицинская анкета”,
# где вы запросите у пользователя следующие данные:
# имя, фамилия, возраст и вес.
# Выведите результат согласно которому:
# Пациент в хорошем состоянии, если ему до 30 лет и
# вес от 50 и до 120 кг,
# Пациенту требуется заняться собой, если ему более 30 и
# вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и
# вес менее 50 или больше 120 кг

name = str(input('Введите ваше имя: '))
family_name = str(input('Введите вашу фамилию: '))
age = int(input('Введите ваш возраст: '))
weight = int(input('Введите ваш вес, килограмм: '))
# print(name: str, family_name: str, age: int, weight: int)

if (age > 40) and (120 >= weight >= 50):
    print('срочно требуется врачебный осмотр')

elif (age > 30 and (weight >= 120) or (weight <= 50)):
    print(name, family_name, age, 'лет', 'вес',
          weight, ' - срочно заняться собой')

else:
    age <= 30 and weight >= 50 or weight <= 120
    print(name, 'вы в хорошей физической форме')
