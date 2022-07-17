import lib.logo as logo
hit = 0
f = open("../return/ID.txt", "r")
fw = open("../return/Target.txt", "w")
lines = f.readlines()
print(logo.logo)
for Id_acc in lines:
    print(f"<@{Id_acc.strip()}>")
    fw.write(f"<@{Id_acc.strip()}>\n")
    hit = hit + 1
fw.close()
print("\nHit : ", hit)

