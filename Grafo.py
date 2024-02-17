import openpyxl
from geopy.distance import geodesic
import matplotlib.pyplot as plt
import networkx as nx

# Caminho para o arquivo Excel no repositório clonado
excel_file_path = "Pasta10.xlsx"

# Carregar o arquivo Excel usando openpyxl
workbook = openpyxl.load_workbook(excel_file_path)
sheet = workbook.active


class Grafo:
    def __init__(self):
        self.grafo = {}

    # Adiciona uma aresta ao grafo
    def adiciona_aresta(self, u, v, w):
        if u not in self.grafo:
            self.grafo[u] = []
        self.grafo[u].append((v, w))
        if v not in self.grafo:
            self.grafo[v] = []

    def imprime_caminho(self, pred, src, dest):
        caminho = []
        vertice = dest
        while vertice != src:
            caminho.append(vertice)
            vertice = pred[vertice]
        caminho.append(src)
        caminho.reverse()
        print("Caminho:", " -> ".join(caminho))

    # O algoritmo de Bellman-Ford
    def bellman_ford(self, src, dest):
        # Inicializa as distâncias do vértice inicial como infinito
        dist = {vertice: float("Inf") for vertice in self.grafo}
        pred = {vertice: None for vertice in self.grafo}
        dist[src] = 0

        # Relaxa todas as arestas |V| - 1 vezes
        for _ in range(len(self.grafo) - 1):
            for u in self.grafo:
                for v, w in self.grafo[u]:
                    if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
                        pred[v] = u

        print(f"O menor caminho entre {src} e {dest} é:")
        self.imprime_caminho(pred, src, dest)
        print(f"peso total: {dist[dest]:.2f} km")

    # Método para visualizar o grafo
    def visualizar_grafo(self, vertices, arestas):
        G = nx.DiGraph()

        for vertice in vertices:
            G.add_node(vertice)

        for aresta in arestas:
            G.add_edge(aresta[0], aresta[1])

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_size=650, node_color="yellow", font_size=5, font_weight="bold",
                width=1, edge_color="gray", arrows=True)

        plt.title("Grafo")
        plt.show()


# Exemplo de uso:
if __name__ == "__main__":
    g = Grafo()
    arestas = []

    for d in range(94):
        celula = sheet.cell(row=(d + 2), column=1)
        bairro1 = celula.value
        celula = sheet.cell(row=(d + 2), column=3)
        coordenadas1 = celula.value.split(", ")
        X1 = float(coordenadas1[0])
        Y1 = float(coordenadas1[1])
        coord_inicial = (X1, Y1)
        celula = sheet.cell(row=(d + 2), column=2)
        limitrofes = celula.value.split(", ")
        for limitrofe in limitrofes:
            linha = None
            for row in sheet.iter_rows(min_row=1, max_row=sheet.max_row, min_col=1, max_col=1):
                for cell in row:
                    if cell.value == limitrofe:
                        linha = cell.row
                        break
            celula = sheet.cell(row=linha, column=3)
            coordenadas2 = celula.value.split(", ")
            X2 = float(coordenadas2[0])
            Y2 = float(coordenadas2[1])
            coord_final = (X2, Y2)
            peso = geodesic(coord_inicial, coord_final).kilometers
            arestas.append((bairro1, limitrofe, peso))
            g.adiciona_aresta(bairro1, limitrofe, peso)

    src = 'Brasília Teimosa'  # Vértice inicial
    dest = 'Pina'  # Vértice final

    g.bellman_ford(src, dest)

    # Visualizar o grafo
    g.visualizar_grafo(list(g.grafo.keys()), arestas)