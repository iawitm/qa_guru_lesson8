import pytest

from models import Product


class TestProductsNegative:

    def test_product_check_quantity_negative_value(self, default_product):
        with pytest.raises(ValueError) as exc_info:
            default_product.check_quantity(-1)

        assert "Quantity can not be negative" in str(exc_info.value)

    def test_product_buy_more_than_available(self, default_product):
        with pytest.raises(ValueError) as exc_info:
            default_product.buy(default_product.quantity+1)

        assert "Not enough quantity" in str(exc_info.value)


class TestCartNegative:

    def test_add_product_zero_products(self, default_cart, default_product):
        with pytest.raises(ValueError) as exc_info:
            default_cart.add_product(default_product,0)

        assert "Count must be greater than 0" in str(exc_info.value)

    def test_add_product_negative_value(self, default_cart, default_product):
        with pytest.raises(ValueError) as exc_info:
            default_cart.add_product(default_product,-1)

        assert "Count must be greater than 0" in str(exc_info.value)

    def test_remove_product_zero_products(self, default_cart, changed_existing_product):
        with pytest.raises(ValueError) as exc_info:
            default_cart.remove_product(changed_existing_product, 0)

        assert "Count must be greater than 0" in str(exc_info.value)

    def test_remove_product_negative_value(self, default_cart, changed_existing_product):
        with pytest.raises(ValueError) as exc_info:
            default_cart.remove_product(changed_existing_product, -1)

        assert "Count must be greater than 0" in str(exc_info.value)

    def test_remove_product_not_existing_product(self, default_cart, default_product):
        with pytest.raises(ValueError) as exc_info:
            default_cart.remove_product(default_product, 1)

        assert "Can not find product in the cart" in str(exc_info.value)

    def test_buy_empty_cart(self, default_empty_cart):
        with pytest.raises(ValueError) as exc_info:
            default_empty_cart.buy()

        assert "Cart is empty" in str(exc_info.value)

    def test_buy_out_of_stock(self, default_cart_out_of_stock):
        with pytest.raises(ValueError) as exc_info:
            default_cart_out_of_stock.buy()

        assert "Not enough quantity in the stock" in str(exc_info.value)