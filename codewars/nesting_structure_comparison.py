def same_structure_as(original,other):
    if type(original) == int and type(other) == int:
        return True
    if type(original) != type(other) and (type(original) == list or type(other) == list):
        return False
    if type(original) != list and type(other) != list:
        return True;
    if type(original) == list and type(other) == list:
        if len(original) != len(other):
            return False
        for item in range(len(original)):
            if same_structure_as(original[item], other[item]) == False:
                return False
        return True
    return False

print(same_structure_as([1,[1,1]],[2,[2,2]]))
print(same_structure_as([1,[1,1]],[[2,2],2]))
print(same_structure_as(['[',']',1], [1,'[',']']))