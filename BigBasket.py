import schedule
import time
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import date
from openpyxl import Workbook
def a():


    print('Meet')
    url = "https://www.bigbasket.com/custompage/getsearchdata/?slug=fresh+vegetable&type=deck"

    # Step 1 : Get the html Here URL link gives us fresh vegetable's
    r = requests.get(url)
    bsobj = r.content

    soup = BeautifulSoup(bsobj, 'html.parser')
    #print(soup.prettify())


    # Get json file's data from BigBasket
    comp = json.loads(r.text)
    #print(comp)


    # Here product name is written in tab info dictionary
    comp = comp['json_data']
    comp = comp['tab_info']
    #print(comp)


    a = []
    for i in comp[0]['product_info']['products']:
        a.append(i)
    #print(a)


    name = []
    mrp = []
    sp = []
    w = []
    for j in a:
        name.append(j['p_desc'])
        mrp.append(j['mrp'])
        sp.append(j['sp'])
        w.append(j['w'])
    # print(name)
    # print(mrp)
    # print(sp)
    # print(w)


    #All data shown in table form
    bigBas = {'Product_Name': name, 'MRP': mrp, 'Special_Price': sp, 'Weight': w}
    df = pd.DataFrame.from_dict(bigBas)
    #print(df)


    # Convert the dataframe to  Excel

    today = date.today()
    lc3 = today.strftime("%b-%d-%Y")
    df.to_excel(r'E:\FreshVeg_BB_'+lc3+'.xlsx')



schedule.every().day.at("00:00").do(a)

while 1:
    schedule.run_pending()
    time.sleep(1)