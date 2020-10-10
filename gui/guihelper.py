import pygetwindow as gw
import pyautogui
import time
import gui.menu as menu
import gui.stats as stats

from PIL import Image
import pytesseract



pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

class GUIHelper:
    def perform_setup(self):
        #Set Up Window
        window = gw.getWindowsWithTitle('DOSBox 0.73')[0]
        window.moveTo(0,0)
        window.activate()
        return window

    def create_menu(self, window):
        #Find and create menu
        menu_location = pyautogui.locateOnScreen('images/menu.png', region=(0,0, window.width, window.height), confidence = 0.8)
        mn = menu.Menu(menu_location.left, menu_location.top)
        self.menu = mn
        return mn

    def click_menu(self, menu_item, clicks=1):
        pyautogui.moveTo(menu_item)
        for i in (range(0, clicks)):
            pyautogui.click()

    def hold_and_click_menu(self, menu_item, selection):
        pyautogui.moveTo(menu_item)
        pyautogui.mouseDown()
        time.sleep(0.7)
        for i in (range(1, selection+1)):
            pyautogui.moveTo(menu_item[0], menu_item[1]+(18*i))
        pyautogui.mouseUp()

    def build_budget_window(self):
        begin = time.time()
        property_tax = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_property.top, stats.tx_property.left, stats.tx_property.width, stats.tx_property.height)), lang='eng')
        btn_raise_property = stats.tx_raise_property
        btn_lower_property = stats.tx_lower_property
        #property_to_date = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_property_to_date.top, stats.tx_property_to_date.left, stats.tx_property_to_date.width, stats.tx_property_to_date.height)), lang='eng')
        #property_eoy = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_property_eoy.top, stats.tx_property_eoy.left, stats.tx_property_eoy.width, stats.tx_property_eoy.height)), lang='eng')
        ordinance_to_date = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_ordinance_to_date.top, stats.tx_ordinance_to_date.left, stats.tx_ordinance_to_date.width, stats.tx_ordinance_to_date.height)), lang='eng')
        #ordinance_eoy = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_ordinance_eoy.top, stats.tx_ordinance_eoy.left, stats.tx_ordinance_eoy.width, stats.tx_ordinance_eoy.height)), lang='eng')
        bond_to_date = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_bond_to_date.top, stats.tx_bond_to_date.left, stats.tx_bond_to_date.width, stats.tx_bond_to_date.height)), lang='eng')
        #bond_eoy = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_bond_eoy.top, stats.tx_bond_eoy.left, stats.tx_bond_eoy.width, stats.tx_bond_eoy.height)), lang='eng')
        #police_spending = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_police.top, stats.tx_police.left, stats.tx_police.width, stats.tx_police.height)), lang='eng')
        btn_raise_police = stats.tx_raise_police
        btn_lower_police = stats.tx_lower_police
        #police_to_date = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_police_to_date.top, stats.tx_police_to_date.left, stats.tx_police_to_date.width, stats.tx_police_to_date.height)), lang='eng')
        police_eoy = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_police_eoy.top, stats.tx_police_eoy.left, stats.tx_police_eoy.width, stats.tx_police_eoy.height)), lang='eng')
        #fire_spending = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_fire.top, stats.tx_fire.left, stats.tx_fire.width, stats.tx_fire.height)), lang='eng')
        btn_raise_fire = stats.tx_raise_fire
        btn_lower_fire = stats.tx_lower_fire
        #fire_to_date = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_fire_to_date.top, stats.tx_fire_to_date.left, stats.tx_fire_to_date.width, stats.tx_fire_to_date.height)), lang='eng')
        fire_eoy = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_fire_eoy.top, stats.tx_fire_eoy.left, stats.tx_fire_eoy.width, stats.tx_fire_eoy.height)), lang='eng')
        #health_spending = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_health.top, stats.tx_health.left, stats.tx_health.width, stats.tx_health.height)), lang='eng')
        btn_raise_health = stats.tx_raise_health
        btn_lower_health = stats.tx_lower_health
        #health_to_date = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_health_to_date.top, stats.tx_health_to_date.left, stats.tx_health_to_date.width, stats.tx_health_to_date.height)), lang='eng')
        health_eoy = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_health_eoy.top, stats.tx_health_eoy.left, stats.tx_health_eoy.width, stats.tx_health_eoy.height)), lang='eng')
        #edu_spending = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_edu.top, stats.tx_edu.left, stats.tx_edu.width, stats.tx_edu.height)), lang='eng')
        btn_raise_edu = stats.tx_raise_edu
        btn_lower_edu = stats.tx_lower_edu
        #edu_to_date = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_edu_to_date.top, stats.tx_edu_to_date.left, stats.tx_edu_to_date.width, stats.tx_edu_to_date.height)), lang='eng')
        edu_eoy = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_edu_eoy.top, stats.tx_edu_eoy.left, stats.tx_edu_eoy.width, stats.tx_edu_eoy.height)), lang='eng')
        #transit_spending = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_transit.top, stats.tx_transit.left, stats.tx_transit.width, stats.tx_transit.height)), lang='eng')
        btn_raise_transit = stats.tx_raise_transit
        btn_lower_transit = stats.tx_lower_transit
        #transit_to_date = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_transit_to_date.top, stats.tx_transit_to_date.left, stats.tx_transit_to_date.width, stats.tx_transit_to_date.height)), lang='eng')
        transit_eoy = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_transit_eoy.top, stats.tx_transit_eoy.left, stats.tx_transit_eoy.width, stats.tx_transit_eoy.height)), lang='eng')
        #to_date_total = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_eoy_total.top, stats.tx_eoy_total.left, stats.tx_eoy_total.width, stats.tx_eoy_total.height)), lang='eng')
        eoy_treasury  = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_eoy_treasury.top, stats.tx_eoy_treasury.left, stats.tx_eoy_treasury.width, stats.tx_eoy_treasury.height)), lang='eng')
        eoy_total = pytesseract.image_to_string(pyautogui.screenshot(region=(stats.tx_to_date_total.top, stats.tx_to_date_total.left, stats.tx_to_date_total.width, stats.tx_to_date_total.height)), lang='eng')
        #print(pytesseract.image_to_string(pyautogui.screenshot(region=(stats.time_money.top, stats.time_money.left, stats.time_money.width, stats.time_money.height)), lang='eng'))
        print("Property Tax:", property_tax)
        print("City Ordinance:", ordinance_to_date)
        print("Bond Payments:", bond_to_date)
        print("Police Dept:", police_eoy)
        print("Fire Dept:", fire_eoy)
        print("Health & Welfare:", health_eoy)
        print("Education:", edu_eoy)
        print("Transit:", transit_eoy)
        print("Estimated EOY:", eoy_total)
        print("EOY Treasury:", eoy_treasury)
        print("Took ", time.time() - begin, " seconds to analyze statistics.")
    
    def __init__(self):
        self.window = self.perform_setup()
        self.scrollbar_v = pyautogui.locateOnScreen('images/scrollbar_v.png', region=(0,0, self.window.width, self.window.height), grayscale=True)
        self.scrollbar_h = pyautogui.locateOnScreen('images/scrollbar_h.png', region=(0,0, self.window.width, self.window.height), grayscale=True)
        self.scroll_up = pyautogui.locateOnScreen('images/scroll_up.png', region=(0,0, self.window.width, self.window.height), grayscale=True)
        self.scroll_down = pyautogui.locateOnScreen('images/scroll_down.png', region=(0,0, self.window.width, self.window.height), grayscale=True)
        self.scroll_right = pyautogui.locateOnScreen('images/scroll_right.png', region=(0,0, self.window.width, self.window.height), grayscale=True)
        self.scroll_left = pyautogui.locateOnScreen('images/scroll_left.png', region=(0,0, self.window.width, self.window.height), grayscale=True)
        self.menu = None
