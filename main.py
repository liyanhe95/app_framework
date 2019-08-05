
import pytest
if __name__ == '__main__':
    pytest.main(["--html=Outputs/Reports/pytest_result.html",
             "--junitxml=Outputs/Reports/result.xml",
                 "--alluredir=Outputs/allure_reports"])