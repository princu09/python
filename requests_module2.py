import requests
r = requests.get("https://financialmodelingprep.com/api/company/price/AAPL")
print(r.text)
print("\nhttp status code\n")
print(r.status_code)

# url = "www.something.com"
# data = {
#     "p1":4,
#     "p2":8
# }
# r2 = requests.post(url=url, data=data)


# -------------------------Note------------------------------------
print("\nFor learn how to run and access request module , open this file in your editor and learn about this file")
print("\nThank You\n")
