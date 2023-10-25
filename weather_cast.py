#import all the modules
try:
    import requests
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'request' module:Install it")
    exit()
try:    
    from bs4 import BeautifulSoup
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'BeautifulSoup' module:Install it")
    exit()
try:
    from lxml import etree
except (Exception, TypeError, AttributeError) as e:
     print("You dont have 'lxml' module:Install it")
     exit()
try:
    import argparse
except (Exception, TypeError, AttributeError) as e:
    print("You dont have 'argparse' module:Install it")



#check your optional input in argparse 
def check_crieria(co,ci,t,p,h,option):
    if option==True:
        print(f"The current temperature in {ci}, {co} is: {t}\nPressure: {p}\nHumidity: {h}")
    elif option=='t':
        print(f"The current Temperature in {ci}, {co} is: {t}")
    elif option=='p':
        print(f"The current Pressure in {ci}, {co} is:  {p}")
    elif option=='h':
        print(f"The current Humadity in {ci}, {co} is:  {h}")
    else:
        print('Wrong option')


def main():
    #parsing the information
    parser = argparse.ArgumentParser()
    parser.add_argument("country", type=str,
                        help="Enter the country")
    parser.add_argument("city", type=str,
                        help="Enter the city")
    parser.add_argument('-o','--optional',default=True, help='Choose necessary option')
    args = parser.parse_args()
    country1 = args.country.lower()
    city1 =args.city.lower()
    option=args.optional

    #Request the page of wheahercast
    page_html = requests.get(f"https://www.timeanddate.com/weather/{country1}/{city1}")
    
    #Get the page on html format
    soup = BeautifulSoup(page_html.content, "html.parser")
    
    #Getting able to take information with xpath
    dom = etree.HTML(str(soup))
    
    #Getting information of temperature with class of it
    temperature_element = soup.find("div", class_="h2")


    try:
        #Getting informatin of humadity and pressure with xpath of it  
        pressure = dom.xpath('/html/body/div[5]/main/article/section[1]/div[2]/table/tbody/tr[5]/td')[0].text
        humidity = dom.xpath('/html/body/div[5]/main/article/section[1]/div[2]/table/tbody/tr[6]/td')[0].text
        temperature = temperature_element.text.strip()

    except (Exception) as e:
        print("There is no such data in the database:\nPlease try again")
        exit()
    #Working function with all information    
    check_option=check_crieria(country1,city1,temperature,pressure,humidity,option)


if __name__=='__main__':
    main()
