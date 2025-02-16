from typing import List

class Tree:
    """Базовый класс для деревьев."""

    def __init__(self, height: float, age: int, type_of_tree: str) -> None:
        """Инициализирует объект Tree.

        Args:
            height: Высота дерева.
            age: Возраст дерева.
            type_of_tree: Тип дерева (лиственное или хвойное).
        """
        self.height = height
        self.age = age
        self.type_of_tree = type_of_tree
        self._root_system_size = self.height / 2 # Инкапсулированный атрибут, примерное соотношение

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"{self.type_of_tree} tree, height: {self.height}m, age: {self.age} years"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта, которое можно использовать для его воссоздания."""
        return f"Tree(height={self.height}, age={self.age}, type_of_tree='{self.type_of_tree}')"

    def grow(self, years: int) -> None:
        """Увеличивает возраст и высоту дерева.

        Args:
            years: Количество лет, на которое дерево вырастет.
        """
        self.age += years
        self.height += 0.5 * years # Пример: дерево вырастает на 0.5 метра каждый год

    def _calculate_root_size(self): # Инкапсулированный метод, т.к. расчет размера корневой системы - внутренняя деталь реализации.
        """Вычисляет размер корневой системы."""
        # В реальном примере здесь могут быть сложные вычисления, зависящие от разных факторов.
        return self.height / 2

class ConiferTree(Tree):
    """Дочерний класс для хвойных деревьев, наследующий от Tree."""

    def __init__(self, height: float, age: int, needle_type: str) -> None:
        """Инициализирует объект ConiferTree.

        Args:
            height: Высота дерева.
            age: Возраст дерева.
            needle_type: Тип хвои.
        """
        super().__init__(height, age, "Conifer") # type_of_tree - хвойное
        self.needle_type = needle_type

    def __str__(self) -> str:
        """Возвращает строковое представление объекта."""
        return f"Conifer tree ({self.needle_type}), height: {self.height}m, age: {self.age} years"

    def __repr__(self) -> str:
        """Возвращает строковое представление объекта, которое можно использовать для его воссоздания."""
        return f"ConiferTree(height={self.height}, age={self.age}, needle_type='{self.needle_type}')"

    def grow(self, years: int, growth_rate: float = 0.3) -> None:
        """Перегруженный метод. Увеличивает возраст и высоту дерева, учитывая скорость роста хвойных деревьев.

        Args:
            years: Количество лет, на которое дерево вырастет.
            growth_rate: Скорость роста дерева.
        """

        self.age += years
        self.height += growth_rate * years # Хвойные могут расти медленнее

    def get_needle_info(self) -> str:
        """Возвращает информацию о типе хвои."""
        return f"Needle type: {self.needle_type}"

if __name__ == "__main__":
    pine = ConiferTree(5.0, 10, "long")
    print(pine)
    pine.grow(5)
    print(pine)
    print(repr(pine))
    print(pine.get_needle_info())
    # print(pine._calculate_root_size()) # Ошибка - инкапсулированный метод