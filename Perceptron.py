import random

class Perceptron:
    def __init__(self, eta ,n):
        self.w_peso = n
        self.eta_n = eta

    def soma(self, x):
        soma = 0
        for i, valor in enumerate(self.w_peso):
            soma += x[i] * valor
        return soma

    def y_resultado(self, x):
        if(self.soma(x) >= 0):
            return 1
        else:
            return 0

    def treinando(self, p_entrada, yd_resultado_esperado):
        tem_erro = 1
        while(tem_erro != 0):
            tem_erro = 0
            for idx,p in enumerate(p_entrada):
                erro = yd_resultado_esperado[idx] - self.y_resultado(p)
                if erro != 0:
                    tem_erro = 1
                    for i,w in enumerate(self.w_peso):
                        self.w_peso[i] = self.w_peso[i] + (self.eta_n * erro * p_entrada[idx][i])
        #w[i+t] = w[i] + eta * erro * x[i]
        
def main():
    perceptron = Perceptron(0.2,[-0.6,0.7,0.2])

    #Portas AND.
    And = [[1,0,0], [1,0,1], [1,1,0], [1,1,1]]
    yd = [0,0,0,1]
    perceptron.treinando(And, yd)

    print("Resultado Porta And:")
    print(perceptron.y_resultado(And[0]))
    print(perceptron.y_resultado(And[1]))
    print(perceptron.y_resultado(And[2]))
    print(perceptron.y_resultado(And[3]))
    print("_________________________________________________")

    #Porta OR.
    Or = [[1,0,0], [1,0,1], [1,1,0], [1,1,1]]
    yd = [0,1,1,1]
    perceptron.treinando(Or, yd)

    print("Resultado Porta Or:")
    print(perceptron.y_resultado(Or[0]))
    print(perceptron.y_resultado(Or[1]))
    print(perceptron.y_resultado(Or[2]))
    print(perceptron.y_resultado(Or[3]))
    print("_________________________________________________")

    #Reconhecimento do A e T.
    pesos = [random.uniform(0, 1) for _ in range(25)]

    perceptron = Perceptron(0.2,pesos)

    letras = [[ 1,1,1,1,1,1,
                1,0,0,0,1,
                1,1,1,1,1,
                1,0,0,0,1,
                1,0,0,0,1 ],
              
              [ 1,1,1,1,1,1,
                0,0,1,0,0,
                0,0,1,0,0,
                0,0,1,0,0,
                0,0,1,0,0 ]]
    yd = [0,1]
    perceptron.treinando(letras, yd)

    print("Resultado A:")
    print(perceptron.y_resultado(letras[0]))
    print("Variações de A:")
    print(perceptron.y_resultado([1,0,1,1,1,0,
                                    1,0,0,0,1,
                                    1,1,1,1,1,
                                    1,0,0,0,1,
                                    0,0,0,0,0]))
    print("Resultado T:")
    print(perceptron.y_resultado(letras[1]))
    print("Variações de T:")
    print(perceptron.y_resultado([1,0,1,1,1,0,
                                    0,0,1,0,0,
                                    0,0,1,0,0,
                                    0,0,0,0,0,
                                    0,0,0,0,0]))
    print("_________________________________________________")

    #Reconhecimento de A a Z.

    pesos = [random.uniform(0, 1) for _ in range(25)]
    perceptron_1 = Perceptron(0.8,pesos)
    pesos = [random.uniform(0, 1) for _ in range(25)]
    perceptron_2 = Perceptron(0.8,pesos)
    pesos = [random.uniform(0, 1) for _ in range(25)]
    perceptron_3 = Perceptron(0.8,pesos)
    pesos = [random.uniform(0, 1) for _ in range(25)]
    perceptron_4 = Perceptron(0.8,pesos)
    pesos = [random.uniform(0, 1) for _ in range(25)]
    perceptron_5 = Perceptron(0.8,pesos)

    alfabeto = [
              [
                1, 1, 1, 1, 1, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 1, 1, 1, 1,
                  1, 0, 0, 0, 1 
              ],
              [
                1, 1, 1, 1, 1, 0,
                  1, 0, 0, 0, 1,
                  1, 1, 1, 1, 0,
                  1, 0, 0, 0, 1,
                  1, 1, 1, 1, 0 
              ],
              [
                1, 0, 1, 1, 1, 1,
                  1, 0, 0, 0, 0,
                  1, 0, 0, 0, 0,
                  1, 0, 0, 0, 0,
                  0, 1, 1, 1, 1 
              ],
              [
                1, 1, 1, 1, 1, 0,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 1, 1, 1, 0 
              ],
              [
                1, 1, 1, 1, 1, 1,
                  1, 0, 0, 0, 0,
                  1, 1, 1, 1, 1,
                  1, 0, 0, 0, 0,
                  1, 1, 1, 1, 1 
              ],
              [
                1, 1, 1, 1, 1, 1,
                  1, 0, 0, 0, 0,
                  1, 1, 1, 1, 1,
                  1, 0, 0, 0, 0,
                  1, 0, 0, 0, 0 
              ],
              [
                1, 0, 1, 1, 1, 0,
                  1, 0, 0, 0, 0,
                  1, 0, 0, 1, 1,
                  1, 0, 0, 0, 1,
                  0, 1, 1, 1, 1 
              ],
              [
                1, 1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 1, 1, 1, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1 
              ],
              [
                1, 0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0, 
              ],
              [
                1, 0, 0, 1, 1, 1,
                  0, 0, 0, 0, 1,
                  0, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  0, 1, 1, 1, 0 
              ],
              [
                1, 1, 0, 0, 1, 0,
                  1, 0, 1, 0, 0,
                  1, 1, 0, 0, 0,
                  1, 0, 1, 0, 0,
                  1, 0, 0, 1, 0 
              ],
              [
                1, 1, 0, 0, 0, 0,
                  1, 0, 0, 0, 0,
                  1, 0, 0, 0, 0,
                  1, 0, 0, 0, 0,
                  1, 1, 1, 1, 1 
              ],
              [
                1, 1, 0, 0, 0, 1,
                  1, 1, 0, 1, 1,
                  1, 0, 1, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1 
              ],
              [
                1, 1, 0, 0, 0, 1,
                  1, 1, 0, 0, 1,
                  1, 0, 1, 0, 1,
                  1, 0, 0, 1, 1,
                  1, 0, 0, 0, 1 
              ],
              [
                1, 0, 1, 1, 1, 0,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  0, 1, 1, 1, 0 
              ],
              [
                1, 1, 1, 1, 1, 0,
                  1, 0, 0, 0, 1,
                  1, 1, 1, 1, 0,
                  1, 0, 0, 0, 0,
                  0, 0, 0, 0, 0 
              ],
              [
                1, 0, 1, 1, 1, 0,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 1, 0,
                  0, 1, 1, 0, 1
              ],
              [
                1, 1, 1, 1, 1, 0,
                  1, 0, 0, 0, 1,
                  1, 1, 1, 1, 0,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1
              ],
              [
                1, 0, 1, 1, 1, 1,
                  1, 0, 0, 0, 1,
                  0, 1, 1, 1, 0,
                  0, 0, 0, 0, 1,
                  1, 1, 1, 1, 0
              ],
              [
                1, 1, 1, 1, 1, 1,
                  0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0 
              ],
              [
                1, 1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  0, 1, 1, 1, 0 
              ],
              [
                1, 1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  0, 1, 0, 1, 0,
                  0, 1, 0, 1, 0,
                  0, 0, 1, 0, 0 
              ],
              [
                1, 1, 0, 0, 0, 1,
                  1, 0, 0, 0, 1,
                  1, 0, 1, 0, 1,
                  1, 1, 0, 1, 1,
                  1, 0, 0, 0, 1
              ],
              [
                1, 1, 0, 0, 0, 1,
                  0, 1, 0, 1, 0,
                  0, 0, 1, 0, 0,
                  0, 1, 0, 1, 0,
                  1, 0, 0, 0, 1
              ],
              [
                1, 1, 0, 0, 0, 1,
                  0, 1, 0, 1, 0,
                  0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0,
                  0, 0, 1, 0, 0 
              ],
              [
                1, 1, 1, 1, 1, 1,
                  0, 0, 0, 1, 0,
                  0, 0, 1, 0, 0,
                  0, 1, 0, 0, 0,
                  1, 1, 1, 1, 1
              ]
            ]

    yd_1 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]
    yd_2 = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,1,1]
    yd_3 = [0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0,0,0,1,1,1,1,0,0]
    yd_4 = [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1,0,0]
    yd_5 = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]

    perceptron_1.treinando(alfabeto,yd_1)
    perceptron_2.treinando(alfabeto,yd_2)
    perceptron_3.treinando(alfabeto,yd_3)
    perceptron_4.treinando(alfabeto,yd_4)
    perceptron_5.treinando(alfabeto,yd_5)

    print("Resultado da letra B:")
    print(perceptron_1.y_resultado(alfabeto[1]))
    print(perceptron_2.y_resultado(alfabeto[1]))
    print(perceptron_3.y_resultado(alfabeto[1]))
    print(perceptron_4.y_resultado(alfabeto[1]))
    print(perceptron_5.y_resultado(alfabeto[1]))

    print("Resultado da letra G:")
    print(perceptron_1.y_resultado(alfabeto[6]))
    print(perceptron_2.y_resultado(alfabeto[6]))
    print(perceptron_3.y_resultado(alfabeto[6]))
    print(perceptron_4.y_resultado(alfabeto[6]))
    print(perceptron_5.y_resultado(alfabeto[6]))

    print("Resultado da letra J:")
    print(perceptron_1.y_resultado(alfabeto[9]))
    print(perceptron_2.y_resultado(alfabeto[9]))
    print(perceptron_3.y_resultado(alfabeto[9]))
    print(perceptron_4.y_resultado(alfabeto[9]))
    print(perceptron_5.y_resultado(alfabeto[9]))

    print("Resultado da letra W:")
    print(perceptron_1.y_resultado(alfabeto[22]))
    print(perceptron_2.y_resultado(alfabeto[22]))
    print(perceptron_3.y_resultado(alfabeto[22]))
    print(perceptron_4.y_resultado(alfabeto[22]))
    print(perceptron_5.y_resultado(alfabeto[22]))
    print("_________________________________________________")

    #Portas XOR.
    perceptron_1 = Perceptron(0.2,[-0.6,0.7,0.2])

    Xor = [[1,0,0], [1,0,1], [1,1,0], [1,1,1]]
    yd = [0,1,1,1]
    perceptron_1.treinando(Xor, yd)

    print("Resultado Perceptron 1:")
    print(perceptron_1.y_resultado(Xor[0]))
    print(perceptron_1.y_resultado(Xor[1]))
    print(perceptron_1.y_resultado(Xor[2]))
    print(perceptron_1.y_resultado(Xor[3]))

    perceptron_2 = Perceptron(0.2,[-0.6,0.7,0.2])

    Xor = [[1,0,0], [1,0,1], [1,1,0], [1,1,1]]
    yd = [1,1,1,0]
    perceptron_2.treinando(Xor, yd)

    print("Resultado Perceptron 2:")
    print(perceptron_2.y_resultado(Xor[0]))
    print(perceptron_2.y_resultado(Xor[1]))
    print(perceptron_2.y_resultado(Xor[2]))
    print(perceptron_2.y_resultado(Xor[3]))

    perceptron_3 = Perceptron(0.2,[-0.6,0.7,0.2])

    Xor = [[1,0,0], [1,0,1], [1,1,0], [1,1,1]]
    yd = [0,0,0,1]
    perceptron_3.treinando(Xor, yd)

    print("Resultado Perceptron 3:")
    print(perceptron_3.y_resultado(Xor[0]))
    print(perceptron_3.y_resultado(Xor[1]))
    print(perceptron_3.y_resultado(Xor[2]))
    print(perceptron_3.y_resultado(Xor[3]))

    Xor = [[1,perceptron_1.y_resultado(Xor[0]), 1,perceptron_2.y_resultado(Xor[0])], 
           [1,perceptron_1.y_resultado(Xor[1]), 1,perceptron_2.y_resultado(Xor[1])],
           [1,perceptron_1.y_resultado(Xor[2]), 1,perceptron_2.y_resultado(Xor[2])],
           [1,perceptron_1.y_resultado(Xor[3]), 1,perceptron_2.y_resultado(Xor[3])]]

    print("Resultado Xor:")
    print(perceptron_3.y_resultado(Xor[0]))
    print(perceptron_3.y_resultado(Xor[1]))
    print(perceptron_3.y_resultado(Xor[2]))
    print(perceptron_3.y_resultado(Xor[3]))
    print("_________________________________________________")
    
if __name__ == "__main__":
    main()