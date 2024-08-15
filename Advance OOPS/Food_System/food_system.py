from typing import List, Dict
from uuid import uuid4
from customer import Customer
from restaurant import Restaurant
from order import Order, OrderStatus
from delivary_agent import DeliveryAgent 
from orderitem import OrderItem
from menu_item import MenuItem

class FoodDeliveryService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.customers = {}
            cls._instance.restaurants = {}
            cls._instance.orders = {}
            cls._instance.delivery_agents = {}
        return cls._instance

    @staticmethod
    def get_instance():
        if FoodDeliveryService._instance is None:
            FoodDeliveryService()
        return FoodDeliveryService._instance

    def register_customer(self, customer: Customer):
        self.customers[customer.id] = customer

    def register_restaurant(self, restaurant: Restaurant):
        self.restaurants[restaurant.id] = restaurant

    def register_delivery_agent(self, agent: DeliveryAgent):
        self.delivery_agents[agent.id] = agent

    def get_available_restaurants(self) -> List[Restaurant]:
        return list(self.restaurants.values())

    def get_restaurant_menu(self, restaurant_id: str) -> List[MenuItem]:
        restaurant = self.restaurants.get(restaurant_id)
        if restaurant:
            return restaurant.menu
        return []

    def place_order(self, customer_id: str, restaurant_id: str, items: List[MenuItem]) -> Order:
        customer = self.customers.get(customer_id)
        restaurant = self.restaurants.get(restaurant_id)
        if customer and restaurant:
            order = Order(self.generate_order_id(), customer, restaurant)
            for item in items:
                order.add_item(item)
            self.orders[order.id] = order
            self.notify_restaurant(order)
            return order
        return None

    def update_order_status(self, order_id: str, status: OrderStatus):
        order = self.orders.get(order_id)
        if order:
            order.set_status(status)
            self.notify_customer(order)
            if status == OrderStatus.CONFIRMED:
                self.assign_delivery_agent(order)

    def cancel_order(self, order_id: str):
        order = self.orders.get(order_id)
        if order and order.status == OrderStatus.PENDING:
            order.set_status(OrderStatus.CANCELLED)
            self.notify_customer(order)
            self.notify_restaurant(order)


    def assign_delivery_agent(self, order: Order):
        for agent in self.delivery_agents.values():
            if agent.available:
                agent.available = False
                order.assign_delivery_agent(agent)
                self.notify_delivery_agent(order)
                break



    def generate_order_id(self) -> str:
        return "ORD" + uuid4().hex[:8].upper()
    
    def notify_customer(self, order: Order):
    # Send notification to the customer about the order status update
        pass

    def notify_restaurant(self, order: Order):
        # Send notification to the restaurant about the new order or order status update
        pass
    

    def notify_delivery_agent(self, order: Order):
        # Send notification to the delivery agent about the assigned order
        pass

    
    
    
service = FoodDeliveryService.get_instance()


customer1 = Customer("C001", "Alice Johnson", "alice@example.com", "555-1234")
customer2 = Customer("C002", "Bob Smith", "bob@example.com", "555-5678")
service.register_customer(customer1)
service.register_customer(customer2)


menu1 = [
    MenuItem("M001", "Pizza", "Cheese Pizza", 10.0),
    MenuItem("M002", "Burger", "Beef Burger", 8.0),
]
menu2 = [
    MenuItem("M003", "Sushi", "Salmon Sushi", 12.0),
    MenuItem("M004", "Ramen", "Tonkotsu Ramen", 15.0),
]

restaurant1 = Restaurant("R001", "Pizza Place", "123 Main St", menu1)
restaurant2 = Restaurant("R002", "Sushi House", "456 Oak St", menu2)
service.register_restaurant(restaurant1)
service.register_restaurant(restaurant2)


agent1 = DeliveryAgent("D001", "Charlie Brown", "555-8765")
agent2 = DeliveryAgent("D002", "Daisy Duck", "555-4321")
service.register_delivery_agent(agent1)
service.register_delivery_agent(agent2)


items = [OrderItem(menu1[0], 2), OrderItem(menu1[1], 1)]
order = service.place_order(customer1.id, restaurant1.id, items)
if order:
    print(f"Order placed: {order.id}")
    

service.update_order_status(order.id, OrderStatus.CONFIRMED)
print(f"Order status updated to {OrderStatus.CONFIRMED}")


print(f"Order details: {order.id}, status: {order.status},\nItems: {[(item.item.name, item.quantity) for item in order._items]}")


available_restaurants = service.get_available_restaurants()
print("Available restaurants:")
for restaurant in available_restaurants:
    print(f"- {restaurant.name}")
    
# Cancel an order
service.cancel_order(order.id)
print(f"Order cancelled: {order.id}")