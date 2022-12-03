

# Домашнее задание к лекции «Открытие и чтение файла, запись в файл»

f = open('recepies.txt', 'rt')
cook_book = {}
recepie = {}
for str in f:
    dish = str.strip()
    ingr_cnt = int(f.readline())
    ingrs = []
    for _ in range(ingr_cnt):
        ing = f.readline().split('|')
        ing_name, ing_quant, ing_measure = ing
        ingrs.append({'ingredient_name': ing_name,
                      'quantity': ing_quant,
                      'measure': ing_measure})
    f.readline()
    recepie = {dish: ingrs}
    cook_book[dish] = ingrs
f.close()

print(cook_book)

order_dish = ''
order_list = []
pers = 0
pers = int(input('Введите кол-во персон \n'))
print('Введите название блюда из меню, если закончили заказ, введите 0:')
while order_dish != '0':
    if order_dish:
        if order_dish in cook_book.keys():
            order_list.append(order_dish)
        else:
            print('Такого блюда в меню нет')
    order_dish = input()

print (order_list)

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for ingr in cook_book[dish]:
                if ingr['ingredient_name'] in shop_list.keys():
                    quan = int(ingr['quantity'])*person_count + int(shop_list[ingr['ingredient_name']]['quantity'])
                else:
                    quan = int(ingr['quantity'])*person_count
                shop_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': quan }
    return shop_list

# order_list = ['Омлет', 'Фахитос']
# pers =2

print (get_shop_list_by_dishes(order_list, pers))