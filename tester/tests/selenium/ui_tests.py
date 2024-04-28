from users_permissions_page import UsersPermissionsPage

def test_change_roles(browser, wait):
    page = UsersPermissionsPage(browser, wait)
    page.open_sidebar()
    page.copy_surname()
    page.find_by_surname()
    page.open_card()
    page.choose_roles()
    page.save_and_refresh_page()
    page.check_roles()
