# 한 문제 최소 30분 정도 고민하면 좋을 듯

# 사용자
# 구독자 수
# 수익창출 가능 여부
# 1000명 이상 가능

input_user = int(input("현재 구독자 수를 입력하세요>>>"))

if input_user >= 1000:
    print("수익 창출이 가능합니다!")
else:
    print("수익 창출이 불가능합니다.")

#문제 풀이
sub_count = input("현재 구독자 수를 입력하세요 >>>")
print(sub_count) 
# 한 번에 코드를 많이 짜는 것 보다 확인하면서 진행하는 걸 권장한다.

if sub_count >= 1000:
    print("수익창출이 가능합니다!")
#TypeError: '>=' not supported between instances of 'str' and 'int'
#스트링과 정수형 비교가 불가능하다는 오류. int로 감싸줌으로 해결
else:
    print("수익창출이 불가능합니다!")
    