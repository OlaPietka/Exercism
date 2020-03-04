class Garden:
    flowers = {'V': "Violets", 'C': "Clover", 'R': "Radishes", 'G': "Grass"}
    children = ["Alice", "Bob", "Charlie", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

    def __init__(self, diagram, students=None):
        diagram = diagram.replace("\n", "")
        l = len(diagram)//2

        self.garden = [diagram[i:i+2] + diagram[l+i:l+i+2] for i in range(0, l, 2)]
        self.students = self.children if students is None else sorted(students)

    def plants(self, name):
        return [self.flowers[p] for p in self.garden[self.students.index(name)]]