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


<p align="center">
    <img src="https://github.com/Jula90210/Automatyzacja-Selenium-Webdriver/blob/master/wizzair%20projekt1.png" width="750" />
    
    
## **II Przypadek testowy:** ##

**ID:** 002

**Tytuł:** Rejestracja nowego użytkownika używając niepoprawnego numeru telefonu

**Środowisko:** Chrome wersja 89.0.4389.90, Ubuntu 20.04 LTS

**Warunek wstępny:** Uruchomiona przeglądarka. Użytkownik nie jest zalogowany.

**Kroki:**
1. Wejdź na stronę "https://wizzair.com/pl-pl#/"
2. Kliknij "ZALOGUJ SIĘ" 
3. Kliknij "REJESTRACJA" 
4. Wpisz imię 
5. Wpisz nazwisko 
6. Wybierz płeć
7. Wprowadź niepoprawny numer telefonu 
8. Wprowadź e-mail 
9. Wprowadź hasło 
10. Wybierz kraj  
11. Zaakceptuj politykę prywatności 

## **II Oczekiwany rezultat:** ## 
Rejestracja nie powodzi się. Użytkownik dostaje informację, że wprowadzony numer telefonu jest niepoprawny.

## **III Uwagi końcowe:** ## 
Automatyzacja przypadku testowego (test funkcjonalny) powiodła się. Test może być wrażliwy na zmianę struktury strony z powodu konieczności stosowania długich ścieżek w lokalizatorach **XPATH** i **CSS Selector**.

<p align="center">       
    <img src="https://github.com/Jula90210/Automatyzacja-Selenium-Webdriver/blob/master/wizzair2%20test%20case2.png" width="900" /> 

