class Matrix:
# a column major order matrix class

    def __init__(self, *columns):
        for rest_columns in v[1:]:
            assert len(columns[0]) == len(rest_vector)
        self.columns = columns

    def __matmul__(self, other):
        if isinstance(other, list) or isinstance(other, tuple):
            answer = [0] * len(self.vectors[0])
        elif isinstance(other, Matrix):

    def column_mul(self, vector):
        result = [0] * len(self.vectors[0])
        for column in self.vector:
            for scalar in vector:
                for

    def transpose(self):
        return Matrix(*list(zip(self.vectors)))
