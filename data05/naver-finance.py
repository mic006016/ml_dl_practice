def get_finance_data(code):
    from bs4 import BeautifulSoup
    from urllib import request
    import pandas as pd
    import datetime

    con2 = request.urlopen('https://finance.naver.com/item/main.naver?code=' + code) # 005930
    # print(con2.status)
    doc2 = BeautifulSoup(con2, 'html.parser')

    # 회사명 추출
    title_list = doc2.select('.wrap_company>h2>a')
    # print(title_list)
    title = title_list[0].text.strip()
    print(title)

    # 코드 추출
    code_list = doc2.select('span.code')
    code = code_list[0].text.strip()
    print(code)

    # 시가 추출
    price_list = doc2.select('div.today span.blind')
    price_1 = price_list[0].text.strip()
    price_today = int(price_1.replace(',', ''))
    print(price_today)

    # 전일시가 추출
    last_price_list = doc2.select('td.first span.blind')
    price_2 = last_price_list[0].text.strip()
    price_yes = int(price_2.replace(',', ''))
    print(price_yes)

    # 최고가 추출
    high_price_list = doc2.select('div.rate_info table.no_info em.no_up>span.blind')
    price_3 = high_price_list[0].text.strip()
    price_high = int(price_3.replace(',', ''))
    print(price_3)

    # 하나의 리스트로 묶자.
    row = [code, title, price_today, price_yes, price_high]
    print(row)