class Perceptron:
    def __init__(self, n):
        self.w_peso = n

    def soma(self, x):
        soma = 0
        i = 0

        for i, valor in enumerate(self.w_peso):
            soma += x[i] * valor
            print("__________>")
            print(x[i])
            print(valor)
        return soma

    def y_resultado(self, x):
        if(self.soma(x) >= 0):
            return 1
        else:
            return 0

    def treinando(self, p_entrada, yd_resultado_esperado):
        i = 0
        for p in p_entrada:
            for i, valor in enumerate(p):
                erro = yd_resultado_esperado[i] - self.y_resultado(p)
                for w in self.w_peso:
                    w = w + (0.2 * erro * p[i])
                    #print(w)
                    #print(p[i])
                    #print('------')
        #w[i+t] = w[i] + eta * erro * x[i]
        
def main():
    perce_and = Perceptron([-0.6,0.7,0.2])

    #Portas AND.
    And = [[1,0,0], [1,0,1], [1,1,0], [1,1,1]]
    yd = [0,0,0,1]

    perce_and.treinando(And, yd)

    #Reconhecimento do A e T.
    novo = Perceptron(25)
    matriz = [[ 1,1,1,1,1,
                1,0,0,0,1,
                1,1,1,1,1,
                1,0,0,0,1,
                1,0,0,0,1 ],
              
              [ 1,1,1,1,1,
                0,0,1,0,0,
                0,0,1,0,0,
                0,0,1,0,0,
                0,0,1,0,0 ]]

    resultado_esperado = [0,1]

   # novo.treinando(matriz, resultado_esperado)
    
if __name__ == "__main__":
    main()