import requests
api_key="57be8f05-9ff1-464f-bfea-38de9a24b101"
base="https://api.cricapi.com/v1/currentMatches"
url=f"{base}?apikey={api_key}&offset=0"
responce=requests.get(url)
status_code=responce.status_code
raw_json=responce.json()
status_code,raw_json.get("status")
if raw_json.get("status")!="success":
    raise RuntimeError(f"api error:{raw_json}")
matches=raw_json.get("data",[])
len(matches)
sample=matches[0] if matches else{}
sample.keys(),sample.get('name'),sample.get("status"),sample.get("score")
def format_score(score_list):
    if not score_list:
        return "no score yet"
    parts=[]
    for s in score_list:
        r=s.get("r")
        w=s.get("w")
        o=s.get("o")
        parts.append(f"{r}/{w} in {o} overs")
    return " | ".join(parts)
for m in matches:
    name=m.get("name","unknown")
    status=m.get("status","unknown")
    score=format_score(m.get("score"))
    print(f"match:   {name}")
    print(f"status:  {status}")
    print(f"score:  {score}")
    print("-"*32)
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # raises for HTTP errors (4xx/5xx)
    data = response.json()
    if data.get("status") != "success":
        raise ValueError(data)
except requests.exceptions.Timeout:
    print("Request timed out. Try again or check your internet.")
except requests.exceptions.HTTPError as e:
    print("HTTP error:", e)
except Exception as e:
    print("Unexpected error:", e)
