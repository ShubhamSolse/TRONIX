from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from APPScreen import start_screen
from kivy.core.window import Window
from kivymd.toast import toast
from kivy.uix.screenmanager import Screen, ScreenManager, FadeTransition,SlideTransition
from kivy.clock import Clock
import json
import requests
from kivymd.stiffscroll import StiffScrollEffect




class FirstScreen(Screen):
    def on_enter(self):

        Clock.schedule_once(
            self.change_to_login_screen,10
        )
    def change_to_login_screen(self, interval):
        self.parent.transition = FadeTransition(duration=1)
        self.parent.current = "second"


class SecondScreen(Screen):
    pass


class ThirdScreen(Screen):
    pass


class ForthScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


class FifthScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


class SixthScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


class SeventhScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


class EightScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


class NineScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


class TenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"
    def set_screen1(self):
        MDApp.get_running_app().root.current = "fortyTwo"
class ElevenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"
    def set_screen1(self):
        MDApp.get_running_app().root.current = "fortyTwo"

class TwelveScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"
    def set_screen1(self):
        MDApp.get_running_app().root.current = "fortyTwo"

class ThirteenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"
    def set_screen1(self):
        MDApp.get_running_app().root.current = "fortyTwo"

class FourteenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"
    def set_screen1(self):
        MDApp.get_running_app().root.current = "fortyTwo"

class FifteenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"
    def set_screen1(self):
        MDApp.get_running_app().root.current = "fortyTwo"

class SixteenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"
    def set_screen1(self):
        MDApp.get_running_app().root.current = "fortyTwo"

class SeventeenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"


class EighteenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"


class NineteenScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"


class TwentyScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "forth"


class TwentyOneScreen(Screen):
    pass


class TwentyTwoScreen(Screen):
    pass


class TwentyThreeScreen(Screen):
    pass


class TwentyFourScreen(Screen):
    pass


class TwentyFiveScreen(Screen):
    pass


class TwentySixScreen(Screen):
    pass


class TwentySevenScreen(Screen):
    pass


class TwentyEightScreen(Screen):
    pass


class TwentyNineScreen(Screen):
    pass


class ThirtyScreen(Screen):
    pass


class ThirtyOneScreen(Screen):
    pass


class ThirtyTwoScreen(Screen):
    pass


class ThirtyThreeScreen(Screen):
    pass


class ThirtyFourScreen(Screen):
    pass


class ThirtyFiveScreen(Screen):
    pass


class ThirtySixScreen(Screen):
    pass


class ThirtySevenScreen(Screen):
    pass


class ThirtyEightScreen(Screen):
    pass


class ThirtyNineScreen(Screen):
    pass


class FortyScreen(Screen):
    pass


class FortyOneScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


class FortyTwoScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


class FortyThreeScreen(Screen):
    pass


class FortyFourScreen(Screen):
    pass


class FortyFiveScreen(Screen):
    pass


class FortySixScreen(Screen):
    pass


class FortySevenScreen(Screen):
    pass


class FortyEightScreen(Screen):
    pass


class FortyNineScreen(Screen):
    pass


class FiftyScreen(Screen):
    pass


class FiftyOneScreen(Screen):
    pass


class FiftyTwoScreen(Screen):
    pass


class FiftyThreeScreen(Screen):
    pass


class FiftyFourScreen(Screen):
    pass


class FiftyFiveScreen(Screen):
    pass


class FiftySixScreen(Screen):
    def set_screen(self):
        MDApp.get_running_app().root.current = "third"


