class loginPage():

    def __init__(self, page):
        self.__page = page
        self.__customer_login = self.__page.get_by_text("Customer Login")
        self.__manager_login = self.__page.get_by_text("Bank Manager Login")

    def login(self, is_customer=True):
        if (is_customer):
            self.__customer_login.click()
        else:
            self.__manager_login.click()
