import requests
from bs4 import BeautifulSoup

keyword= 'camera'
#page_number = '5'
results = []

headers = {
    'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:80.0) Gecko/20100101 Firefox/80.0'
}

for i in range(1,11):
    #r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw='+keyword, headers = headers)
    r = requests.get('https://www.ebay.com/sch/i.html?_from=R40&_nkw='+keyword+'&_pgn='+str(i), headers=headers)
    print('r.status_code=', r.status_code)

    soup = BeautifulSoup(r.text, 'html.parser')

    '''
    items = soup.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
    for item in items:
        print('item=', item.text)

    prices = soup.select('.s-item__price')
    for price in prices:
        print('price=',price.text)
    '''
    #extract the 'item boxes' rather than just the titles/prices

    
    boxes = soup.select('li.s-item--watch-at-corner.s-item')
    for box in boxes:
        #print('------')
        result = {}
        titles = box.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__link > .s-item__title')
        for title in titles:
            #print('title=', title.text)
            result['title'] = title.text
        states = box.select('li.s-item--watch-at-corner.s-item > .clearfix.s-item__wrapper > .clearfix.s-item__info > .s-item__subtitle > .SECONDARY_INFO')
        for state in states:
            #print('state=', state.text)
            result['state'] = state.text
        prices = box.select('.s-item__price')
        for price in prices:
            #print('price=',price.text)
            result['price'] = price.text
        #print('result=', result)
        results.append(result)

    print('len(results)=', len(results))

#output to a json file

import json
j = json.dumps(results)
with open('items.json', 'w') as f:
    f.write(j)
#print('j=', j)




