#搶票
###########################################
#測試台鐵搶票
#網路示範版本     01: https://www.youtube.com/watch?v=rOp5b49qsiU
#過驗證參考      01: https://ithelp.ithome.com.tw/articles/10298908?sc=rss.iron
###########################################

#網路示範版本 https://www.youtube.com/watch?v=rOp5b49qsiU
#pip3 install selenium
from selenium import webdriver #using chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# import pycharm
from time import sleep
import pickle #cookie讀取與存取，免登入重點
import os
import time
import json
from selenium import webdriver

'''
#台鐵官網搶票頁面
main_train_url = 'https://www.railway.gov.tw/tra-tip-web/tip'
#登入頁面
login_url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip008/tip811/memberLogin'
#搶票頁面
get_ticket_url = 'https://www.railway.gov.tw/tra-tip-web/tip/tip001/tip123/query'


#開始搶票的類別
class Gohome:
#先進行初始化
    def __init__(self):
        self.status = 0 #初始化狀態,表示是否初始化
        self.login_method = 1 #登入狀態{0: 需要登入, 1: 已登入}
        self.driver = webdriver.Chrome()

    def set_cookies(self):
        #登入網站用的參數(未登入)#
        self.driver.get(main_train_url)
        print("##點擊登入##")
        #如果未登入
        while self.driver.find("會員登入")!=-1:
            #休眠
            sleep(1)
        print("##成功登入##")
        pickle.dump(self.driver.get_cookies(), open('cookies.pkl', 'wb')) #儲存登入的cookies
        print("##登入cookies儲存成功##")
        self.driver.get(get_ticket_url)
    def get_cookie(self):
        #如果登過，直接領取登入訊息(cookies)#
        cookies = pickle.load(open("cookies.pkl", "rb"))
        for cookie in cookies:
            cookie_dict = {"domain": 'https://www.railway.gov.tw/tra-tip-web/tip/tip008/tip841/tip841profile',
            'name': cookie.get('name'),
            'value': cookie.get('value')
            }
            self.driver.add_coolie(cookie_dict)
            peint("#讀取cookie")

    def login(self):
        ##登入##
        if self.login_method ==0:
            self.driver.get(login_url) #目前未登入，跳去登入
            print("##開始登入##")
        elif self.login_method ==1:
            #如果本地無cookies
            if not os.path.exists('cookies.pkl'):
                self.set_cookies()
            else:
                self.driver.get(get_ticket_url) #確認登入後開始搶票
                self.get_cookie()               #載入登入的訊息
    def enter_concert(self):
        ##開啟瀏覽器##
        print("###打開chrome並且登入台鐵官網###")
        self.login()
        self.driver.refresh()
        self.status = 2
        print('##登入成功#')

if __name__=='__main__':
    GH = Gohome()
    GH.enter_concert()
'''
'''
# login_url = 'https://www.railway.gov.tw/tra-tip-web/tip'
ticket_url = 'https://irs.thsrc.com.tw/IMINT/?locale=tw'
driver = webdriver.Chrome()    # 指向 chromedriver 的位置
driver.get(ticket_url)
print('get')
time.sleep(1)
driver.find_element("xpath", '//*[@id="queryForm"]/div[1]/div[3]/div[2]/label[1]').click()
print('進入班次模式')
time.sleep(2)
account = driver.find_element("xpath", '//*[@id="pid"]')
account.clear()
account.send_keys("T124657651")
print('輸入身分證')
time.sleep(2)
start_station = driver.find_element("xpath", '//*[@id="startStation1"]')
start_station.clear()
start_station.send_keys('1000-臺北')
print('輸入起始車站')
time.sleep(2)
end_station = driver.find_element("xpath", '//*[@id="endStation1"]')
end_station.clear()
end_station.send_keys('3360-彰化')
print('輸入終點車站')
time.sleep(2)
time_station = driver.find_element("xpath", '//*[@id="rideDate1"]')
time_station.clear()
time_station.send_keys('20231222')
#Error 
print('輸入搭乘日期'+'2023/12/22')
time.sleep(2)
ticket_sum = driver.find_element("xpath", '//*[@id="normalQty1"]')
ticket_sum.clear()
ticket_sum.send_keys('2')
print('輸入票數')
time.sleep(2)
ticket_number = driver.find_element("xpath", '//*[@id="trainNoList1"]')
ticket_number.clear()
ticket_number.send_keys('149')
print('輸入班次')
time.sleep(2)
driver.find_element("xpath", '//*[@id="queryForm"]/div[5]/input').click()
print('完成基本資料')
time.sleep(2)
driver.find_element("xpath", '/html/body/div[1]/form[1]/div[1]/table/tbody/tr[2]/td[10]/label').click()
print('點擊車次')
time.sleep(2)
# driver.switch_to_new_tab()

wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div[1]/div/div'))).click()
print('0')
sleep(0.1)
# wait.until(EC.visibility_of_element_located((By.ID, "inpNick"))).send_keys('baby')

sleep(0.1)

# verify = driver.find_element("xpath", '/html/body/div[2]/div[3]/div[1]/div/div/span/div[4]')
# actions = ActionChains(driver)
# actions.move_to_element(verify).click(verify)
# actions.perform()
print('機器人')
time.sleep(10)
# driver.find_element("xpath", '//*[@id="submitBtn"]').click()
print('Finsh！！！')
time.sleep(10)
# # 模拟按下回车键
# 关闭浏览器
driver.quit()

'''
######################################
#e7line 測試登入
#高鐵訂票
ticket_url = 'https://www.thsrc.com.tw/'
driver = webdriver.Chrome()
driver.get(ticket_url)



driver.find_element("xpath", '/html/body/div[5]/div/div[3]/button[2]').click()
print('點擊完蒐集資料')
time.sleep(0.1)

driver.maximize_window()
print('放大視窗完成')
time.sleep(0.3)

driver.find_element("xpath", '//*[@id="aIRS"]/div/img').click()
print('點擊轉換訂票')
time.sleep(2)

windows = driver.window_handles
driver.switch_to.window(windows[-1])
print('切換到新的頁面')
time.sleep(0.1)

driver.find_element("xpath", '//*[@id="cookieAccpetBtn"]').click()
print('點擊完新頁面蒐集資料')
time.sleep(0.3)

Select(driver.find_element("xpath", '//*[@id="BookingS1Form"]/div[4]/div[1]/div/div[1]/div/select')).select_by_index(2)
print('選擇完出發車站')
time.sleep(0.3)

Select(driver.find_element("xpath", '//*[@id="BookingS1Form"]/div[4]/div[1]/div/div[2]/div/select')).select_by_index(12)
print('選擇完出發車站')


time.sleep(18)
driver.quit()
