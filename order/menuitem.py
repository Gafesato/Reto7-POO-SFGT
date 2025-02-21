class MenuItem:
    """Representation of a menu item."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        self.name = name
        self.price = price
        if self.price < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.quantity = quantity
        if self.quantity <= 0:
            raise ValueError("La cantidad debe ser un número positivo.")

    def get_total_price(self) -> float:
        """Calculates and returns the total price of this item."""
        return self.price * self.quantity

    def change_price(self, fee: float) -> None:
        """
        Adjusts the price of an item.

        Args:
            fee: A multiplier factor to adjust the price.
        """
        self.price *= fee

    def __str__(self) -> str:
        """Returns the name of the MenuItem as a string."""
        return self.name


class Appetizer(MenuItem):
    """Representation of an appetizer."""

    def __init__(
        self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__for_sharing = None

    def get_for_sharing(self) -> object:
        return self.__for_sharing

    def set_for_sharing(self, for_sharing: bool) -> None:
        if type(for_sharing) == bool:
            self.__for_sharing = for_sharing
            if for_sharing:
                self.change_price(0.95)
        else:
            print("La entrada solo puede ser o no ser para compartir.")

    def __repr__(self) -> str:
        """Creates the unique name of the Class."""
        return "Appetizer"


class MainCourse(MenuItem):
    """Representation of a main course."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__is_meet = None

    def get_is_meet(self) -> object:
        return self.__is_meet

    def set_is_meet(self, is_meet: bool) -> None:
        if type(is_meet) == bool:
            self.__is_meet = is_meet
            if is_meet:
                self.change_price(1.05)
        else:
            print("El plato principal solo puede tener o no tener carne.")

    def __repr__(self) -> str:
        """Creates the unique name of the Class."""
        return "MainCourse"


class Beverage(MenuItem):
    """Representation of a beverage."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__size = None
        self.__has_sugar = None

    def get_size(self) -> object:
        return self.__size

    def set_size(self, size: int) -> None:
        if size > 0:
            self.__size = size
        else:
            print("El tamaño debe ser positivo.")

    def get_has_sugar(self) -> object:
        return self.__has_sugar

    def set_has_sugar(self, has_sugar: bool) -> None:
        if type(has_sugar) == bool:
            self.__has_sugar = has_sugar
            if has_sugar:
                self.change_price(1.05)
        else:
            print("La bebida solo puede tener o no tener azúcar.")

    def __repr__(self) -> str:
        """Creates the unique name of the Class."""
        return "Beverage"


class Dessert(MenuItem):
    """Representation of a dessert."""

    def __init__(self, name: str, price: float, quantity: int) -> None:
        super().__init__(name, price, quantity)
        self.__on_season = None

    def get_on_season(self) -> object:
        return self.__on_season

    def set_on_season(self, on_season: bool) -> None:
        if type(on_season) == bool:
            self.__on_season = on_season
            if on_season:
                self.change_price(0.95)
        else:
            print("El postre solo puede ser o no ser de temporada.")

    def __repr__(self) -> str:
        """Creates the unique name of the Class."""
        return "Dessert"