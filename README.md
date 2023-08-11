# 대한민국 기상 특보 API

특보구역 코드를 기반으로 해당 구역에 내려진 특보를 조회하기 위해 발표시각(From), 발표시각(To), 특보구역코드, 특보종류의 조회 조건으로 지점번호, 발표시각(년월일시분), 발표번호(월별), 특보구역코드, 구역명, 특보종류, 특보강도, 특보발표코드, 발효시각, 발효해제시각, 전체특보해제시각, 취소구분의 정보를 조회하는 스크립트 입니다.

Powe by [대한민국 기상청 API](http://apis.data.go.kr/1360000/WthrWrnInfoService/getPwnCd "사용 API 링크")

## 사용법

1. [공공데이터 포털](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000415 "공공 데이터 포털로 연결됩니다.")에 접속하여 API 키를 발급받습니다.
2. 개인 API 키를 `api_key.txt`파일을 생성하여 붙여 넣습니다.
3. 스크립트를 실행하여 기상 특보 정보를 불러옵니다.

## 요구사항

- python 3.X
- `request` 라이브러리

## 매개변수 

* `serviceKey`: 발급받은 API 키.
* `pageNo`: 결과의 페이지 번호.
* `numOfRows`: 페이지 당 결과 수.
* `dataType`: 데이터 유형 (XML 또는 JSON). Defalt = XML
* `fromTmFc`: 조회 시작 시간 (YYYYMMDD), 입력하지 않으면 현재 날짜.
* `toTmFc`: 조회 종료 시간 (YYYYMMDD), 입력하지 않으면 현재 날짜.
* `areaCode`: 특정 지역을 위한 지역 코드.
* `warningType`: 경보 유형 (1-강풍, 2-비, 3-한파 등).
* `stnId`: 지점 코드.

더 많은 정보는 [API 문서-29페이지](https://github.com/mushroomsando/special-weather-report/blob/fd2699728cb1a1b54fddcb5455ad5c2732945e26/official_document/%EA%B8%B0%EC%83%81%EC%B2%AD21_%EA%B8%B0%EC%83%81%ED%8A%B9%EB%B3%B4%20%EC%A1%B0%ED%9A%8C%EC%84%9C%EB%B9%84%EC%8A%A4_%EC%98%A4%ED%94%88API%ED%99%9C%EC%9A%A9%EA%B0%80%EC%9D%B4%EB%93%9C.docx)를 참조하세요.

## 라이선스

이 프로젝트는 [GPL-3.0 license](https://github.com/mushroomsando/special-weather-report/blob/main/LICENSE) 에 따라 라이선스가 부여됩니다.
