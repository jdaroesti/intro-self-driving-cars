import itertools


DICES_SUM = 7


space = [dice_throw for dice_throw in itertools.product(range(1, 7), repeat=2)]
result = [r for r in filter(lambda dice_throw: dice_throw[0] + dice_throw[1] == DICES_SUM, space)]

print(len(result) / len(space))
print(result)
