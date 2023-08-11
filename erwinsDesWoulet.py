from random import*
for erw in range(5):
    nimewoOdi=randint(26,96)
    nimewoIti=int(input("Antre nimewo paw la :"))
    if nimewoIti==nimewoOdi:
        print("Ou genyen, ou jwenn nimewo kache a.")
    elif nimewoIti<nimewoOdi:
        print("Nimewo ou chwazi a pi piti ke nimewo kache a.")
    else:
        print("Nimewo ou chwazi a pi gwo ke nimewo kache a.")
        
print("Fen pwogram!")
