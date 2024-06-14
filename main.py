import django_setup

from managment.models import User

while True:
    a = input("1 - Додати користувача до бази даних\n2 - Оновити роль користувача\n3 - Видалити користувача\n4 - Закінчити роботу пограми")
    match a:
        case "1":
            name = input("Name: ")
            email = input("Email: ")
            role = input("Role (admin, user)")
            User(name = name, email = email, role = role).save()
        case "2":
            idn = int(input("ID: "))
            user = User.objects.get(id = idn)
            user.role = input("Role (admin, user): ")
            user.save()
        case "3":
            idn = int(input("ID: "))
            User.objects.get(id=idn).delete()
        case "4":
            break