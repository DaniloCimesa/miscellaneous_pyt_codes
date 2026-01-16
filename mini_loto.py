drawn = [5,11,8,20,42,3,49]
bet = [3,7,19,42,8,36]
hits=0

for num in bet:
    if num in drawn:
        hits+=1

print(f"You have {hits} hits!")