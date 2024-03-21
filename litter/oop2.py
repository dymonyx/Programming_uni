class Graph:

    LIMIT_Y = [0, 10]

    def set_data(self, spisok):
        self.data = spisok

    def draw(self):
        self.data_new = []
        for numb in self.data:
            if self.LIMIT_Y[0] <= numb <= self.LIMIT_Y[1]:
                self.data_new.append(numb)
        print(*self.data_new)


graph1 = Graph()
graph1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph1.draw()


