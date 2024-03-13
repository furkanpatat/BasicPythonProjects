"""
Get a 2-digit number from the user and write
a function that finds the reading of this number.
"""
dict1 = {1:"Bir",2:"İki",3:"Üç",4:"Dört",5:"Beş",6:"Altı",7:"Yedi",8:"Sekiz",9:"Dokuz"}
dict2 = {10:"On",20:"Yirmi",30:"Otuz",40:"Kırk",50:"Elli",60:"Altmış",70:"Yetmiş",80:"Seksen",90:"Doksan"}

def pronunciation(x):
    tens_place = number // 10
    ones_place = ((number / 10) - tens_place) * 10
    tens_place *= 10
    ones_place = round(ones_place)
    print(dict2[tens_place],dict1[ones_place])


number = int(input("Enter a two-digit number:"))
pronunciation(number)



