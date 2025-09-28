class TestProductsPositive:

    def test_product_check_quantity_true_enough_stock(self, default_product):
        assert default_product.check_quantity(default_product.quantity-1) is True

    def test_product_check_quantity_true_equals_stock(self, default_product):
        assert default_product.check_quantity(default_product.quantity) is True

    def test_product_check_quantity_not_enough_stock(self, default_product):
        assert default_product.check_quantity(default_product.quantity + 1) is False

    def test_product_buy_enough_quantity(self, default_product):
        default_product.buy(default_product.quantity-1)

        assert default_product.quantity == 1

    def test_product_buy_equals_quantity(self, default_product):
        default_product.buy(default_product.quantity)

        assert default_product.quantity == 0


class TestCartPositive:

    def test_add_product_new_product(self, default_cart, default_product):
        default_cart.add_product(default_product, 1)

        assert default_cart.products[default_product] == 1
        assert len(default_cart.products) == 11

    # Проверка, что существующий продукт увеличивается в количестве
    # При этом продукт с другим описанием не меняется
    def test_add_product_existing_product(self, default_cart, changed_existing_product, unchanged_existing_product):
        changed_existing_product_cart_value = default_cart.products[changed_existing_product]
        unchanged_existing_product_cart_value = default_cart.products[unchanged_existing_product]

        default_cart.add_product(changed_existing_product, 1)

        assert default_cart.products[changed_existing_product] == changed_existing_product_cart_value+1
        assert default_cart.products[unchanged_existing_product] == unchanged_existing_product_cart_value

    # Проверка, что существующий продукт удаляется, если передать remove_count = None
    # При этом продукт с другим описанием не меняется
    def test_remove_product_none_remove_count(self, default_cart, changed_existing_product, unchanged_existing_product):

        default_cart.remove_product(changed_existing_product, None)

        assert changed_existing_product not in default_cart.products
        assert unchanged_existing_product in default_cart.products
        assert len(default_cart.products) == 9


    # Проверка, что существующий продукт удаляется, если передать remove_count = все количество продукта
    # При этом продукт с другим описанием не меняется
    def test_remove_product_equals_remove_count(self, default_cart, changed_existing_product, unchanged_existing_product):
        remove_count = default_cart.products[changed_existing_product]

        default_cart.remove_product(changed_existing_product, remove_count)

        assert changed_existing_product not in default_cart.products
        assert unchanged_existing_product in default_cart.products
        assert len(default_cart.products) == 9

    def test_remove_product_without_delete(self, default_cart, changed_existing_product):
        remove_count = default_cart.products[changed_existing_product] - 1

        default_cart.remove_product(changed_existing_product, remove_count)

        assert changed_existing_product in default_cart.products
        assert default_cart.products[changed_existing_product] == 1
        assert len(default_cart.products) == 10

    def test_clear(self, default_cart):
        default_cart.clear()
        assert default_cart.products == {}

    def test_clear_empty_cart(self, default_empty_cart):
        default_empty_cart.clear()
        assert default_empty_cart.products == {}

    def test_total_price(self, default_cart):
        total_price = default_cart.get_total_price()

        assert total_price == 232602.41

    def test_total_price_empty_cart(self, default_empty_cart):
        default_empty_cart.get_total_price()

        assert default_empty_cart.get_total_price() == 0

    def test_buy(self, default_cart):
        default_cart.buy()

        assert default_cart.products == {}