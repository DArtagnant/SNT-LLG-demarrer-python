from random import choice

nums_loto = list(range(1, 50))

def tire(nums, nbr_tirage):
    assert nbr_tirage <= len(nums), "plus de tirage que de boules !"
    b_tire = []
    nums_tour = nums.copy()
    for n in range(nbr_tirage):
        b_tire.append(choice(nums_tour))
        nums_tour.remove(b_tire[-1])
    return b_tire

def tire_loto(): tire(nums_loto, 7)

if __name__ == "__main__":
    print(tire(nums_loto, 7))
    print(tire(nums_loto, 7))
