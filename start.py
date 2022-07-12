import time
from selenium import webdriver
import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

def log(log_text):
    log_text = str(time.strftime("%Y.%m.%d %H:%M:%S")) + " ➾ " + log_text
    print(log_text)
    log_file = open("log.txt", "a", encoding='utf-8')
    log_file.write(log_text + "\n")
    log_file.close()

global_delay = 3
yeni_sifre = "reset2reset2!"

def delay(delay_time):
    log("Delay Baslangıc: " + str(delay_time))
    for i in range(delay_time, 0, -1):
        time.sleep(1)
        log("Delay Kalan: " + str(i))
    

if __name__ == '__main__':
    log('Bu program Can Tarafından Yapılmıştır.')
    log('https://fastuptime.com ve https://speedsmm.com üzerinden bize ulaşabilirsiniz.')
    log('Program başlatıldı')


def login():
    ac_file = open("ac.txt", "r", encoding='utf-8')
    ac_list = ac_file.readlines()
    for ac in ac_list:
        driver = uc.Chrome()
        driver.delete_all_cookies()
        driver.get('https://accounts.google.com/signin/v2/identifier?flowName=GlifWebSignIn&flowEntry=ServiceLogin')
        driver.maximize_window()
        delay(7)
        ac = ac.split(":")
        email = ac[0]
        password = ac[1]
        try:
            driver.find_element(By.ID,"identifierId").send_keys(email)
            driver.find_element(By.ID,"identifierNext").click()
            log('Email Girildi: ' + email)
            delay(global_delay)
            driver.find_element(By.NAME,"password").send_keys(password)
            driver.find_element(By.ID,"passwordNext").click()
            log('Şifre Girildi: ' + password)
            delay(8)
            try:
                driver.get('https://myaccount.google.com/?utm_source=sign_in_no_continue&pli=1')
                delay(5)
                hg_mesaj = driver.find_element(By.CLASS_NAME, 'XY0ASe').text
                #if includes Hoş geldiniz mesajı
                if hg_mesaj.find("Hoş geldiniz") != -1:
                    hg_mesaj = hg_mesaj.replace('Hoş geldiniz', '')
                    log('Başarıyla Giriş Yapıldı: ' + email + ' Kullanıcı Adı: ' + hg_mesaj)
                    delay(global_delay)
                    try:
                        log('Şifre Değiştirme İşlemi Başladı')
                        driver.get('https://myaccount.google.com/signinoptions/password?continue=https%3A%2F%2Fmyaccount.google.com%2Fsecurity')
                        delay(5)
                        driver.find_element(By.NAME,'password').send_keys(password)
                        driver.find_element(By.ID,"passwordNext").click()
                        delay(15)
                        driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/form/div/div[1]/div/div[1]/div/div/div/label/input').send_keys(yeni_sifre)
                        driver.find_element(By.XPATH, '/html/body/c-wiz/div/div[2]/div[2]/c-wiz/div/div[4]/form/div/div[1]/div/div[3]/div/div/label/input').send_keys(yeni_sifre)
                        driver.find_element(By.CLASS_NAME, 'VfPpkd-vQzf8d').click()
                        log(hg_mesaj + ' İsimli Hesabın Şifre Değiştirme İşlemi Tamamlandı')
                        delay(global_delay)
                        new_pass_file = open("new_pass.txt", "w", encoding='utf-8')
                        yenisiu = email + ":" + yeni_sifre + "|" + hg_mesaj
                        new_pass_file.write(yenisiu + "\n")
                        driver.quit()
                    except Exception as e:
                        print(e)
                        log(hg_mesaj + ' İsimli Hesabın Şifre Değiştirme İşlemi Başarısız Oldu')
                        delay(global_delay)
                        driver.quit()
                else:
                    log('Giriş Yapılamadı: ' + email)
                    delay(global_delay)
                    driver.quit()
            except:
                log('Giriş Yapılamadı: ' + email)
                delay(global_delay)
                driver.quit()
        except:
            log('Giriş Yapılamadı: ' + email)
            delay(global_delay)
            driver.quit()
            continue
if __name__ == '__main__':
    login()