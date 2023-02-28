import networkx as nx
import matplotlib.pyplot as plt 

class Vertice:
    def __init__(self, id):
        self.id = id
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')

    def agregar_vecino(self, v, p):
        if v not in self.vecinos:
            self.vecinos.append([v,p])

class Grafica:
    def __init__(self):
        self.G = nx.Graph()
        self.vertices = {}

    def mostrar_grafica(self):
        pos = nx.layout.spring_layout(self.G)
        nx.draw_networkx(self.G, pos)
        labels = nx.get_edge_attributes(self.G, "weigth")
        nx.draw_networkx_edge_labels(self.G, pos, edge_labels=labels)
        plt.show()

    def agregar_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregar_arista(self, vertice_a, vertice_b, peso):
        if vertice_a in self.vertices and vertice_b in self.vertices:
            self.vertices[vertice_a].agregar_vecino(vertice_b, peso)
            self.vertices[vertice_b].agregar_vecino(vertice_a, peso)

            self.G.add_edge(vertice_a, vertice_b, weigth=peso)

    def obtener_camino(self, vertice_b):
        camino = []
        actual = vertice_b
        while (actual != None):
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[vertice_b].distancia]
    
    def minimo(self, lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]

            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
                return v

    def dijkstra(self, vertice_a):
        if vertice_a in self.vertices:
            self.vertices[vertice_a].distancia = 0
            actual = vertice_a
            no_visitados = []

            for v in self.vertices:
                if v != vertice_a:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None
                no_visitados.append(v)


            while (len(no_visitados) > 0):
                for vecino in self.vertices[actual].vecinos:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                no_visitados.remove(actual)

                actual = self.minimo(no_visitados)

        else:
            return False
        
if __name__ == '__main__':
    gr = Grafica()
    gr.agregar_vertice('a')
    gr.agregar_vertice('b')
    gr.agregar_vertice('c')

    gr.agregar_arista('a', 'b', 8)
    gr.agregar_arista('a', 'c', 4)
    gr.agregar_arista('b', 'c', 6)

    print('La ruta mas rapida por Disjktra es:')
    gr.dijkstra('a')
    print(gr.obtener_camino('b'))

    gr.mostrar_grafica()
