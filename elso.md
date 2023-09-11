# Prog óra 2023.09.11

## Címsor 2

### Címsor 3

- első 
- második
- harmadik

1. első
1. második
1. harmadik
```python
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


```