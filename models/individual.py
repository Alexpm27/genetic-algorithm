class Individual:
    def __init__(self, chromosome, decimal, x, y):
        self.chromosome = chromosome,
        self.decimal = decimal,
        self.x = x,
        self.y = y

    def __str__(self):
        return f"Chromosome: {self.chromosome}, Decimal: {self.decimal}, X: {self.x}, Y: {self.y}"

    def __eq__(self, other):
        return isinstance(other, Individual) and self.__dict__ == other.__dict__

    def __hash__(self):
        return hash(tuple(sorted(self.__dict__.items())))
