#조건
#10시간 이상 : 휴대폰 잠금이 해제 됩니다.
#5시간 이상 : 휴대폰 30분 사용가능 합니다.
#나머지 : 휴대폰 사용이 불가능합니다.

#공부시간을 입력하세요(시간) >>>

study_time = int(input("공부시간을 입력하세요(시간) >>>"))

if study_time >= 10:
    print("휴대폰 잠금이 해제 됩니다.")
elif study_time >=5:
    print("휴대폰 30분 사용가능 합니다.")
else:
    print("휴대폰 사용이 불가능합니다.")

#문제 풀이 생략 쉬었음
