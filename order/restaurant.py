from queue import Queue
from order.order import Order


class Restaurant:
    """Representation of a restaurant with multiple orders."""

    def __init__(self, maxsize: int) -> None:
        self.maxsize = maxsize
        self.order_list = Queue(maxsize=self.maxsize)

    def add_order(self, order: "Order") -> str:
        """Add an order to the queue."""
        if self._check_order_disponibility():
            self.order_list.put(order)
            return f"Orden {order} agregada con éxito."
        else:
            return f"Sin espacio. Resuelva las órdenes pendientes primero."

    def _check_order_disponibility(self) -> bool:
        """Checks if an order can be processed."""
        if not self.order_list.full():
            return True
        else:
            return False
        
    def __str__(self) -> str:
        return f"Ordenes: {self.order_list}."
