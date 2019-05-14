from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.keys import Keys
import string
import time
from selenium.webdriver import *

startTime = time.time()
print(startTime)

try:
    driver = webdriver.Chrome("d:\\chromedriver.exe")
    driver.get("https://login.salesforce.com")
    driver.maximize_window()

except:
    print("Unable to login!!!")


class PermissionSet():
    def log_me(self):
        try:
            f = open("id.txt", "r")
            line = f.readline()
            username = driver.find_element_by_id("username").send_keys(line)
            f.close()
            g = open("pwd.txt", "r")
            line = g.readline()
            pwd = driver.find_element_by_id("password").send_keys(line)
            g.close()
            submit = driver.find_element_by_name("Login").click()

        except IOError:
            print("Incorrect id or password!!!")

    def find_setup(self):
        try:
            setup = driver.find_element_by_id("setupLink").click()
            time.sleep(4)
            find_search = driver.find_element_by_id("setupSearch").send_keys("Permission Sets")
            time.sleep(2)
            driver.find_element_by_id("PermSets_font").click()
            time.sleep(2)

        except:
            pass

    def create_ps(self):
        driver.find_element_by_name("new").click()
        time.sleep(4)
        driver.find_element_by_class_name("pc_permSetLabel").send_keys("DemandFarm Standard User PS" + ' ' + random.choice
        (string.ascii_letters) + random.choice(string.digits))
        driver.find_element_by_id("save").click()

    def existing_ps(self):
        driver.find_element_by_link_text('DF Users').click()
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.LINK_TEXT, "Object Settings")))
        # driver.find_element_by_link_text("Object Settings").click()
        # time.sleep(4)

    def assigned_app(self):

        try:
            # SELECT APP
            # driver.find_element_by_link_text("Permission Set Overview").click()
            # time.sleep(4)
            driver.find_element_by_link_text("Assigned Apps").click()
            time.sleep(3)
            driver.find_element_by_link_text("Edit").click()
            time.sleep(3)
            driver.find_element_by_xpath('.//option[@title="dFarm.DemandFarm (dFarm__DemandFarm)"]').click()
            time.sleep(2)
            driver.find_element_by_class_name("rightArrowIcon").click()
            driver.find_element_by_xpath('.//input[@value="Save"]').click()
            time.sleep(4)

        except:
            pass

    def vf_pages(self):
        try:
            # ADD VF Pages
            driver.find_element_by_link_text("Permission Set Overview").click()
            time.sleep(3)
            driver.find_element_by_link_text("Visualforce Page Access").click()
            time.sleep(3)
            driver.find_element_by_link_text("Edit").click()
            time.sleep(3)

            table = [driver.find_elements_by_xpath('.//option[starts-with(@title,"dFarm")]')]

            driver.execute_script("var select = document.getElementsByClassName('dueling')[0]; "
                                  "for ( var i = 0; i < select.options.length; i++ ){ "
                                  "if(select.options[i].text.indexOf('dFarm')!=-1)" \
                                  "select.options[i].selected = true;}")

            # driver.find_element_by_xpath('.//option[starts-with(@title,"dFarm")]').click()
            driver.find_element_by_class_name("rightArrowIcon").click()
            # do stuff

            driver.find_element_by_xpath('.//input[@value="Save"]').click()

        except:
            pass

    def apex_classes(self):
        try:
            # SELECT APEX CLASSES
            driver.find_element_by_link_text("Permission Set Overview").click()
            time.sleep(3)
            driver.find_element_by_link_text("Apex Class Access").click()
            time.sleep(3)
            driver.find_element_by_link_text("Edit").click()
            time.sleep(3)

            table = [driver.find_elements_by_xpath('.//option[starts-with(@title,"dFarm")]')]

            driver.execute_script("var select = document.getElementsByClassName('dueling')[0]; "
                                  "for ( var i = 0; i < select.options.length; i++ ){ "
                                  "if(select.options[i].text.indexOf('dFarm')!=-1)" \
                                  "select.options[i].selected = true;}")

            # driver.find_element_by_xpath('.//option[starts-with(@title,"dFarm")]').click()
            driver.find_element_by_class_name("rightArrowIcon").click()
            # do stuff

            driver.find_element_by_xpath('.//input[@value="Save"]').click()

        except:
            pass

    def objectsettings(self):
        # OBJECT SETTINGS

        try:
            # driver.find_element_by_link_text("Permission Set Overview").click()
            # time.sleep(3)
            driver.find_element_by_link_text("Object Settings").click()
            time.sleep(4)
            f = open("objects.txt", 'r')
            lines = f.readlines()
            # line = line.replace("\n", "")
            cnt = 1

            for line in lines:
                line = line.replace("\n", "")
                print(type(line))
                print(line)
                print("Object Number:", cnt)
                # line = "Cases"
                time.sleep(5)
                # print(driver.find_element_by_link_text(line))
                try:
                    driver.find_element_by_link_text(line).click()
                except:
                    cnt += 1
                time.sleep(4)
                driver.find_element_by_link_text('Edit').click()
                time.sleep(2)
                table = driver.find_element_by_css_selector('div.pbBody')
                time.sleep(2)
                a = table.find_elements_by_xpath("//input[@type='checkbox']")
                print(len(a))
                print(type(a))

                if (property(table, driver.find_elements_by_xpath("//input[@type='checkbox']"))) == 'checked':
                    pass
                else:
                    try:
                        if line == 'Competitors':
                            for row in a[0:6]:
                                row.click()

                            for row in a[8:]:
                                row.click()

                        elif line == 'Engagements':
                            for row in a[0:7]:
                                row.click()
                                time.sleep(0.002)

                            for row in a[9:]:
                                row.click()
                                time.sleep(0.002)

                        elif line == 'Buying Centers':
                            for row in a[0:2]:
                                row.click()

                            for row in a[3:6]:
                                row.click()
                                time.sleep(0.002)

                            for row in a[9:]:
                                row.click()
                                time.sleep(0.002)

                        elif line=='Offerings':
                            for row in a[0:2]:
                                row.click()
                                time.sleep(0.002)

                            for row in a[3:6]:
                                row.click()
                                time.sleep(0.002)

                            for row in a[9:]:
                                row.click()
                                time.sleep(0.002)

                        elif line=='Question Sets':
                            for row in a[0:2]:
                                row.click()
                                time.sleep(0.002)

                            for row in a[3:6]:
                                row.click()
                                time.sleep(0.002)

                            for row in a[9:]:
                                row.click()
                                time.sleep(0.002)

                        else:
                            for row in a[0:4]:
                                # f = row.find_element_by_xpath("//input[@type='checkbox']")
                                # print(row)
                                # print(f)
                                row.click()

                            for row in a[6:]:
                                row.click()

                    except:
                        pass

                    finally:
                        driver.find_element_by_xpath('.//input[@value="Save"]').click()
                        f.close()
                    # driver.execute_script("var checkboxes = document.getElementsByTagName('input'); "
                    # "for (var i = 0; i < checkboxes.length; i++) { "
                    # "if (checkboxes[i].type == 'checkbox') { checkboxes[i].checked = true; }}")

                    driver.find_element_by_link_text("Object Settings").click()
                    time.sleep(3)

            cnt += 1
        finally:
            print('The script took {0} second !'.format(time.time() - startTime))
        # time.sleep(10)
        # driver.find_element_by_class_name("pageDescription").click()
        # time.sleep(2)
        # driver.find_element_by_xpath('.//input[@value="Save"]').click()'''

        # except:
        #   pass
        # finally:
        #  print ('The script took {0} second !'.format(time.time() - startTime))


if __name__ == '__main__':
    ps = PermissionSet()
    ps.log_me()
    time.sleep(3)
    ps.find_setup()
    time.sleep(3)
    ps.create_ps()
    # ps.assigned_app()
    time.sleep(3)
    # ps.vf_pages()
    # ps.apex_classes()
    # time.sleep(4)
    # time.sleep(3)
    # ps.existing_ps()
    time.sleep(3)
    ps.objectsettings()
