#오픈소스프로그래밍 기말 과제 
#주식 매매손익과 비트코인 보유량을 계산하는 프로그램

#명령줄 인자 처리를 위한 sys 모듈 가져오기
import sys

def calculate_stock_profit(buy_price, quantity, sell_price, sell_fee_rate):
    """
    주식 매매 손익을 계산하는 함수

    매개변수:
        buy_price (float): 주식의 매수 가격
        quantity (int): 매수한 주식의 수량
        sell_price (float): 주식의 매도 가격
        sell_fee_rate (float): 매도 시 부과되는 수수료율 (예: 0.001는 0.1%)

    반환값:
        profit (float): 총 손익
        profit_rate (float): 수익률 (%)
    """
    # 총 매수 금액 계산
    total_buy = buy_price * quantity

    # 매도 시 발생하는 수수료 계산
    sell_fee = sell_price * quantity * sell_fee_rate

    # 총 매도 금액 계산
    total_sell = (sell_price * quantity) - sell_fee

    # 손익 계산
    profit = total_sell - total_buy

    # 수익률 계산
    profit_rate = (profit / total_buy) * 100

    return profit, profit_rate

def calculate_bitcoin_quantity(buy_price, current_price):
    """
    내가 보유한 비트코인의 개수를 계산하는 함수

    매개변수:
        buy_price (float): 비트코인 매수 가격
        current_price (float): 현재 비트코인 가격

    반환값:
        bitcoin_quantity (float): 보유 비트코인의 개수
    """

    #가격이 0이면 에러를 발생
    if current_price <= 0:
        raise ValueError("현재 비트코인 가격은 0보다 커야 합니다.")
    
    #코인 보유량 계산
    bitcoin_quantity = buy_price / current_price
    return bitcoin_quantity

def get_input_data():
    """
    사용자로부터 입력 데이터를 받아오는 함수

    반환값:
        buy_price (float): 매수 가격
        quantity (int): 매수 수량
        sell_price (float): 매도 가격
        sell_fee_rate (float): 매도 수수료율
    """
    try:
        buy_price = float(input("매수 가격을 입력하세요 (1주당): "))
        quantity = int(input("매수한 주식 수량을 입력하세요: "))
        sell_price = float(input("매도 가격을 입력하세요 (1주당): "))
        sell_fee_rate = float(input("매도 수수료율을 입력하세요 (소수로 입력, 예: 0.003): "))
        return buy_price, quantity, sell_price, sell_fee_rate
    except ValueError:
        raise ValueError("입력값이 올바르지 않습니다. 숫자를 입력해주세요.")

def get_bitcoin_data():
    """
    사용자로부터 비트코인 데이터를 받아오는 함수

    반환값:
        buy_price (float): 비트코인 매수 가격
        current_price (float): 현재 비트코인 가격
    """
    try:
        buy_price = float(input("비트코인 매수 가격을 입력하세요: "))
        current_price = float(input("현재 비트코인 가격을 입력하세요: "))
        return buy_price, current_price
    except ValueError:
        raise ValueError("입력값이 올바르지 않습니다. 숫자를 입력해주세요.")

def main_menu():
    """
    프로그램의 메인 메뉴 함수
    """
    while True:
        print("\n==== 주식 및 비트코인 계산 프로그램 ====")
        print("1. 주식 매매 손익 계산")
        print("2. 비트코인 보유량 계산")
        print("3. 종료")

        try:
            if len(sys.argv) > 1:
                # 비인터랙티브 환경에서 명령줄 인자 사용
                print("비인터랙티브 환경에서 실행 중. 명령줄 입력값 사용.")
                args = sys.argv[1:]
                choice = int(args[0])
            else:
                # 인터랙티브 환경에서 사용자 입력 받기
                choice = input("원하는 작업을 선택하세요 (1/2/3): ").strip()
                if not choice.isdigit():
                    raise ValueError("숫자를 입력해주세요.")
                #입력값을 정수로 변환
                choice = int(choice)

            if choice == 1:
                #명령줄 인자가 충분한 경우
                if len(sys.argv) > 1 and len(sys.argv) >= 5:
                    buy_price, quantity, sell_price, sell_fee_rate = map(float, sys.argv[1:5])
                else:
                    buy_price, quantity, sell_price, sell_fee_rate = get_input_data()
                profit, profit_rate = calculate_stock_profit(buy_price, quantity, sell_price, sell_fee_rate)
                print(f"\n총 손익: {profit:.2f} 원")
                print(f"수익률: {profit_rate:.2f} %")

            elif choice == 2:
                #명령줄 인자가 충분한 경우
                if len(sys.argv) > 1 and len(sys.argv) >= 3:
                    bitcoin_buy_price, bitcoin_current_price = map(float, sys.argv[1:3])
                else:
                    bitcoin_buy_price, bitcoin_current_price = get_bitcoin_data()
                bitcoin_quantity = calculate_bitcoin_quantity(bitcoin_buy_price, bitcoin_current_price)
                print(f"현재 보유 중인 비트코인 개수: {bitcoin_quantity:.10f} 개")

            elif choice == 3:
                print("프로그램을 종료합니다.")
                break

            else:
                print("올바른 번호를 선택해주세요.")
            
        #입력 오류 처리
        except (ValueError, EOFError, IndexError) as e:
            print(f"입력 에러: {e}")
            print("프로그램 종료를 원하면 3번을 입력하세요.")

#프로그램 시작점
if __name__ == "__main__":
    main_menu()
