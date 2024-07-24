immutable_bar = (1, 2, 3, 'hello', False, [1, 2])
print(immutable_bar)
# immutable_bar[0] = 66
# Если попытаться заменить элементы кортежа, то будет ошибка, т.к кортеж являтся неизменяемым типом.Из-за этого не можем добавлять или удалять элементы в кортеже.
# Но если внутри кортежа есть списко, то этот список можно вызвать и изменить
immutable_bar[5][1] = 6
print(immutable_bar)

mutable_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(mutable_list)
mutable_list[9] = 10
print(mutable_list)