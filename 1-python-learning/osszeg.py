import itertools
# A. match_ends
# Bemenet: sztringek listája. Számoljuk meg, hogy a bemenetben
# hány olyan sztring van, melynek a hossza legalább 2 s az
# első karaktere egyezik az utolsó karakterével. A visszatérési
# érték ezen feltételeket kielégítő sztringek száma legyen.
# Megjegyzés: Pythonban inkrementálásra a ++ helyett a += operátort használjuk.
def match_ends(words):
    counter=0

    for i in words:
        if (len(i)>=2): 
            if (i[0] == i[-1]): counter = counter + 1
    return  counter

# B. front_x
# Bemenet: sztringek listája. Egy olyan listával térjünk vissza,
# melyben a szavak rendezve vannak, viszont az 'x'-szel kezdődő szavak
# kerüljenek előre.
# Példa: ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] bemenet esetén
# az eredmény: ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].
# Tipp: használhatunk 2 listát is, melyeket külön-külön rendezünk, majd
#       egyesítjük őket.
def front_x(words):
    words.sort()
    listx = []
    listg = []
    for i in words:
        if (i[0] == "x"): listx.append(i)
        else:
            listg.append(i)
    listx.sort()
    listg.sort()
    words.clear()

    for i in listx:
        words.append(i)
    for j in listg:
        words.append(j)

    return words

    # D.
# Bemenet: számok rendezett listája.
# Kimenet: a bementből távolítsuk el az ismétlődéseket, vagyis az
# eredményben egy szám csak egyszer szerepeljen.
# Példa: [1, 2, 2, 3] -> [1, 2, 3].
# Készíthetünk egy új listát, vagy módosíthatjuk a bemeneti listát is.
def remove_adjacent(nums):
    new_nums = set(nums)
    nums.clear()
    for i in new_nums:
        nums.append(i)
    return nums

# E.
# Bemenet: két lista, mindkettőben az elemek növekvő sorrendbe rendezve.
# Kimenet: egy összefésült lista, melyben az elemek rendezve szerepelnek.
def list_merge(list1, list2):
    main_list = []
    main_list = [x**2 for x in range(5)]

    return main_list

def main():
    list1 = ['aa', 'xx', 'zz']
    list2 = ['bb', 'cc']
    print(list_merge(list1, list2))


    nums  = [1, 2, 2, 3]
    nums2 = [2, 2, 3, 3, 3]
    nums3 = []
    #print(remove_adjacent(nums3))


    words4 = ['bbb', 'ccc', 'axx', 'xzz', 'xaa']
    words5 = ['ccc', 'bbb', 'aaa', 'xcc', 'xaa']
    words6 = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']
    #print(front_x(words6))

    words  = ['aba', 'xyz', 'aa', 'x', 'bbb']
    words2 = ['', 'x', 'xy', 'xyx', 'xx']
    words3 = ['aaa', 'be', 'abc', 'hello']
    #print(match_ends(words3))


#############################################################################

if __name__ == '__main__':
    main()