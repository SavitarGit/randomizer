import random

k = random.randint(2,4)
n = random.randint(1,2)
z = random.randint(3,5)
m = random.randint(0,2)
q = random.randint(0,5)
t = random.randint(0,2)
o = random.randint(1,2)
p = random.randint(2,4)
y = random.randint(0,4)
g = random.randint(2,3)


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
all_ranges = [k, n, z, m, q, t, o, p, y, g]
lists = []


for a,b in zip(all_lists,all_ranges):
    lists.append(random.sample(a, b))


for x in lists:
    print(*x, sep=", ", end='\n\n')