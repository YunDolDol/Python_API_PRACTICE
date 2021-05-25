# API 활용을 위한 라이브러리 및 헤더파일 불러오기
from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json
from datetime import datetime
from requests.api import get

# API 소개 문구
print("이 프로그램은 서울특별시 내 스쿨존 교통사고 건수와 사망 인원수를 알려주는 API입니다.\n")
print("입력할 해당 년도 및 서울특별시 대표 2군구 코드 안내입니다.\n")

with open ("secret.json") as f: 
    # secret 변수에 json 내용 저장 
    secret = json.loads(f.read())

# 필수 정보값들을 input으로 입력받음
input_year = input("17 ~ 18년 사이의 해당 년도를 입력하세요 (20YY 형식): ")
input_guGun = input("서울특별시 대표 2군구 코드를 입력하세요 (강서구: 500, 구로구 530): ")

# API URL을 불러오는 코드
url = 'http://apis.data.go.kr/B552061/schoolzoneChild/getRestSchoolzoneChild'

# API 파라미터를을 나열 & 사용 / URL뒤에 '?'로 구분하여
# 파라미터들을 나열 및 활용
# queryParams는 단순 파라미터 변수 이름이며, 그 뒤에가 더 중요하다.
# '?'로 URL와 파라미터 값을 구분한다.
# 파라미터 값은 quote_plus로 필수 파라미터 값을 부른다.
queryParams = '?' + urlencode(
    {
    quote_plus('ServiceKey'): secret["SECRET_KEY"],
    quote_plus('searchYearCd'): input_year,
    quote_plus('siDo'): '11',
    quote_plus('guGun'): input_guGun,
    quote_plus('type'): 'json',
    quote_plus('numOfRows'): '10',
    quote_plus('pageNo'): '1'
    }
)

# requests.get()으로 API 속 필요한 파라미터의 데이터를
# 불러와(requests)변수 get_data에 저장
# 한글로 받아온 데이터를 다시 풀어줌
get_data = requests.get(url + unquote(queryParams))

#변수 res에 get_data의 json 타입을 저장
res = get_data.json()

# res의 딕셔너리 키 'resultMsg'의 키값을 불러 냄.
if (input_guGun == '500' and input_year == '2017') :
    print('2017년도 강서구 스쿨존 내 교통사고 건수는 ' + str(res['items']['item'][0]['occrrnc_cnt']) + '건 입니다. '
    + '사망자수는 ' + str(res['items']['item'][0]['dth_dnv_cnt']) + '명 입니다.')
elif (input_guGun == '500' and input_year == '2018') : 
    print('2018년도 강서구 스쿨존 내 교통사고 건수는 ' + str(res['items']['item'][0]['occrrnc_cnt']) + '건 입니다. '
    + '사망자수는 ' + str(res['items']['item'][0]['dth_dnv_cnt']) + '명 입니다.')
elif (input_guGun == '530' and input_year == '2017') : 
    print('2017년도 구로구 스쿨존 내 교통사고 건수는 ' + str(res['items']['item'][0]['occrrnc_cnt']) + '건 입니다. '
    + '사망자수는 ' + str(res['items']['item'][0]['dth_dnv_cnt']) + '명 입니다.')
elif (input_guGun == '530' and input_year == '2018') : 
    print('2018년도 구로구 스쿨존 내 교통사고 건수는 ' + str(res['items']['item'][0]['occrrnc_cnt']) + '건 입니다. '
    + '사망자수는 ' + str(res['items']['item'][0]['dth_dnv_cnt']) + '명 입니다.')