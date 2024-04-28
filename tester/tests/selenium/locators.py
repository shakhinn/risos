from selenium.webdriver.common.by import By


class AuthPageLocators:
    ETU_ID_BUTTON = (By.XPATH, '//button[text="Войти через ETU ID"]')
    EMAIL = (By.NAME, "email")
    PASSWORD = (By.NAME, "password")
    REMEMBER_CHECKBOX = (By.ID, "remember")
    SUBMIT_BUTTON = (By.XPATH, "//button[@type='submit']")
    LOGOUT = (By.XPATH, "//a[contains(@href='logout')]")
    LK_STUDENT = (By.ID, "body-clone")


class UserPermissionsLocators:
    LOCATOR = ""