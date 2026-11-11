class Televisao:
    def __init__(self, pcanal, menor, maior):
        self.canal = pcanal
        self.cmin = menor
        self.cmax = maior

    def muda_canal_para_baixo(self):
        if self.canal == self.cmin:
            self.canal = self.cmax
        else:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal == self.cmax:
            self.canal = self.cmin
        else:
            self.canal += 1

#Criando uma TV que contem o canal inicial, maior e menor canal.
tv = Televisao(pcanal=2, menor=2, maior=11)

#Verificando o canal atual
print(f"Canal atual: {tv.canal}")

#Diminuindo o canal
tv.muda_canal_para_baixo()
print(f"Canal após descer: {tv.canal}")

#Aumentando o canal
tv.muda_canal_para_cima()
print(f"Canal após subir: {tv.canal}")
    