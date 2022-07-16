







import json






def roman(num: int) -> str:

    chlist = "VXLCDM"
    rev = [int(ch) for ch in reversed(str(num))]
    chlist = ["I"] + [chlist[i % len(chlist)] + "\u0304" * (i // len(chlist))
                    for i in range(0, len(rev) * 2)]

    def period(p: int, ten: str, five: str, one: str) -> str:
        if p == 9:
            return one + ten
        elif p >= 5:
            return five + one * (p - 5)
        elif p == 4:
            return one + five
        else:
            return one * p

    return "".join(reversed([period(rev[i], chlist[i * 2 + 2], chlist[i * 2 + 1], chlist[i * 2])
                            for i in range(0, len(rev))]))

def create():
	with open("base.json", "r") as f:
		data = json.load(f)
	for i in range(1, 1001):
		data["potion.potency."+str(i)] = roman(i)
	data["potion.potency.0"]=""
	for i in range(1, 1001):
		data["enchantment.level."+str(i)] = roman(i)

	
	#create a en_us.json file
	with open("en_us.json", "w") as f:
		json.dump(data, f,indent=4)