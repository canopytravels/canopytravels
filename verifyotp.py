import http.client

conn = http.client.HTTPSConnection("api.msg91.com")

payload = ""

headers = { 'content-type': "application/x-www-form-urlencoded" }

conn.request("POST", "/api/verifyRequestOTP.php?authkey=256624Ax2u15T0ke135c3c6465&mobile=918638176825&otp=7496", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))

## TO CONVERT string response to json
#import json
#jsob = json.loads(data)
##**********************************
