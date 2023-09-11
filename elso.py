#x = int(input("adj meg egy számot: "))
szam = None
nemjo = True

"""
while nemjo:
    szam_str = (input("szám: "))
    if szam_str.isdecimal():
        nemjo = False
        szam = int(szam_str)
"""

while True:
    szam_str = (input("szám: "))
    if szam_str.isdecimal():
        szam = int(szam_str)
        break


if szam < 3:
    print("kisebb mint 3")
elif szam> 3:
    print("nagyobb mint 3")
#else:
#    print("ez a szám 3")