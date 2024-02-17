import openpyxl
from geopy.distance import geodesic

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

        print("Pesos das arestas:")
        for i in range(len(caminho) - 1):
            u = caminho[i]
            v = caminho[i + 1]
            for neighbor, weight in self.grafo[u]:
                if neighbor == v:
                    print(f" {u} -> {v}: {weight:.2f} km")
                    break

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


# Exemplo de uso:
if __name__ == "__main__":
    g = Grafo()
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
            g.adiciona_aresta(bairro1, limitrofe, peso)

    src = 'Espinheiro'  # Vértice inicial
    dest = 'Recife'  # Vértice final

    g.bellman_ford(src, dest)