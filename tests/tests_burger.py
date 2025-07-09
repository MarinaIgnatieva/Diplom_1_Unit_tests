import pytest

from data import TestData


class TestBurger:
    def test_add_new_buns(self, burger):
        burger.set_buns(TestData.bun)

        assert burger.bun == TestData.bun

    def test_get_ingredient(self, burger):
        for ingr in [TestData.ingredient_1, TestData.ingredient_2]:
            burger.add_ingredient(ingr)

        assert (len(burger.ingredients) == 2 and
                TestData.ingredient_1 in burger.ingredients and
                TestData.ingredient_1 in burger.ingredients)

    def test_remove_ingredient(self, burger):
        for ingr in [TestData.ingredient_1, TestData.ingredient_2]:
            burger.add_ingredient(ingr)

        burger.remove_ingredient(0)

        assert (len(burger.ingredients) == 1 and TestData.ingredient_2 in burger.ingredients and
                TestData.ingredient_1 not in burger.ingredients)

    def test_move_ingredient(self,burger):
        for ingr in [TestData.ingredient_1, TestData.ingredient_2]:
            burger.add_ingredient(ingr)

        burger.move_ingredient(0,1)

        assert (burger.ingredients.index(TestData.ingredient_1) == 1 and
                burger.ingredients.index(TestData.ingredient_2) == 0)

    @pytest.mark.parametrize('data', [TestData.one_bun_one_ingredient,
                             TestData.one_bun_none_ingredient,
                             TestData.one_bun_some_ingredients])
    def test_get_price(self, data, burger):
        burger.set_buns(data[0])

        for ingr in data[1]:
            burger.add_ingredient(ingr)

        assert burger.get_price() == data[2]


    @pytest.mark.parametrize('data', [TestData.one_bun_one_ingredient_receipt,
                                      TestData.one_bun_none_ingredient_receipt,
                                      TestData.one_bun_some_ingredients_receipt])
    def test_get_receipt(self, burger, data):
        burger.set_buns(TestData.bun)

        for ingr in data[1]:
            burger.add_ingredient(ingr)

        assert burger.get_receipt() == data[2]