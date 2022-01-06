# = : 할당 연산자 : 오른쪽에 있는 데이터를 왼쪽에 있는 변수에 저장한다.

# 변수명 짓기 규칙
# 데이터를 표현할 수 있는 이름으로 짓는다.
# 문자부터 시작해야한다.
# 대소문자는 구분한다.
# _로 시작할 수있다.
# 미리 예약된 키워드는 사용할 수 없다.

# 마스터 이 챔피언 데이터를 변수에 저장
name = "마스터이"
level = 5
health = 800
attack = 90
print(name, level, health, attack)

# 변수에 저장된 데이터를 변경하기
level = level + 1
health = health = 50
attack = attack = 10
print(name, level, health, attack)
