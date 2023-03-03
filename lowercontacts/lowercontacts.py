import vobject
import sys

with open(sys.argv[1]) as readfile:
    writefile = open(sys.argv[2], "a")
    for card in vobject.readComponents(readfile.read()):
        card.n.value = vobject.vcard.Name(family=card.n.value.family.lower(), given=card.n.value.given.lower())
        writefile.write(card.serialize())
        print(f"lowercased {card.n.value}")