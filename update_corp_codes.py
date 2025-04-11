import requests
import zipfile
import xml.etree.ElementTree as ET
import json
import os

DART_API_KEY = "fc43af46c1bc915dce2fc6e156971f2569e603b3"
zip_url = f"https://opendart.fss.or.kr/api/corpCode.xml?crtfc_key={DART_API_KEY}"

# 1. 다운로드
res = requests.get(zip_url)
with open("corpCode.zip", "wb") as f:
    f.write(res.content)

# 2. 압축 해제
with zipfile.ZipFile("corpCode.zip", "r") as zip_ref:
    zip_ref.extractall(".")

# 3. XML 파싱
tree = ET.parse("CORPCODE.xml")
root = tree.getroot()

result = []
for child in root.findall("list"):
    corp_name = child.findtext("corp_name")
    corp_code = child.findtext("corp_code")
    if corp_name and corp_code:
        result.append({
            "corp_name": corp_name.strip(),
            "corp_code": corp_code.strip()
        })

# 4. 저장
with open("corp_codes.json", "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

# 5. 정리
os.remove("corpCode.zip")
os.remove("CORPCODE.xml")

print("✅ corp_codes.json 생성 완료!")


