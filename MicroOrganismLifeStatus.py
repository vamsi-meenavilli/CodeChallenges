class Status():
    def __init__(self, time):
        self.time = time
        self.beta = 1
        self.gama = 0
        self.delta = 0
        self.organisms = 1
        self.GetLifeStatus()
        print(self.beta, self.gama, self.delta, sep=', ')

    def GetLifeStatus(self):
        while self.time > 0:
            multiplier = self.GetMultiplier()

            # Beta 0 - 2
            self.time -= 2 * multiplier

            # Gama 3 - 10
            if self.time > 0:
                multiplier = self.GetMultiplier()
                self.beta -= multiplier
                self.gama += multiplier
                self.time -= 8 * multiplier

            # Delta 11 - 26
            if self.time > 0:
                multiplier = self.GetMultiplier()
                self.gama -= multiplier
                self.delta += multiplier
                self.time -= 16 * multiplier

            # Split > 26
            if self.time > 0:
                multiplier = self.GetMultiplier()
                self.delta -= multiplier
                self.beta += 2 * multiplier
                self.organisms = self.beta

        return None

    def GetMultiplier(self):
        return self.organisms if self.time >= self.organisms else 1


if __name__ == "__main__":
    Status(27)
