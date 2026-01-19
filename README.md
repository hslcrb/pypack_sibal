# SIBAL (씨발) - Python Emergency Package

이 패키지는 당신의 파이썬 코드가 에러가 났을 때, 터미널을 광란의 도가니로 만들고 사이렌 소리를 울려 비상사태임을 알립니다.

## 설치 방법 (Installation)

```bash
pip install .
```

## 사용 방법 (Usage)

코드 최상단에 `import sibal` 한 줄만 추가하면 됩니다.

```python
import sibal

# 여기에서 에러가 발생하면...
print(1 / 0)
```

## 주요 기능 (Features)

1.  **무지개 광란 (Rainbow Madness)**: 터미널이 화려한 무지개 색상과 비상 메시지로 뒤덮입니다.
2.  **사이렌 소리 (Siren Sound)**: 스피커에서 "이용이용" 하는 사이렌 소리가 울려 퍼집니다 (Linux/macOS 지원).
3.  **무한 루프 (Infinite Loop)**: 터미널을 닫거나 프로세스를 강제 종료하기 전까지는 멈추지 않습니다.

## 경고 (Warning)

*   공공장소나 조용한 사무실에서 사용 시 주변의 시선을 한 몸에 받을 수 있습니다.
*   심장이 약하신 분들은 사용을 자제해 주세요.
*   이 패키지는 정말로 '씨발' 소리가 절로 나오게 설계되었습니다.

---
Created by Rheehose (Rhee Creative)  
Copyright (c) 2008-2026 Rheehose. Licensed under the MIT License.  
Official Website: [rheehose.com](https://rheehose.com)
