
from   selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from   selenium import webdriver
from   selenium.webdriver.support.ui import WebDriverWait
from   selenium.webdriver.support.ui import Select


from   Pylite.iLibraries.TypeDeclaration import BrowserType,IdentifierType,SelectType #,ResultType
import Pylite.reports.Pylite.iLibraries.Configuration as Configuration
import Pylite.reports.Pylite.drivers.BrowserConfig as BrowserConfig
 
global listVal
listVal=[]


class Browser():
       
    def __init__(self):      
        self._driver          = None
        self._wait            = None
        self._capabilities    = None
        self._element         = None
        self._element_status  = None
        self.text_value       = None
        print("Ui elements... __ init__")

    def initialization_browser_go_to_app(self, browser_type, app_url):
        if browser_type == BrowserType.CHROME :
            print("BrowserConfig.CHROME_DRIVER_PATH",BrowserConfig.CHROME_DRIVER_PATH)
            self._driver = webdriver.Chrome(executable_path=BrowserConfig.CHROME_DRIVER_PATH)
            self.go_to(app_url)
        elif browser_type == BrowserType.IE :
            self._capabilities = self.desired_capabilities()
            self._driver = webdriver.Ie (executable_path=BrowserConfig.IE_DRIVER_PATH,
                                         capabilities = self._capabilities)
            self.go_to(app_url)

        self._wait = WebDriverWait(self._driver, Configuration.MAX_WAIT_TIME)

    def go_to(self,app_url):
        self._driver.delete_all_cookies()
        self._driver.maximize_window()
        self._driver.get(app_url)

    def desired_capabilities(self):
        self._capabilities = DesiredCapabilities.INTERNETEXPLORER
        self._capabilities["requireWindowFocus"] = True
        self._capabilities["NATIVE_EVENTS"] = False
        self._capabilities["acceptSslCerts"] = True
        self._capabilities["ie.ensureCleanSession"] = True
        self._capabilities["cleanSession"] = True
        #self._capabilities["platform"] = True
        #self._capabilities["version"] = True
        #self._capabilities["ignoreZoomSetting"] = True
        #self._capabilities["ie.INTRODUCE_FLAKINESS_BY_IGNORING_SECURITY_DOMAINS"] = True
        return self._capabilities

    def verifying_element(self):
        if self._element.is_displayed():self._element_status=True
        else:self._element_status=False

    def find_element(self,Identifier_type,element_property):
        if Identifier_type== IdentifierType.id:
            self._element=self._driver.find_element_by_id(element_property)
            self.verifying_element()
        elif Identifier_type == IdentifierType.name:
            self._element = self._driver.find_element_by_name(element_property)
            self.verifying_element()
        elif Identifier_type == IdentifierType.link_text:
            self._element = self._driver.find_element_by_link_text(element_property)
            self.verifying_element()
        elif Identifier_type == IdentifierType.class_name:
            self._element = self._driver.find_element_by_class_name(element_property)
            self.verifying_element()
        elif Identifier_type == IdentifierType.css_selector:
            self._element = self._driver.find_element_by_css_selector(element_property)
            self.verifying_element()
        elif Identifier_type == IdentifierType.xpath:
            self._element = self._driver.find_element_by_xpath(element_property)
            self.verifying_element()
        else:
            print("Please use Predefind Keyword defind by 9Libraries. "+Identifier_type)

    def click_element(self,Identifier_type,element_property,description,expected_result):
        self.find_element(Identifier_type, element_property)
        if self._element_status==True:
            self._element.click()
            self.add_step(description, expected_result,"PASS")
        else:
            self.add_step(description, expected_result, "FAIL")

    def set_text(self,Identifier_type,element_property,input_text,description,expected_result):
        self.find_element(Identifier_type,element_property)
        temp_description    = description+"-"+str(input_text)
        temp_expectedresult = expected_result+"-"+str(input_text)
        
        if self._element_status==True:
            self._element.send_keys(input_text)          
            self.add_step(temp_description,temp_expectedresult,"PASS")
        else:
            self.add_step(temp_description,temp_expectedresult,"FAIL")

    def switch_to_window(self):
        current_window = self._driver.current_window_handle
        for window in self._driver.window_handles:
            if window!= current_window:
                self._driver.switch_to_window(window)
    def select(self, Identifier_type, element_property, select_type, Input_Parameter):
        self.find_element(self, Identifier_type, element_property)
        if self._element_status != False:
            select = Select(self._element)
            if select_type == SelectType._by_value:
                select.select_by_value(Input_Parameter)
            elif select_type == SelectType._index:
                select.select_by_index(Input_Parameter)
            elif select_type == SelectType._visible_text:
                select.select_by_visible_text(Input_Parameter)
        
    def add_step(self,description,expected_result,status):
        Sublist = []
        Sublist.append(description)
        Sublist.append(expected_result)
        actual_result = expected_result.replace('should', 'successfully')
        actual_result = actual_result.replace('able to', '')
        actual_result = actual_result.replace('Able to', '')
        Sublist.append(actual_result)
        Sublist.append(status)
        print(Sublist)
        listVal.append(Sublist)       
        Sublist = None
    
    def tear_down(self):
        self._driver.close()
           
        
        