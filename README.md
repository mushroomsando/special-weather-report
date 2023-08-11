# 대한민국 기상 특보 API

특보구역 코드를 기반으로 해당 구역에 내려진 특보를 조회하기 위해 발표시각(From), 발표시각(To), 특보구역코드, 특보종류의 조회 조건으로 지점번호, 발표시각(년월일시분), 발표번호(월별), 특보구역코드, 구역명, 특보종류, 특보강도, 특보발표코드, 발효시각, 발효해제시각, 전체특보해제시각, 취소구분의 정보를 조회하는 스크립트 입니다.

Powe by [대한민국 기상청 API](http://apis.data.go.kr/1360000/WthrWrnInfoService/getPwnCd "사용 API 링크")

## 사용법

1. [공공데이터 포털](https://www.data.go.kr/tcs/dss/selectApiDataDetailView.do?publicDataPk=15000415 "공공 데이터 포털로 연결됩니다.")에 접속하여 API 키를 발급받습니다.
2. 개인 API 키를 `api_key.txt`파일을 생성하여 붙여 넣습니다.
3. [특보 정보 데이터](https://github.com/mushroomsando/special-weather-report/blob/39d874e709d1955a46eeec5bc9dc1b03c0c7fa5b/alret_info.json)를 다운받아 `alert_info.json`파일로 저장합니다.
4. `get_raw_data`함수에 다음과 같은 파라메터를 전달하여 `raw` 데이터를 반환받습니다.

   ```abc
   get_raw_data(service_key = open("api_key.txt", "r"), areacode = 조회하고자 하는 위치, branchCod = 조회하고자 하는 위치)
   ```

   *`warningType`, `fromTime`, `toTime` 파라메터는 필요에 따라 전달*
5. `extract_weather_info`함수에 `get_raw_data`에서 반환받은 `raw`데이터를 전달합니다.

## 요구사항

- python 3.X
- `request` 라이브러리
- `json` 라이브러리

## 참고문서

* [API 문서-29페이지](https://github.com/mushroomsando/special-weather-report/blob/fd2699728cb1a1b54fddcb5455ad5c2732945e26/official_document/%EA%B8%B0%EC%83%81%EC%B2%AD21_%EA%B8%B0%EC%83%81%ED%8A%B9%EB%B3%B4%20%EC%A1%B0%ED%9A%8C%EC%84%9C%EB%B9%84%EC%8A%A4_%EC%98%A4%ED%94%88API%ED%99%9C%EC%9A%A9%EA%B0%80%EC%9D%B4%EB%93%9C.docx)
* [특보구역 코드 데이터](https://github.com/mushroomsando/special-weather-report/blob/39d874e709d1955a46eeec5bc9dc1b03c0c7fa5b/official_document/%EA%B8%B0%EC%83%81%EC%B2%AD21_%EA%B8%B0%EC%83%81%ED%8A%B9%EB%B3%B4%20%EC%A1%B0%ED%9A%8C%EC%84%9C%EB%B9%84%EC%8A%A4_%EC%98%A4%ED%94%88API%ED%99%9C%EC%9A%A9%EA%B0%80%EC%9D%B4%EB%93%9C_%ED%8A%B9%EB%B3%B4%EA%B5%AC%EC%97%AD%EC%BD%94%EB%93%9C%EC%95%88%EB%82%B4(210715).xlsx)

## 라이선스

이 프로젝트는 [GPL-3.0 license](https://github.com/mushroomsando/special-weather-report/blob/main/LICENSE) 에 따라 라이선스가 부여됩니다.
