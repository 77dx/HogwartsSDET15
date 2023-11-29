
class LoginBase:

    def account_locator(self):
        return '//input[@class="login-user"]'

    def password_locator(self):
        return '//input[@class="login-password"]'

    def login_button_locator(self):
        return '//button[@class="login-button-main login-button-container"]'

