
def Menu(file):
    file = open(file, 'r')
    food = []
    ingredients = []
    for line in file:
        line = line.rstrip()
        if line != "" and line[0].isupper() and not line.endswith(':'): #food
            food.append(line)
        elif line != "" and line[0].islower() and line not in ingredients: #ingredients
            ingredients.append(line)
            ingredients = sorted(ingredients)
    print(food)
    x = 0
    menu = {}
    for i in food:
        menu.update({i : []})
    while x <= len(food):
        menu[food[x]].append(1)
        x += 1

            
    
    return menu

    # menu = {}
    # for i in food:
    #     i = i.rstrip()
    #     if i not in menu:
    #         menu.update({i : []})
    #     menu[i].append(i)
    # return menu

# def ingredients():



# def drinks():






print(Menu("spam.txt"))