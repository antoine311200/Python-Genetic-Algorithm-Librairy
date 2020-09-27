def deeplist(func, lst):
    if not isinstance(lst, (list, tuple)):
        print(lst, func(lst))
        return func(lst)
    for i in range(len(lst)):
        lst[i] = deeplist(func, lst[i])
    return lst

def deepdict(func, dct):
    if not isinstance(dct, dict):
        print(dct, func(dct))
        return func(dct)
    for keys,value in dct.items():
        dct[keys] = deepdict(func, value)
    return dct


def deepmap(func, obj, *keysenable):
    if not isinstance(obj, (list, tuple, dict)):
        return func(obj)
    elif isinstance(obj, dict):
        if keysenable:
            old_keys = list(obj.keys())
            new_keys = deepmap(func, old_keys, keysenable)
        for key,value in obj.items():
            obj[key] = deepmap(func, value, keysenable)
        if keysenable:
            obj = dict(zip(new_keys, obj.values()))
    elif isinstance(obj, (list, tuple)):
        for i in range(len(obj)):
            obj[i] = deepmap(func, obj[i], keysenable)
    return obj

def falsify(x):
    if isinstance(x, str):
        return x+"_CHEH"
    if isinstance(x, int):
        return 69

lst = [[1,2,3],[[1,2,3],[4,[4,3],3,2]]]
dct = {
    "test": { "r": 4, "truc": { "e": [2,3]} }
}
print(deepmap(falsify, dct, True))

obj = {
    "test": {
        "coucou": 2, "e": [[1,2,3],[[1,2,3],[4,[4,3],3,2]]]
    },
    "r": { "e" : 3, "r": 1 },
    "e" : [3,2,{"e": 3, "de": [2,3]}]
}

test = {
    "salut": [3,2,12,3,{ "yo": 3, "zebi": [1,2 ]}],
    "coucou": 3,
    "bye": { "eww": 4, "nul": [4,3]}
}

print(deepmap(falsify, test, True))

#print(deeplist(lambda x: x+3, lst))
#print(deepmap(lambda x: x+3, obj))
