import json
from order.menuitem import MenuItem
from collections import namedtuple
import uuid

class Order:
    """Representation of a restaurant order."""

    # Tener un json file para almecenar cada orden.
    ORDERS_FILE = "orders_db.json"

    def __init__(self) -> None:
        self.order_id = str(uuid.uuid4()) # ID único de la orden
        self.menu_items = []

    def add_item(self, item: "MenuItem") -> None:
        """Add items to the list."""
        self.menu_items.append(item)
        self.save_order()
    
    def delete_item(self, item: "MenuItem") -> bool:
        """Deletes an item from the list."""
        if item in self.menu_items:
            self.menu_items.remove(item)
            self.save_order()
            return True
        return False

    def update_item(self, item: str, new: str) -> bool:
        """Updates an item from the list."""
        if item not in self.menu_items:
            return False
        index = self.menu_items.index(item)
        self.menu_items[index] = new
        self.save_order()
        return True

    def show(self) -> list[str]:
        """
        Returns a readable list of items.

        Converts each item in the order to a string.
        """
        return [str(item) for item in self.menu_items]

    def to_dict(self) -> dict:
        """Returns a dict with the features of each MenuItem."""
        return {
            "order_id": self.order_id,
            "items": [{"name": item.name, "price": item.price, "quantity": item.quantity} for item in self.menu_items]
        }

    def save_order(self) -> None:
        try:
            with open(self.ORDERS_FILE, "r") as file:
                orders_data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            orders_data = []
        
        # Buscar si la orden ya existe en el archivo
        for i, order in enumerate(orders_data):
            if order["order_id"] == self.order_id:
                orders_data[i] = self.to_dict()
                break
        else:
            orders_data.append(self.to_dict())
        
        with open(self.ORDERS_FILE, "w") as file:
            json.dump(orders_data, file, indent=4)
    
    def calculate_total_price(self) -> float:
        """
        Calculates the total cost of the order.

        Returns the sum of the total price of all items.
        Also applies potential discounts based on the
        order composition.
        """
        bill: float = 0
        beverage_discount: bool = False
        dessert_discount: bool = False
        for item in self.menu_items:
            if "MainCourse" == repr(item):
                beverage_discount, dessert_discount = True, True
                # Aplicar el descuento
            if "Beverage" == repr(item) and beverage_discount:
                item.change_price(0.2)
                beverage_discount = False
            if "Dessert" == repr(item) and dessert_discount:
                item.change_price(0.4)
                dessert_discount = False
            bill += item.get_total_price()

        return round(bill, 2)

    def apply_discount(self, discount: float) -> float:
        """
        Applies a discount to the total order cost.

        Args:
            discount: The discount percentage as a decimal (e.g., 0.1 for 10%).

        Returns:
            The total cost after applying the discount.
        """
        total = self.calculate_total_price()
        if discount <= 1:
            new_total = total * (1-discount)
        elif discount > 1:
            new_total = total * discount
        return round(new_total, 2)

if __name__ == '__main__':
    order = Order()
    menu_data2 = {
        ("Caldo", 20_000, 2),
        ("Cerveza", 5_000, 20),
        ("Cocacola", 2_000, 14),
    }
    for (menuitem, price, quantity) in menu_data2:
        item = MenuItem(menuitem, price, quantity)
        order.add_item(item)
    print(order.show())
    print(f"Total de la cuenta: {order.calculate_total_price()}")
    print(f"Identificador orden: {order.order_id}")
    print(order.to_dict())
    order.update_item(MenuItem("Limonada", 5_000, 3), MenuItem("Limonada", 5000, 4))

    print(order.menu_items)
    order.delete_item("Caldo")



