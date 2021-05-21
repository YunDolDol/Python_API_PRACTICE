from urllib.request import urlopen
from urllib.parse import urlencode, unquote, quote_plus
import requests
import json
from datetime import datetime
from requests.api import get

print("이 프로그램은 서울특별시 내 스쿨존 사망사고 건수와 사망 인원수를 알려주는 API입니다.\n")
print("입력할 해당 년도 및 서울특별시 대표 2군구 코드 안내입니다.\n")

input_year = input("17 ~ 18년 사이의 해당 년도를 입력하세요 (20YY 형식): ")
input_guGun = input("서울특별시 대표 2군구 코드를 입력하세요 (강서구: 500, 구로구 530): ")

url = 'http://apis.data.go.kr/B552061/schoolzoneChild/getRestSchoolzoneChild'

queryParams = '?' + urlencode(
    {
    quote_plus('ServiceKey'): 'DW5bb4kcJgB%2F2VzW7kgDBQd%2BFXpN6iDamy2pDMMogOI18F7Ip6p3qstIzZsp5u0rGvit93DEWWHWIc3HuZuZ6A%3D%3D',
    quote_plus('searchYearCd'): input_year,
    quote_plus('siDo'): '11',
    quote_plus('guGun'): input_guGun,
    quote_plus('type'): 'json',
    quote_plus('numOfRows'): '10',
    quote_plus('pageNo'): '1'
    }
)

get_data = requests.get(url + unquote(queryParams))

res = get_data.json()




print(res)