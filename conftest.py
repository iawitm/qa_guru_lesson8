import csv

import pytest

from models import Product, Cart


@pytest.fixture
def default_product():
    return Product("Default Product", 100, "This is a default product", 1000)

@pytest.fixture
def product_from_csv():
    with open('./resources/products.csv') as csvfile:
        products = list(csv.DictReader(csvfile, delimiter=","))

    return [
        Product(name=product["name"],
                price=float(product["price"]),
                description=product["description"],
                quantity=int(product["quantity"]))
        for product in products]

@pytest.fixture
def default_cart(product_from_csv):
    default_cart_dict = {}
    for product in product_from_csv:
        default_cart_dict[product] = product.quantity - 1

    default_cart = Cart(default_cart_dict)
    return default_cart

@pytest.fixture
def default_cart_out_of_stock(product_from_csv):
    default_cart_out_of_stock_dict = {}
    for product in product_from_csv:
        default_cart_out_of_stock_dict[product] = product.quantity + 1

    default_cart = Cart(default_cart_out_of_stock_dict)
    return default_cart

@pytest.fixture
def default_empty_cart():
    default_empty_cart = Cart({})
    return default_empty_cart

@pytest.fixture
def changed_existing_product(default_cart):
    changed_existing_product = next(
        product for product in default_cart.products.keys()
        if product.name == "Marker" and product.description == "Pink")

    return changed_existing_product

@pytest.fixture
def unchanged_existing_product(default_cart):
    unchanged_existing_product = next(
        product for product in default_cart.products.keys()
        if product.name == "Marker" and product.description == "Blue")

    return unchanged_existing_product