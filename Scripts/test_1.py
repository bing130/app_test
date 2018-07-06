import allure


class Test_01:

    @allure.step(title="测试步骤001")
    def test_01_1(self):
        assert 1

    @allure.step(title="测试步骤002")
    def test_01_2(self):
        assert 0
