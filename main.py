# Создаем экземпляры пользователей
user1 = User(1, "John Doe")
user2 = User(2, "Jane Doe")

# Создаем экземпляр администратора
admin = Admin(99, "Alice Admin")

# Админ добавляет пользователей
admin.add_user(user1)
admin.add_user(user2)

# Вывод списка пользователей
admin.list_users()

# Админ удаляет пользователя
admin.remove_user(1)

# Вывод обновленного списка пользователей
admin.list_users()
