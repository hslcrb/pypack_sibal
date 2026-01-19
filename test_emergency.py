import sibal
import time

print("이 코드는 3초 후에 에러가 발생합니다. 준비하세요!")
for i in range(3, 0, -1):
    print(f"{i}...")
    time.sleep(1)

# 고의적인 에러 발생
raise Exception("SIBAL ERROR OCCURRED!!!")
