from random import random, randint

class Matrix:
    def __init__(self, rows_=1, cols=1, data=None):
        self.rows_ = rows_
        self.cols = cols
        self.data = data
        if self.data is None:
            self.data = [[0 for j in range(cols)] for i in range(rows_)]
    
    def __repr__(self):
        data_string = str(self.data)
        for i, char in enumerate(data_string):
            if data_string[i:i+2] == "],":
                data_string = data_string[:i+2] + "\n" + data_string[i+2:]                
        return data_string + "\n"
    
    def randomize(self, a=0, b=9, is_float=False):
        for i in range(self.rows_):
            for j in range(self.cols):
                if is_float:
                    self.data[i][j] = random(a, b)
                else:
                    self.data[i][j] = randint(a, b)
                    
    def _match_dimensions(self, other, limited=False, name=""):
        if limited:
            if not self.cols == other.rows_:
                raise ValueError("The column dimension of this matrix does not match the row dimension of the other matrix. " + name)
        elif not (self.rows_ == other.rows_ and self.cols == other.cols):
            raise ValueError("The dimensions of these matricies do not match. " + name)
        return
    def copy_(self):
        return Matrix(self.rows_, self.cols, self.data)
    
    def add_(self, other, persist=False):
        result = self.copy_()
        if isinstance(other, Matrix):
            result._match_dimensions(other, name="(Addition)")
            for i in range(result.rows_):
                for j in range(result.cols):
                    result.data[i][j] += other.data[i][j]
        else:
            # Assume scalar
            for i in range(result.rows_):
                for j in range(result.cols):
                    result.data[i][j] += other
        return result
    def sub_(self, other):
        result = self.copy_()
        if isinstance(other, Matrix):
            result._match_dimensions(other, name="(Subtraction)")
            for i in range(result.rows_):
                for j in range(result.cols):
                    result.data[i][j] -= other.data[i][j]
        else:
            # Assume scalar
            for i in range(result.rows_):
                for j in range(result.cols):
                    result.data[i][j] -= other
        return result
    
    def mult_(self, other):
        result = self.copy_()
        if isinstance(other, Matrix):
            result._match_dimensions(other, name="(Element-wise Multiplication)")
            for i in range(result.rows_):
                for j in range(result.cols):
                    result.data[i][j] *= other.data[i][j]
        else:
            # Assume scalar
            for i in range(result.rows_):
                for j in range(result.cols):
                    result.data[i][j] *= other
        return result
    
    def dot_(self, other):
        if not isinstance(other, Matrix):
            return self.mult_(other)
        self._match_dimensions(other, limited=True, name="(Dot Multiplication)")
        dot_product = Matrix(self.rows_, other.cols)
        for i in range(dot_product.rows_):
            for j in range(dot_product.cols):
                sum = 0
                for k in range(self.cols):
                    value = self.data[i][k] * other.data[k][j]
                    sum += value
                dot_product.data[i][j] = sum
        return dot_product


test_mat = Matrix(2, 3)

scalar = randint(1, 10)
same_dim_mat = Matrix(5, 6)
same_dim_dot_mat = Matrix(3, 2)
diff_dim_mat = Matrix(4, 4)

test_mat.randomize()
same_dim_mat.randomize()
same_dim_dot_mat.randomize()
diff_dim_mat.randomize()

print test_mat
print same_dim_dot_mat
# Add
# test_mat.add_(scalar)
# test_mat.add_(same_dim_mat)
# test_mat.add_(diff_dim_mat)

# Sub
# test_mat.sub_(scalar)
# test_mat.sub_(same_dim_mat)
# test_mat.sub_(diff_dim_mat)

# Mult
# test_mat.mult_(scalar)
# test_mat.mult_(same_dim_mat)
# test_mat.mult_(diff_dim_mat)

# Dot
# test_mat.dot_(scalar)
# test_mat.dot_(same_dim_mat)
test_mat.dot_(same_dim_dot_mat)
# test_mat.dot_(diff_dim_mat)

print test_mat
