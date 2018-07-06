import allure,pytest


class Test_01:

    @pytest.allure.severity(pytest.allure.severity_level.TRIVIAL)
    @allure.step(title="测试步骤001")
    def test_01_1(self):
        allure.attach('描述', '我是测试步骤001的描述～～～')
        assert 1

    @pytest.allure.severity(pytest.allure.severity_level.BLOCKER)
    @allure.step(title="测试步骤002")
    def test_01_2(self):
        allure.attach('描述', '我是测试步骤002的描述～～～')
        assert 0
