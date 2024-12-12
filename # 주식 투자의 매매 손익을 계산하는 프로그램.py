# 주식 투자의 매매 손익을 계산하는 프로그램
# 이 프로그램은 사용자가 매수 가격, 매수 수량, 매도 가격, 매도다수수료를 입력하면
# 최종적인 손익과 수익률을 계산한다.

def calculate_stock_profit(buy_price, quantity, sell_price, sell_fee_rate):
    """
    주식 매매 손익을 계산하는 함수

    매개변수:
        buy_price (float): 주식의 매수 가격
        quantity (int): 매수한 주식의 수량
        sell_price (float): 주식의 매도 가격
        sell_fee_rate (float): 매도 시 부과되는 수수료율 (예: 0.003는 0.3%)

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

if __name__ == "__main__":
    print("주식 매매 손익 계산 프로그램")

    try:
        # 사용자 입력 데이터 가져오기
        buy_price, quantity, sell_price, sell_fee_rate = get_input_data()

        # 손익 계산
        profit, profit_rate = calculate_stock_profit(buy_price, quantity, sell_price, sell_fee_rate)

        # 결과 출력
        print(f"\n총 손익: {profit:.2f} 원")
        print(f"수익률: {profit_rate:.2f} %")

    except ValueError as e:
        print(e)

    except OSError:
        print("입출력 환경에서 문제가 발생했습니다. 환경 설정을 확인하세요.")
