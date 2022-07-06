import random

salad_n = random.randint(2,4)
soup_n = random.randint(1,2)
pizza_n = random.randint(3,5)
desserts_n = random.randint(0,2)
fastfood_n = random.randint(0,5)
pies_n = random.randint(0,2)
sushi_n = random.randint(1,2)
rolls_n = random.randint(2,4)
hots_n = random.randint(0,4)
breakfasts_n = random.randint(2,3)


salad = ['Оливье', 'Греческий', 'Цезарь', 'Овощной', 'Селедка под шубой', 'Рыбный']
soup = ['Борщ', 'Окрошка', 'Грибной', 'Гороховый', 'Солянка', 'Гаспачо']
pizza = ['Маргарита', 'Пепперони', 'Карбонара', 'Сырная', 'Мясная']
desserts = ['Чизкейк', 'Печенье', 'Торт', 'Блины', 'Штрудель']
fastfood = ['Чизбургер', 'Фишбургер', 'Чикенбургер', 'Цезарь ролл', 'Шаверма']
pies = ['С вишней', 'С яблоком', 'С мясом', 'С курицей', 'С черникой']
sushi = ['Калифорния', 'С креветкой', 'Курица', 'С лососем', 'С моцареллой']
rolls = ['Ролл с огурцом', 'Ролл с Авокадо', 'Ролл с креветкой', 'Ролл с лососем', 'Запеченый']
hots = ['Котлеты с пюре', 'Курица с грибами', 'Курица с рисом', 'Спагетти', 'Колбаски с пастой']
breakfasts = ['Омлет с беконом', 'Омлет с колбасками', 'Овсянка', 'Сырники', 'Блины со сметаной']


all_lists = [salad, soup, pizza, desserts, fastfood, pies, sushi, rolls, hots, breakfasts]
all_ranges = [salad_n, soup_n, pizza_n, desserts_n, fastfood_n, pies_n, sushi_n, rolls_n, hots_n, breakfasts_n]
lists = []


for a,b in zip(all_lists,all_ranges):
    lists.append(random.sample(a, b))


#Если выбан десерт то удаляются все выбранные салаты
if len(lists[3])!=0:
    lists.remove(lists[0])


for x in lists:
    print(x, end='\n\n')
