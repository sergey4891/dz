
class Matrix:
    def __init__(self, data):
        self.data = data
        self.n = len(data)
        self.m = len(data[0])
    def __add__(self, other):
        if self.m == other.m and self.n == other.n:
            data1 = []
            for i in range(self.n):
                curr_data =[]
                for j in range(self.m):
                    curr_data.append(self.data[i][j] + other.data[i][j])
                data1.append(curr_data)
            return Matrix(data1)
        else:
            return "размер не правельный"

m1 = Matrix([[1,2], [1,2]])
m2 = Matrix([[1,0], [0,1]])
m3 = m1 + m2

print(m3.data)