from selenium.webdriver.common.by import By

class ForgotPasswordPageLocators:
    TITLE_FORM_FORGOT_PASSWORD = (By.XPATH ,".//h2[text()='Восстановление пароля']") # заголовок формы восстановленяи пароля
    INPUT_EMAIL_FORGOT = (By.XPATH, ".//input[@type='text']")  # поле ввода email на странице восстановления пароля
    SUBMIT_BUTTON_ACCOUNT_RECOVERY = (By.XPATH, ".//button[text() = 'Восстановить']")  # кнопка восстановления пароля на странице восстановления
    SUBMIT_BUTTON_FORGOT_FORM = (By.XPATH, ".//p[text() = 'Вспомнили пароль?']/a")  # Кнопка войти в форме восстановления пароля
    HIDE_AND_SHOW_INPUT_PASSWORD = (By.CSS_SELECTOR, ".input__icon svg") # кнопка скрытия/отображения пароля
    INPUT_PASSWORD_FORGOT = (By.XPATH, ".//input[@type='password']")  # поле ввода пароля на странице восстановления со скрытым паролем
    INPUT_PASSWORD_IS_ACTIVE = (By.XPATH, "//div[contains(@class, 'input_status_active')]") # поле ввода пароля в состоянии активно

class LoginPageLocators:
    FORGOT_PASSWORD_BUTTON = (By.CSS_SELECTOR, 'a[href="/forgot-password"]')  # кнопка восстановить пароль
    SUBMIT_BUTTON_LOGIN_TO_ACCOUNT = (By.XPATH, ".//button[text() = 'Войти']")  # кнопка входа в аккаунт на странице login


class MainPageLocators:
    BUTTON_PROFILE_ACCOUNT = (By.XPATH, ".//a[@href='/account']")  # кнопка входа в личный кабинет
    CONSTRUCTOR_BUTTON = (By.XPATH, './/a[@href="/"]/p')  # кнопка перехода на раздел с конструктором
    FEED_BUTTON = (By.XPATH, './/a[@href="/feed"]/p')  # кнопка перехода на раздел с конструктором
    CONSTRUCTOR_TITLE = (By.XPATH, ".//h1[text()='Соберите бургер']") # заголовок формы конструктора "соберите бургер"
    INGREDIENT_IN_CONSTRUCTOR = (By.XPATH, '//a[@href="/ingredient/61c0c5a71d1f82001bdaaa6c"]') # булочка в конструкторе
    BUN_COUNTER = (By.XPATH, "//p[contains(text(), 'Краторная булка N-200i')]/preceding-sibling::div[contains(@class, 'counter_')]/p") # каунтер Краторная булка
    BUN_STATS_IN_MODAL = (By.XPATH, "//ul[contains(@class, 'Modal_modal__statsList')]") # подпись с составом (белки, жиры...) в попапе булочки
    CLOSE_BUN_TITLE_IN_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]") # закрытие модального окна булки с деталями ингредиента
    CLOSE_ORDER_MODAL = (By.XPATH, "//button[contains(@class, 'Modal_modal__close_modified')]") # закрытие модального окна булки с деталями ингредиента
    BURGER_CONSTRUCTOR_ZONE = (By.CSS_SELECTOR, '.BurgerConstructor_basket__29Cd7') # область для перетаскивания ингредиента заказа
    BUTTON_ORDER = (By.XPATH, "//button[text()='Оформить заказ']") # кнопка оформить заказ
    ORDER_ACCEPTANCE_NOTIFICATION = (By.XPATH, "//p[contains(@class, 'undefined text') and text()='Ваш заказ начали готовить' ] ") # уведомление о взятии заказа в модальном окне
    NUMBER_ORDER_IN_MODAL = (By.XPATH, "//h2[contains(@class, 'text_type_digits-large mb-8')]") #номер заказа в модальном окне
    SUCCESS_ORDER_INDICATOR = (By.CSS_SELECTOR, '[alt="tick animation"]') # иконка с анимацией успешного заказа
    LOADING_ORDER_INDICATOR = (By.CSS_SELECTOR, '[alt="loading animation"]') # иконка с анимацией процесса заказа
    MODAL_OPENED = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")  # модальное окно попапа на главной (общее для всех попапов)
    MODAL_OVERLAY_WHEN_ORDER_PROCESS = (By.XPATH, '//img[@alt="loading animation"]/following-sibling::div[contains(@class, "Modal_modal_overlay_")]')  # оверлей который накладывается на модальное окно оформления заказа


class OrderFeedPageLocators:
    FEED_TITLE = (By.XPATH, ".//h1[text()='Лента заказов']")  # заголовок формы ленты заказов "Лента заказов"
    FIRS_ORDER_CARD_IN_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li[1]") # первая карточка в ленте заказов
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]") # модальное окно на странице заказов
    ORDER_TEXT_IN_ORDER_MODAL = (By.XPATH, "//p[text()= 'Cостав']") # текст состава в открытом модальном окне
    TOTAL_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p") # общее кол-во заказов
    TODAY_ORDERS_COUNTER = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p") # кол-во заказов выполненных сегодня
    ALL_ORDERS_IN_FEED = (By.XPATH, "//p[starts-with(text(),'#')]") # все заказы в ленте заказов
    ALL_ORDERS_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderListReady')]/li[contains(@class, 'digits')]") # все заказы в работе

class ProfilePageLocators:
    ACCOUNT_TEXT_IN_PROFILE = (By.XPATH, ".//p[contains(@class, 'Account_text')]")  # текст на странице профиля
    HISTORY_ORDER_BUTTON_IN_PROFILE = (By.CSS_SELECTOR, 'a[href="/account/order-history"]') # кнопка истории заказов
    BUTTON_LOGOUT_PROFILE = (By.XPATH, ".//button[text() = 'Выход']") # кнопка выхода из профиля
    ALL_ORDERS_IN_HISTORY_USER = (By.XPATH, "//ul[contains(@class, 'OrderHistory_profileList')]//p[contains(@class, 'digits') and not(contains(@class, 'mr-2'))]")  # все заказы в ленте заказов
    PROFILE_MENU =  (By.XPATH, "//ul[contains(@class, 'Account_list')]") # блок основного меню в профиле