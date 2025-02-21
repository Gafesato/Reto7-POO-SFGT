from order.order import Order
from order.menuitem import Appetizer, Beverage, Dessert, MainCourse
from order.restaurant import Restaurant

def main():
    # Crear instancia de restaurante donde se guardan las ordenes
    restaurant = Restaurant(4) # Máximo 4 ordenes
    order1 = Order()
    order2 = Order()
    order3 = Order()
    order4 = Order()

    # Orden Principal
    mc1 = MainCourse(name="Steak", price=15.00, quantity=1)
    mc2 = MainCourse(name="Vegetarian Pasta", price=12.00, quantity=2)
    ap1 = Appetizer(name="Nachos", price=5.50, quantity=2)
    ap2 = Appetizer(name="Garlic Bread", price=3.50, quantity=1)
    ap3 = Appetizer(name="Spring Rolls", price=4.00, quantity=3)
    bv1 = Beverage(name="Coca Cola", price=2.50, quantity=2)
    bv2 = Beverage(name="Orange Juice", price=3.00, quantity=1)
    bv3 = Beverage(name="Latte", price=4.00, quantity=1)
    ds1 = Dessert(name="Cheesecake", price=6.00, quantity=1)
    ds2 = Dessert(name="Chocolate Cake", price=5.50, quantity=1)

    order_list = [mc1, mc2, ap1, ap2, ap3, bv1, bv2, bv3, ds1, ds2]
    for i in range(len(order_list)):
        order1.add_item(order_list[i])
        order2.add_item(order_list[i])
        order3.add_item(order_list[i])
        order4.add_item(order_list[i])

    # Mostrar los elementos en la orden
    print("Items en la orden:")
    print(order1.show())
    for item in order1.show():
        print(f" -> {item}")
    print('*'*25)
    print(restaurant)

if __name__ == '__main__':
    main()