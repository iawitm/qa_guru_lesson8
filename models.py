class Product:
    name: str
    price: float
    description: str
    quantity: int

    def __init__(self, name, price, description, quantity):
        self.name = name
        self.price = price
        self.description = description
        self.quantity = quantity

    def __hash__(self):
        return hash(self.name + self.description)

    def __eq__(self, other):
        if not isinstance(other, Product):
            return False
        return (self.name, self.description) == (other.name, other.description)

    def __repr__(self):
        return f'{self.name} {self.price} {self.description} {self.quantity}'

    def check_quantity(self, quantity) -> bool:

        if quantity < 0:
            raise ValueError('Quantity can not be negative')

        return self.quantity >= quantity

    def buy(self, quantity):

        if  self.check_quantity(quantity):
            self.quantity -= quantity
        else:
            raise ValueError('Not enough quantity')

class Cart:
    products: dict[Product, int]

    def __init__(self, products):
        # По-умолчанию корзина пустая
        self.products = products

    def add_product(self, product: Product, buy_count=1):
        if buy_count <= 0:
            raise ValueError('Count must be greater than 0')

        if self.products.get(product) is not None:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count


    def remove_product(self, product: Product, remove_count=None):
        if product not in self.products:
            raise ValueError('Can not find product in the cart')

        if remove_count is not None and remove_count <= 0:
            raise ValueError('Count must be greater than 0')

            # Условие >=, тк при удалении всех товаров позиция тоже должна удаляться
        if remove_count is None or remove_count >= self.products[product]:
            self.products.pop(product)
        else:
            self.products[product] -= remove_count

    def clear(self):
        self.products.clear()

    def get_total_price(self) -> float:
        return round(sum(product.price * count for product, count in self.products.items()), 2)

    def buy(self):
        if not self.products:
            raise ValueError('Cart is empty')

        for product in self.products:
           if not product.check_quantity(self.products[product]):
               raise ValueError('Not enough quantity in the stock')

        for product in self.products:
            product.buy(self.products[product])

        self.products.clear()
