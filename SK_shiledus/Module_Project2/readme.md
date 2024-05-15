# Blind sql injection
blind sql injection 공격은 쿼리의 결과를 참과 거짓으로만 출력하는 페이지에서 사용되는 공격으로, 출력 내용이 참과 거짓밖에 없어서 이를 이용해 데이터베이스의 내용을 추측하여 쿼리를 조종하는 공격

# 공격에 사용되는 함수
Substr, chr, ascii

# 대응방안
Prepared statement 구문을 사용하여 입력된 값은 모두 문자열로서만 처리되도록 구현하는 것이 가장 안전하다.

(하지만 여러 이유로 Prepared statement 구문을 사용하여 구현하지 못하는 상황이 있을 수 있다. 
그럴 경우 입력된 값이 개발자가 의도한 값인지 검증할 수 있는 로직을 구현하여 불필요한 특수 문자 등은 입력되지 않도록 구현해야 한다.)

에러 메시지가 출력되지 않도록 설정한다.

웹 방화벽(WAF)을 사용하여 부적절한 요청이 전송될 경우 차단한다.

# 보고서 작성
![image](https://github.com/JeonSH-Francesco/Python/assets/112309895/95d56999-d1a2-41e7-9b03-9cdc424372cd)

![image](https://github.com/JeonSH-Francesco/Python/assets/112309895/45872804-6d77-45cb-a8b0-f6f190e69746)

![image](https://github.com/JeonSH-Francesco/Python/assets/112309895/d48fb873-d485-4935-bf84-76bf05c26a77)

![image](https://github.com/JeonSH-Francesco/Python/assets/112309895/078faaf6-4fff-4ae9-b150-d156abb5c2db)

![image](https://github.com/JeonSH-Francesco/Python/assets/112309895/aec86ed2-347a-4319-8bcc-bc052960fae6)

![image](https://github.com/JeonSH-Francesco/Python/assets/112309895/58e6a13b-dec0-43e8-b24c-1af1ee4d3b3b)

![image](https://github.com/JeonSH-Francesco/Python/assets/112309895/468462d8-4e4c-41aa-a449-5c1fee8c165c)

## 실행 영상 추가
https://github.com/JeonSH-Francesco/Python/assets/112309895/442830c3-47e9-46d9-8bd8-ebd7787bb83e

