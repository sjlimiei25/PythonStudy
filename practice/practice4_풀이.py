# practice4.py

# [1] 은행 계좌 클래스
#     BankAccount 클래스 정의
#     - 속성 : 계좌번호(account_number), 잔액(balance)
#     - 메소드 : 
#       * deposit(amount) : 입금. 잔액을 증가시킨다.
#       * withdraw(amount): 출금. 잔액을 감소시킨다. 
#                           단, 잔액이 부족하면 "잔액이 부족합니다." 출력한다.
#       * show_balance()  : 잔액 확인. 현재 잔액을 출력한다.
class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{amount}원 입금 완료. 현재 잔액: {self.balance}원")

    def withdraw(self, amount):
        if self.balance < amount:
            print("잔액이 부족합니다.")
            return
        
        self.balance -= amount
        print(f"{amount}원 출금 완료. 현재 잔액: {self.balance}원")
    
    def show_balance(self):
        print(f"계좌: {self.account_number} 잔액: {self.balance}원")


kim_bank = BankAccount("111-222", 1000)
kim_bank.deposit(500)           # 출력예) 500원 입금 완료. 현재 잔액: 1500원
kim_bank.withdraw(2000)         # 출력예) 잔액이 부족합니다.
kim_bank.show_balance()         # 출력예) 계좌 111-222 잔액: 1500원
# =====================================================================
# [2] 온라인 쇼핑몰 클래스
#     Product 클래스
#     - 속성 : 상품명(name), 가격(price), 재고(__stock)
#     - 메소드 :
#       * reduce_stock(quantity) : 구매 시 재고 감소
#       * add_stock(quantity) : 재고 추가
#       * get_stock() : 현재 재고 조회
#       * __str__() : 상품 정보 문자열로 반환
class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.__stock = stock

    def reduce_stock(self, quantity):
        if self.__stock >= quantity:
            self.__stock -= quantity
            print(f"{self.name} 재고 {quantity} 차감! 남은 수량: {self.__stock}")
        else:
            print(f"{self.name} 재고 부족!")

    def add_stock(self, quantity):
        self.__stock += quantity
        print(f"{self.name} 재고 {quantity} 추가! 남은 수량: {self.__stock}")

    def get_stock(self):
        return self.__stock
    
    def __str__(self):
        return f"{self.name} ({self.price}원 / {self.__stock}개)"
    

#     Cart 클래스
#     - 속성 : 담은 상품 목록(items) -> (Product 객체, 수량) 형태로 저장
#     - 메소드 :
#       * add_product(product, quantity) : 장바구니에 상품 추가
#       * remove_product(product_name) : 장바구니에서 상품 제거
#       * show_cart() : 장바구니 내역 출력
#       * total_price() : 장바구니 총액 계산
class Cart:
    def __init__(self):
        self.items = []   # Cart(장바구니) 객체 생성 시 리스트는 비어있음!

    def add_product(self, product, quantity):
        # 해당 제품의 재고가 개수보다 많을 경우 장바구니에 추가
        if product.get_stock() >= quantity:
            self.items.append( (product, quantity) )    # [] --> [(Product, 개수)]
            product.reduce_stock(quantity)
            print(f"{product.name} {quantity}개 장바구니에 추가")
        else:
            print(f"{product.name}은 재고 부족으로 장바구니에 담을 수 없습니다.")

    def remove_product(self, product_name):
        for index, (product, qty) in enumerate(self.items):
            if product.name == product_name:
                self.items.pop(index)   # 장바구니에 제거
                product.add_stock(qty)  # 재고 업데이트
                print(f"{product_name} 장바구니에서 제거")
                return
            
        # 장바구니에 없는 경우
        print(f"{product_name} 장바구니에 없음!")

    def total_price(self):
        '''
        total = 0
        for product, qty in self.items:
            total += product.price * qty
        return total
        '''
        return sum(product.price * qty for product, qty in self.items)
    
    def show_cart(self):
        '''
        출력예)
        장바구니 내역:
        - 노트북 (1개) : 1200000원
        - 마우스 (2개) : 60000원
        총 금액: 1260000원
        '''
        #if len(self.items) == 0:
        if not self.items:
            print("장바구니가 비었습니다.")
            return

        print("장바구니 내역:")
        for p, q in self.items:
            print(f"- {p.name} ({q}개) : {p.price*q}원")
        print(f"총 금액: {self.total_price()}원")



p1 = Product("노트북", 1200000, 5)
p2 = Product("마우스", 30000, 10)

cart = Cart()

cart.add_product(p1, 1)         # 출력예) 노트북 1개 장바구니에 추가
cart.add_product(p2, 2)         # 출력예) 마우스 2개 장바구니에 추가
cart.show_cart()                
'''
출력예)
장바구니 내역:
- 노트북 (1개) : 1200000원
- 마우스 (2개) : 60000원
총 금액: 1260000원
'''

cart.remove_product("마우스")   # 출력예) 마우스 장바구니에서 제거
cart.show_cart()
'''
출력예)
장바구니 내역:
- 노트북 (1개) : 1200000원
'''