# Automatyzacja przypadku testowego przy pomocy Selenium-Webdriver #

## **I Przypadek testowy:** ##

**ID:** 001

**Tytuł:** Rejestracja nowego użytkownika używając niepoprawnego adresu e-mail

**Środowisko:** Chrome wersja 89.0.4389.90, Ubuntu 20.04 LTS

**Warunek wstępny:** Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.

**Kroki:**
1. Wejdź na stronę "https://wizzair.com/pl-pl#/"
2. Kliknij "ZALOGUJ SIĘ" 
3. Kliknij "REJESTRACJA" 
4. Wpisz imię 
5. Wpisz nazwisko 
6. Wybierz płeć
7. Wprowadź nr telefonu 
8. Wprowadź niepoprawny e-mail 
9. Wprowadź hasło 
10. Wybierz kraj  
11. Zaakceptuj politykę prywatności  

## **II Oczekiwany rezultat:** ## 
Rejestracja nie powodzi się. Użytkownik dostaje informację, że wprowadzony e-mail jest niepoprawny.

## **III Uwagi końcowe:** ## 
Automatyzacja przypadku testowego (test funkcjonalny) powiodła się. Test może być wrażliwy na zmianę struktury strony z powodu konieczności stosowania długich ścieżek w lokalizatorach **XPATH** i **CSS Selector**. 

![wizzair2 projekt1](https://user-images.githubusercontent.com/53537695/113926992-2f355600-97ed-11eb-8779-5b91ba92e343.png)