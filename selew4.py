# Import niezbednych bibliotek
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Dane testowe
valid_first_name = "Marcin"
valid_last_name = "Nowak"
gender = "male"
valid_country = "Polska"
valid_phone = "123123234"
invalid_email = "jdshadsa.pl"
valid_password = "Qwert347626@"
valid_country = "Polska"

class WizzairRegistration(unittest.TestCase):
    #Warunki wstepne testow
    def setUp(self):
        print("Przygotowanie testu")
    # Tutaj wlaczymy przegladarke
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(60)
    # Wejdziemy na strone wizzaira
        self.driver.maximize_window()
        self.driver.get('https://wizzair.com/pl-pl/#/')

    # Instrukcje po kazdym tescie
    def tearDown(self):
        print("Sprzatanie po tescie")

    # Wylaczamy przegladarke
        self.driver.quit()

    # Metody testowe-zaczynaja sie od slowa "test"
    def testInvalidEmail(self):
        print("Prawdziwy test")
    # Tutaj bedziemy wykonywac kroki
    # Krok 1. Kliknij "Zaloguj"
        driver = self.driver
        zaloguj_btn = driver.find_element_by_xpath('//button[@data-test="navigation-menu-signin"]')
        zaloguj_btn.click()
        #print(type(zaloguj_btn))
    # Poczekajmy 15 sekund zeby zdazyc zauwazyc co sie dzieje
        time.sleep(15)
    # Krok 2. Rejestracja
        driver.find_element_by_css_selector('button[data-test="registration"]').click()
    # Krok 3. Wpisz imie
        name_input = driver.find_element_by_name('firstName')
        name_input.send_keys(valid_first_name)
    # Krok 4. Wpisz nazwisko
        lastname_input = driver.find_element_by_name('lastName')
        lastname_input.send_keys(valid_last_name)
    # Krok 5. Wybierz plec
        if gender == "female":
            # Wybierz kobiete
            driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()
        else:
            # Odslon mezczyzne
            name_input.click()
            # Wybierz mezczyzne
            driver.find_element_by_xpath('//label[@data-test="register-gendermale"]').click()
        time.sleep(4)
    # Krok 6. Wybierz kraj
        driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]').click()
        cc_input = driver.find_element_by_name('phone-number-country-code')
        cc_input.send_keys(valid_country, Keys.RETURN)
    # Krok 7. Wpisz numer telefonu
        phone_input = driver.find_element_by_xpath('//input[@data-test="check-in-step-contact-phone-number"]')
        phone_input.send_keys(valid_phone)
    # Krok 8. Wpisz NIEPOPRAWNY email
        email_input = driver.find_element_by_xpath('//input[@data-test="booking-register-email"]')
        email_input.send_keys(invalid_email)
    # Krok 9. Wpisz haslo
        password_input = driver.find_element_by_name('password')
        password_input.send_keys(valid_password)
    # Krok 10. Wpisz narodowosc
        nationality_input = driver.find_element_by_name('country-select')
        nationality_input.send_keys(valid_country, Keys.RETURN)
    # Krok 11. Zaakceptuj polityke prywatnosci
        driver.find_element_by_xpath('//label[@for="checkbox-privacyPolicy"]').click()

        time.sleep(4)
    # Jesli uruchamiamy z tego pliku
if __name__=="__main__":

    # Wlaczamy testy
    unittest.main()
