def insertData(custlist,page):
    customer={'name':'','gender':'',"email":'',"birthyear":''}
    customer['name'] = input('이름 >>> ')

    while True:
        customer['gender'] = input('성별(M,F) >>> ').upper()
        if customer['gender'] in ('M','F'):
            break

    while True:
        customer['email'] = input('email >>> ')
        check = 0
        for item in custlist:
            if item['email'] == customer['email']:
                check=1
                break
        if check == 0 :
            break  
        print('중복되는 이메일이 있습니다.')  

    while True:
        customer['birthyear'] = input('태어난 연도(4자리) >>> ')
        if customer['birthyear'].isdigit() and len(customer['birthyear']) == 4 :
            customer['birthyear'] = int(customer['birthyear'])
            break

    print(customer)
    custlist.append(customer)
    print(custlist)
    page = len(custlist)-1
    return page

def curView(custlist,page):
    if page >= 0:
        print('현재 페이지는 {}페이지 입니다.'.format(page+1))
        print(custlist[page])
    else:
        print('입력된 내용이 없습니다.') 

def preView(custlist,page):
    if page <= 0:
        print('첫번째 페이지 입니다.')
        print(custlist[page])
    else:
        page -= 1
        print('현재 페이지는 {}페이지 입니다.'.format(page+1))
        print(custlist[page])
    return page

def nextView(custlist,page):
    if page >= len(custlist)-1:
        print('마지막 페이지입니다.')
        print(custlist[page])
    else:
        page += 1
        print("현재 페이지는 {}쪽 입니다".format(page + 1))
        print(custlist[page])
    return page

def updateData(custlist,page):
    while True:
        choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ') # 이메일 존재 여부 체크 필요
        idx=-1
        for i in range(0,len(custlist)):
            if custlist[i]['email'] == choice1:
                idx=i
        if idx==-1:
            print('등록되지 않은 이메일입니다.')       
            break
                    
        choice2=input('''
        다음 중 수정하실 정보를 골라주세요 
                name, gender, birthyear
        (수정할 정보가 없으면 'exit' 입력)
        ''')
        if choice2 in ('name','gender','birthyear'):
            custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
            break
        elif choice2 =='exit':
            break
        else:
            print('존재하지 않는 정보입니다.')
            break 

def deleteData(custlist,page):
    email = input('삭제하려는 고객의 이메일을 입력하세요 >>> ').strip()
    delok = 0
    for idx,i in enumerate(custlist):
        if i['email'] == email:
            data = custlist.pop(idx)
            print('{}님의 정보가 삭제되었습니다.'.format(data['name']))
            delok=1
            break
    if delok == 0:
        print('등록되지 않은 이메일입니다.')
    print(custlist)
    page = len(custlist)-1
    return page