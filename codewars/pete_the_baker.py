import math

def cakes(recipe, available):
    #return min(available[ingredient] // recipe[ingredient] if ingredient in available.keys() else 0 for ingredient in recipe.keys())

    pieces = []
    for ingredient in recipe:
        try:
            pieces.append(available[ingredient] // recipe[ingredient])
        except:
            return 0
    return min(pieces)

    # pieces = -1
    # for material in recipe.keys():
    #     if available.get(material) == None:
    #         return 0
    #     else:
    #         pieces_by_material = math.floor(available.get(material) / recipe.get(material))
    #         if pieces_by_material < pieces or pieces == -1:
    #             pieces = pieces_by_material
    #
    # return pieces


recipe = {"flour": 500, "sugar": 200, "eggs": 1}
available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
print(cakes(recipe, available))

recipe = {"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}
available = {"sugar": 500, "flour": 2000, "milk": 2000}
print(cakes(recipe, available))