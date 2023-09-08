class Point:
    def __init__(self, *vector: tuple[float, float]):
        self.vectors: list[tuple] = list(vector)
