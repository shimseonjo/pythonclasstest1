import sys

class Customer:
    def __init__(self):
        self.custlist=[{'name': 'hong', 'gender': 'M', 'email': 'hong@gmail.com', 'birthyear': 2000},
          {'name': 'kim', 'gender': 'F', 'email': 'kim@gmail.com', 'birthyear': 2001},
          {'name': 'lee', 'gender': 'M', 'email': 'lee@gmail.com', 'birthyear': 2002},
          {'name': 'han', 'gender': 'F', 'email': 'han@gmail.com', 'birthyear': 2003}]
        self.page=3
        while True:
            self.exe(self.display())

    def display(self):
        choice=input('''
    다음 중에서 하실 일을 골라주세요 :
    I - 고객 정보 입력
    C - 현재 고객 정보 조회
    P - 이전 고객 정보 조회
    N - 다음 고객 정보 조회
    U - 고객 정보 수정
    D - 고객 정보 삭제
    Q - 프로그램 종료
    ''').upper()
        return choice  
    
    def exe(self,choice):
        if choice=="I":        
            print("고객 정보 입력")
            self.insertData()
        elif choice=="C":
            print("현재 고객 정보 조회")
            self.curView()
        elif choice == 'P':
            print("이전 고객 정보 조회")
            self.preView()
        elif choice == 'N':
            print("다음 고객 정보 조회")
            self.nextView()
        elif choice=='D':
            print("고객 정보 삭제")
            self.deleteData()
        elif choice=="U": 
            print("고객 정보 수정")
            self.updateData()
        elif choice=="Q":
            print("프로그램 종료")
            sys.exit()
            

    def insertData(self):
        customer={'name':'','gender':'',"email":'',"birthyear":''}
        customer['name'] = input('이름 >>> ')

        while True:
            customer['gender'] = input('성별(M,F) >>> ').upper()
            if customer['gender'] in ('M','F'):
                break

        while True:
            customer['email'] = input('email >>> ')
            check = 0
            for item in self.custlist:
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
        self.custlist.append(customer)
        print(self.custlist)
        self.page = len(self.custlist)-1


    def curView(self):
        if self.page >= 0:
            print('현재 페이지는 {}페이지 입니다.'.format(self.page+1))
            print(self.custlist[self.page])
        else:
            print('입력된 내용이 없습니다.') 

    def preView(self):
        if self.page <= 0:
            print('첫번째 페이지 입니다.')
            print(self.custlist[self.page])
        else:
            self.page -= 1
            print('현재 페이지는 {}페이지 입니다.'.format(self.page+1))
            print(self.custlist[self.page])


    def nextView(self):
        if self.page >= len(self.custlist)-1:
            print('마지막 페이지입니다.')
            print(self.custlist[self.page])
        else:
            self.page += 1
            print("현재 페이지는 {}쪽 입니다".format(self.page + 1))
            print(self.custlist[self.page])

    def updateData(self):
        while True:
            choice1=input('수정하시려는 고객 정보의 이메일을 입력하세요 : ') # 이메일 존재 여부 체크 필요
            idx=-1
            for i in range(0,len(self.custlist)):
                if self.custlist[i]['email'] == choice1:
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
                self.custlist[idx][choice2]=input('수정할 {}을 입력하세요 :'.format(choice2))
                break
            elif choice2 =='exit':
                break
            else:
                print('존재하지 않는 정보입니다.')
                break 

    def deleteData(self):
        email = input('삭제하려는 고객의 이메일을 입력하세요 >>> ').strip()
        delok = 0
        for idx,i in enumerate(self.custlist):
            if i['email'] == email:
                data = self.custlist.pop(idx)
                print('{}님의 정보가 삭제되었습니다.'.format(data['name']))
                delok=1
                break
        if delok == 0:
            print('등록되지 않은 이메일입니다.')
        print(self.custlist)
        self.page = len(self.custlist)-1


Customer()