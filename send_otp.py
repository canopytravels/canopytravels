import http.client

authkey="256624Ax2u15T0ke135c3c6465"
message = "Your verification code is ##OTP##"
sender = "OTPSMS"
mobile = "+918638176825"

conn = http.client.HTTPConnection("api.msg91.com")

payload = ""

conn.request("POST", "/api/sendotp.php?template=&otp_length=&authkey=256624Ax2u15T0ke135c3c6465&message=&sender=&mobile=918638176825&otp=&otp_expiry=&email=", payload)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


