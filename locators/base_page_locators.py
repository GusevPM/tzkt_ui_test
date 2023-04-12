from selenium.webdriver.common.by import By


class BasePageLocators:
    BUTTON_ACCEPT_COOKIES = [By.XPATH, './/span[@class="v-btn__content" and text()="OK"]']
    BUTTON_NETWORK_SELECTOR = [By.XPATH, './/div[@class="v-select__selections"]']
    BUTTON_API = [By.XPATH, './/span[@class="v-btn__content" and text()=" API "]']
    BUTTON_DAPPS = [By.XPATH, './/span[@class="v-btn__content" and text()=" Dapps "]']
    BUTTON_STATS = [By.XPATH, './/span[@class="v-btn__content" and text()=" Stats "]']
    BUTTON_BAKERS = [By.XPATH, './/span[@class="v-btn__content" and text()=" Bakers "]']
    BUTTON_BLOCKCHAIN = [By.XPATH, './/span[text()="Blockchain"]']
    BUTTON_BUY_TEZOS = [By.XPATH, './/span[@class="v-btn__content" and text()=" Buy Tezos "]']

    INPUT_SEARCH = [By.XPATH, './/input[@id="input-34"]']