sm = ScreenManager()
sm.add_widget(FirstScreen(name='first'))
sm.add_widget(SecondScreen(name='second'))
sm.add_widget(ThirdScreen(name='third'))
sm.add_widget(ForthScreen(name='forth'))
sm.add_widget(FifthScreen(name='fifth'))
sm.add_widget(SixthScreen(name='sixth'))
sm.add_widget(SeventhScreen(name='seventh'))
sm.add_widget(EightScreen(name='eight'))
sm.add_widget(NineScreen(name='nine'))
sm.add_widget(TenScreen(name='ten'))
sm.add_widget(ElevenScreen(name='eleven'))
sm.add_widget(TwelveScreen(name='twelve'))
sm.add_widget(ThirteenScreen(name='thirteen'))
sm.add_widget(FourteenScreen(name='fourteen'))
sm.add_widget(FifteenScreen(name='fifteen'))
sm.add_widget(SixteenScreen(name='sixteen'))
sm.add_widget(SeventeenScreen(name='seventeen'))
sm.add_widget(EighteenScreen(name='eighteen'))
sm.add_widget(NineteenScreen(name='nineteen'))
sm.add_widget(TwentyScreen(name='twenty'))
sm.add_widget(TenScreen(name='twentyOne'))
sm.add_widget(TwentyTwoScreen(name='twentyTwo'))
sm.add_widget(TwentyThreeScreen(name='twentyThree'))
sm.add_widget(TwentyFourScreen(name='twentyFour'))
sm.add_widget(TwentyFiveScreen(name='twentyFive'))
sm.add_widget(TwentySixScreen(name='twentySix'))
sm.add_widget(TwentySevenScreen(name='twentySeven'))
sm.add_widget(TwentyEightScreen(name='twentyEight'))
sm.add_widget(TwentyNineScreen(name='twentyNine'))
sm.add_widget(ThirtyScreen(name='thirty'))
sm.add_widget(ThirtyOneScreen(name='thirtyOne'))
sm.add_widget(ThirtyTwoScreen(name='thirtyTwo'))
sm.add_widget(ThirtyThreeScreen(name='thirtyThree'))
sm.add_widget(ThirtyFourScreen(name='thirtyFour'))
sm.add_widget(ThirtyFiveScreen(name='thirtyFive'))
sm.add_widget(ThirtySixScreen(name='thirtySix'))
sm.add_widget(ThirtySevenScreen(name='thirtySeven'))
sm.add_widget(ThirtyEightScreen(name='thirtyEight'))
sm.add_widget(ThirtyNineScreen(name='thirtyNine'))
sm.add_widget(FortyScreen(name='forty'))
sm.add_widget(FortyOneScreen(name='fortyOne'))
sm.add_widget(FortyTwoScreen(name='fortyTwo'))
sm.add_widget(FortyThreeScreen(name='fortyThree'))
sm.add_widget(FortyFourScreen(name='fortyFour'))
sm.add_widget(FortyFiveScreen(name='fortyFive'))
sm.add_widget(FortySixScreen(name='fortySix'))
sm.add_widget(FortySevenScreen(name='fortySeven'))
sm.add_widget(FortyEightScreen(name='fortyEight'))
sm.add_widget(FortyNineScreen(name='fortyNine'))
sm.add_widget(FiftyScreen(name='fifty'))
sm.add_widget(FiftyOneScreen(name='fiftyOne'))
sm.add_widget(FiftyTwoScreen(name='fiftyTwo'))
sm.add_widget(FiftyThreeScreen(name='fiftyThree'))
sm.add_widget(FiftyFourScreen(name='fiftyFour'))
sm.add_widget(FiftyFiveScreen(name='fiftyFive'))
sm.add_widget(FiftySixScreen(name='fiftySix'))


class Tronix(MDApp):

    def build(self):

        self.theme_cls.primary_palette = "Blue"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_hue = 'A700'
        self.effect_cls = StiffScrollEffect
        self.screen = Builder.load_string(start_screen)
        self.url = "https://login-3009a-default-rtdb.firebaseio.com/.json"


        return self.screen


    def show_popup(self):
        toast('Data saved successfully')
    def signup(self):
        signupEmail = self.screen.get_screen('fortyNine').ids.signup_email.text
        signupPassword =self.screen.get_screen('fortyNine').ids.signup_password.text
        signupconPassword = self.screen.get_screen('fortyNine').ids.signup_con_password.text
        if signupEmail.split() == [] or signupPassword.split() == [] or signupconPassword.split() == []:

            toast('Enter a valid data')
            self.screen.get_screen('fortyNine').manager.current = 'fortyNine'
        elif signupPassword.split() != signupconPassword.split():
            toast("Password not matching")
            self.screen.get_screen('fortyNine').manager.current = 'fortyNine'
        else:

            signup_info = str({f'\"{signupEmail}\":{{"Password":\"{signupPassword}\"}}'})
            password=len(signupPassword)

            print(password)
            signup_info = signup_info.replace("\'", " ")
            signup_info = signup_info.replace(".", "-")

            to_database = json.loads(signup_info)

            requests.patch(url=self.url, json=to_database)
            self.screen.get_screen('second').manager.current = 'second'
            toast('Signup success ')
    auth="ORxlFejos3A2gNQVmD9mWy1LwpjdF82WCg8REHoE"
    def login(self,):
        loginEmail = self.screen.get_screen('second').ids.login_email.text
        loginPassword = self.screen.get_screen('second').ids.login_password.text
        self.login_check = False
        supported_loginEmail = loginEmail.replace('.', '-')
        supported_loginPassword = loginPassword.replace('.', '-')

        request = requests.get(self.url + '?auth=' + self.auth)
        data = request.json()
        emails = set()
        for key, value in data.items():
            emails.add(key)
        if supported_loginEmail in emails and supported_loginPassword == data[supported_loginEmail]['Password']:

            self.login_check = True
            self.screen.get_screen('third').manager.current = 'third'
            toast('Welcome to TRONIX')
        else :
            toast('User not found')

    def login_email(self,login_email):

        login_email=login_email.replace('.', '-')
        print(login_email)
        self.url1 = "https://login-3009a-default-rtdb.firebaseio.com/"+ str(login_email)+".json"



    def buy(self,product,price,label_value):
        Total=0
        a=float(price)
        b=int(label_value)
        c=a*b
        Total= Total+ c
        print(product,label_value,Total)
        product_info = str({f'\"{product}\":{{"Quantity":\"{label_value}\","Total Price":\"{Total}\"}}'})

        product_info = product_info.replace(".", "-")
        product_info = product_info.replace("\'", " ")

        to_database = json.loads(product_info)

        requests.patch(url=self.url1, json=to_database)







Tronix().run()
