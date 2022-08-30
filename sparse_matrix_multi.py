"""
Matrix are given like (x, y, w) where x is row number, y in col number and w is value at that position.
Return multiplied value only if value is nonzero, first sort in order of x then in order of y
"""


class SparseMatrix:
    def __init__(self, n_rows, n_cols, matrix):
        self.nr = n_rows
        self.nc = n_cols
        self.matrix = self.to_sparse(matrix)

    @staticmethod
    def to_sparse(matrix):
        sp_matrix = {}
        for x, y, w in matrix:
            sp_matrix[(x, y)] = w
        return sp_matrix

    @staticmethod
    def from_sparse(matrix):
        final_ans = []
        order_map = {}
        max_n_row = 0
        for r, c in matrix:
            if not matrix[(r, c)]:
                continue
            if r not in order_map:
                order_map[r] = [r, c, matrix[(r, c)]]
                max_n_row += 1
            else:
                order_map[r].append([r, c, matrix[(r, c)]])
        for i in range(max_n_row):
            row_vals = order_map[i]
            row_vals.sort(key=lambda x: x[2])
            final_ans.append(sorted(row_vals))
        return final_ans

    def mat_mul(self, sp_matrix):
        mat1 = self.matrix
        mat2 = sp_matrix.matrix
        ans_mat = {}
        for (mat1_r, mat1_c), mat1_val in mat1.items():
            for mat2_c in range(sp_matrix.nc):
                if (mat1_c, mat2_c) in mat2_c:
                    mat2_val = mat2[(mat1_c, mat2_c)]
                    ans_mat[(mat1_c, mat2_c)] = ans_mat.get((mat1_c, mat2_c), 0) + mat1_val * mat2_val
        return self.from_sparse(ans_mat)

