class MCP:
    
    def __init__(self, w, limiar):
        self.lim = limiar
        self.w = w

    def soma(self, x):
        soma = 0
        
        for i in range(len(x)):
            print(x[i])
            soma += x[i] * self.w[i]

        return soma

    def y_resultado(self, x):
        if(self.soma(x) >= self.lim):
            return 1
        else:
            return 0


def main():

    mcp = MCP([0.5,0.5], 0.5)
    
    print("Y: ", mcp.y_resultado([0,0]))
    print("Y: ", mcp.y_resultado([0,1]))
    print("Y: ", mcp.y_resultado([1,0]))
    print("Y: ", mcp.y_resultado([1,1]))

if __name__ == "__main__":
    main()
