from selenium import webdriver
from time import sleep
import csv

class Bot:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://innovationlabs.harvard.edu/ventures/venture-teams/");
        sleep(4);

    def run(self):
        self._load_all()
        companies = self._get_companies()
        with open("output.csv", "w", newline = "") as f:
            writer = csv.writer(f)
            writer.writerows(companies)

    def _load_all(self):
        div_box = self.driver.find_element_by_xpath('//div[@class=\"facetwp-template\"]')
        sleep(3)
        last_ht, ht = 0, div_box.size['height']
        print(last_ht, ht);
        while (last_ht != ht):
            last_ht = ht;
            tmp = self.driver.find_elements_by_xpath('//button[@class=\"fwp-load-more\"]');
            if (len(tmp) == 0):
                break;
            button = self.driver.find_element_by_xpath('//button[@class=\"fwp-load-more\"]');
            button.click();
            sleep(2)
            ht = div_box.size['height']
            print(last_ht, ht)

        print("all loaded");
        sleep(5)
        #limit = 130
    
    def _get_companies(self):
        div_box = self.driver.find_element_by_xpath('//div[@class=\"facetwp-template\"]')
        window_shades = div_box.find_elements_by_xpath('//div[@class=\"window-shade\"]')
        companies = []
        for entry in window_shades:
            txt = entry.text
            contents = txt.split('\n');
            hdr = contents[0];
            txt = "".join(contents[1:])
            companies.append([hdr, txt])
        return companies

mybot = Bot()
sleep(3)
mybot.run()
