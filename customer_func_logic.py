import customer_func as cf

custlist=[{'name': 'hong', 'gender': 'M', 'email': 'hong@gmail.com', 'birthyear': 2000},
          {'name': 'kim', 'gender': 'F', 'email': 'kim@gmail.com', 'birthyear': 2001},
          {'name': 'lee', 'gender': 'M', 'email': 'lee@gmail.com', 'birthyear': 2002},
          {'name': 'han', 'gender': 'F', 'email': 'han@gmail.com', 'birthyear': 2003}]
page=3

while True:
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

    if choice=="I":        
        print("고객 정보 입력")
        page = cf.insertData(custlist,page)

    elif choice=="C":
        print("현재 고객 정보 조회")
        cf.curView(custlist,page)
        
    elif choice == 'P':
        print("이전 고객 정보 조회")
        page = cf.preView(custlist,page)
    elif choice == 'N':
        print("다음 고객 정보 조회")
        page = cf.nextView(custlist,page)
    elif choice=='D':
        print("고객 정보 삭제")
        page = cf.deleteData(custlist,page)
    elif choice=="U": 
        print("고객 정보 수정")
        cf.updateData(custlist,page)
    elif choice=="Q":
        print("프로그램 종료")
        break
