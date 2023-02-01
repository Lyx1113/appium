from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

class Testtb:
    def setup(self):
        caps = {}
        caps["platformName"] = "android"
        caps["deviceName"] = "xxx"
        caps["appPackage"] = "com.smartahc.android.tb_smart_trace"
        caps["appActivity"] = ".activity.MainActivity"
        caps["autoGrantPermissions"] = "true"
        caps["ensureWebviewsHavePages"] = True
        caps["noReset"] = False
        caps["fullReset"] = True
        caps["app"] = "D:/SmartAHC/test engineer/睿溯/APK/1.5.4/app_production_release_v364.apk"

        driver = webdriver.Remote("http://localhost:4723/wd/hub", caps)
        driver.implicitly_wait(10)

    def test_tb(self):
        # TouchAction(self).long_press().move_to().release().perform()
        el1 = self.driver.find_element_by_id("com.smartahc.android.tb_smart_trace:id/edtAccount")
        el1.send_keys("test02")
        el2 = self.driver.find_element_by_id("com.smartahc.android.tb_smart_trace:id/edtPassword")
        el2.send_keys("q123456")
        el3 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.Button")
        el3.click()

    def teardown(self):
        self.drver.quit()