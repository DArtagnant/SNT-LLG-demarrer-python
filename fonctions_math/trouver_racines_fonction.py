

class Function2degree:
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c
    
    def __str__(self):
        return f"Function2degree({self._a}x² + {self._b}x + {self._c})"
    
    def discriminant(self) -> float:
        return (self._b ** 2) - 4 * self._a * self._c
    
    def has_two_solutions(self) -> bool:
        return self.discriminant() > 0
    
    def has_one_solution(self) -> bool:
        return self.discriminant() == 0
    
    def solution_pos(self) -> float:
        return (-self._b + (self.discriminant() ** 0.5)) / (2 * self._a)
    
    def solution_neg(self) -> float:
        return (-self._b - (self.discriminant() ** 0.5)) / (2 * self._a)
    
    def solution_0(self) -> float:
        return (-self._b) / 2 * self._a 

    def solutions(self):
        if self.has_two_solutions():
            return (self.solution_pos(), self.solution_neg())
        elif self.has_one_solution():
            return self.solution_0()
        else:
            return None

    def print_all(self):
        print("discriminant", self.discriminant())
        print("has solution in R", self.has_two_solutions())
        print("has only one solution", self.has_one_solution())
        print("solution positive", self.solution_pos())
        print("solution negative", self.solution_neg())
        print("solution 0", self.solution_0())

if __name__ == "__main__":
    f = Function2degree(0, 0, 0)
    print(f)
    print("solution :", f.solutions())