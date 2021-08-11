class DivisionByNull:
    def __init__(self, divisible, divisor):
        self.divisible = divisible
        self.divisor = divisor

    @staticmethod
    def divide_by_null(divisible, divisor):
        try:
            return (divisible / divisor)
        except:
            return (f"Делить на ноль нельзя!")


div = DivisionByNull(5, 10)
print(div.divide_by_null(5, 10))
print(div.divide_by_null(5, 0))
print(div.divide_by_null(0, 5))