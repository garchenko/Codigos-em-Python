class Circulo():

    _total_circulos = 0

    def __init__(self, pontox, pontoy, raio):
        self.pontox = pontox
        self.pontoy = pontoy
        self.raio = raio
        Circulo._total_circulos += 1

circ1 = Circulo(1, 1, 10)
print(circ1._total_circulos)

circ2 = Circulo(2, 2, 20)
print(circ2._total_circulos)

print(Circulo.total_circulos)