import random

jokersizdeste = ["S01", "S02", "S03", "S04", "S05", "S06", "S07", "S08", "S09", "S10", "S11", "S12", "S13",
                 "K01", "K02", "K03", "K04", "K05", "K06", "K07", "K08", "K09", "K10", "K11", "K12", "K13",
                 "Q01", "Q02", "Q03", "Q04", "Q05", "Q06", "Q07", "Q08", "Q09", "Q10", "Q11", "Q12", "Q13",
                 "M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"]
#                 Sinek Karo Kupa Maça

distaki = []


class PlayerDefs:
    def __init__(self):
        self.el = []
        self.score = 0
        self.toplam = 0

    def toplamhesabı(self):
        self.toplam = 0
        for kart in self.el:
            self.toplam += PlayerDefs.deger(kart)
        return self.toplam

    def kartcek(self, deste):
        self.el.append(deste[-1])
        del deste[-1]

    @staticmethod
    def deger(kart):
        return int(kart[1] + kart[2])


player = PlayerDefs()
computer = PlayerDefs()
print(player)


def karistir(listt, ite):
    for _ in range(1, ite):
        i = 0
        for kart in listt:
            if random.randint(0, 1) == 1:
                del listt[i]
                distaki.append(kart)
            i += 1
    return listt + distaki


deste = karistir(jokersizdeste, 7)
PlayerDefs.kartcek(player, deste)
PlayerDefs.kartcek(computer, deste)
PlayerDefs.kartcek(player, deste)
PlayerDefs.kartcek(computer, deste)
while player.toplam != 21 or computer.toplam != 21:
    ekran("ask")


print(player.el)

print(123)
