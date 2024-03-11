guest = ""
beverage_type = ["hot","iced"]
drinks_menu = {
    "Americano":{"options":beverage_type,"price":5000},
    "Cafe_Latte":{"options":beverage_type,"price":6000},
    "Einspenner":{"options":"icedonly","price":7000},
    "Chocolate_Latte":{"options":beverage_type,"price":6000},
    "Peach_Iced_Tea":{"options":"icedonly","price":6000},
    "Earl_Grey":{"options":beverage_type,"price":5000}
    }
desserts_menu = {
    "Scone":{"count":3,"price":5000},
    "Croissant":{"count":10,"price":5000},
    "Tiramisu":{"count":7,"price":6000},
    "Strawberry_cake":{"count":8,"price":7000},
    "Chocolate_cake":{"count":8,"price":7000}
}
customer_order = {}
order_count =0
total_price=0
bell = [1,2,3,...,30]
count_customer=0


revenue=0
cash = 0
card = 0

event_member = {"Emily":123456,"Ethan":123457,"Olivia":123458,"Liam":123459,"Sophia":123460}
event_code = []

def order_bell_func():
  while True:
    order_bell = int(input("앞쪽에 있는 진동벨 번호를 입력해주세요.[1번-30번]"))
    if order_bell<1 or order_bell>30:
      order_bell = int(input("[1번에서 30번사이로 다시 입력해주세요."))     
      break
    else:
      num = order_bell
      return num
      


def cafe_system():
  while True:
    print("안녕하세요 가구카페 [가페]입니다.")
    print("*"*50)
    order_type = input("매장이나 테이크아웃을 선택해주세요.[store/takeout/종료=q]").lower()
    if order_type =='q':break     
    print(f"음료 : {list(drinks_menu)}")
    print("디저트 : {}".format(list(desserts_menu)))
    while True:
      order_menu = input("메뉴를 선택해주세요.").capitalize()
      if order_menu not in (list(drinks_menu) and list(desserts_menu)):
        order_menu = input("메뉴를 다시 선택해주세요.").capitalize()
        if order_menu in (list(drinks_menu) and list(desserts_menu)): break
      else:
        break            
    if order_menu in list(drinks_menu):       # 메뉴가 음료일 때
      order_option = input(f"{order_menu}의 옵션을 선택해주세요.{beverage_type}")
      customer_order = order_menu,order_option    # 메뉴와 옵션을 고객주문에 저장
      total_price = drinks_menu[order_menu]["price"]    # 주문메뉴의 금액을 결제총금액에 저장
    elif order_menu in list(desserts_menu):     # 메뉴가 디저트일 때
      order_count = int(input(f"{order_menu}의 수량을 선택해주세요."))  
      if desserts_menu[order_menu]["count"]<order_count:  # 주문메뉴의 수량이 디저트메뉴의 재고수량 보다 적어야함
        print("재고가 부족합니다. {}개 까지 주문 가능합니다.".format(desserts_menu[order_menu]["count"]))
        continue
      customer_order=order_menu,order_count   # 주문메뉴와 수량을 고객주문에 저장
      total_price = desserts_menu[order_menu]["price"]*order_count    # 총금액은 디저트메뉴 금액과 주문메뉴 수량을 곱함
    else:
      order_bell = input("메뉴를 다시 입력해주세요")
    print(customer_order)

    order_bell = order_bell_func()

    payment = input("결제방법을 선택해주세요.[Card/Cash]")  # 예외 다른결제이용
    try:
      if payment=="cash":
        cash = total_price
        print(f"현금 정산: {cash}")
      else:
        card = total_price
        print(f"현금 정산: {card}")
    except :
        print("결제방법이 다릅니다.")
    # #### 결제금액
    print(f"총 금액은 {total_price}원입니다.")

    # #### 결제완료
    if order_menu in list(drinks_menu):
      print(f"결제가 완료되었습니다.\n주문하신 {order_menu}[{order_option}]가 준비되면 진동벨{order_bell}로 불러드리겠습니다.")
    else:
      print(f"결제가 완료되었습니다.\n주문하신 {order_menu}[{order_count}]가 준비되면 진동벨{order_bell}로 불러드리겠습니다.")
    # ## 영수증
    print("-"*50)
    print(order_type+"\t"+str(order_bell))
    print("상품명\t단가\t수량\t금액")
    print(order_menu,"\tprice","\tcount\t",total_price)
    print("-"*50)
    print("")

    ## 방문객 / 매출
    # count_customer+=1
    cash = 0
    card = 0
    revenue = cash + card

cafe_system()
