# dictionary practice

my_pc = {"cpu": "i5 6500", "gpu": "rx 590", "ram": "16 gig"}

if "gpu" in my_pc:
    print("Graphics are available")

my_pc["psu"] = 500
print(my_pc)

my_pc["ram"] = "32 gig"

print(my_pc["gpu"])
# or

item_1 = my_pc.get("gpu")
print(item_1)
print(my_pc)

my_pc["games"] = ["cs 2", "dota 2"]

print(my_pc["games"][1])

for item in my_pc["games"]:
    print(item)

my_pc["spacs"] = {"monitor": "1080P", "hz": 144}
print(my_pc["spacs"]["hz"])

