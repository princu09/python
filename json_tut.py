import json

# -------------------------Json Loads------------------------------
data = '{"var1":"darkweb" ,"var2":56}'

parsed =  json.loads(data)

print(parsed)
print(parsed['var1'])

# -------------------------Json Dump------------------------------
data2 = {
    "channel_name":"darkweb videos",
    "cars":['bmw','ferari' , 'audi'],
    "fridge":('roti', "special bidi"),
    "isbad":False
}

jscomp = json.dumps(data2)
print(jscomp)

# -------------------------Note------------------------------------

print("\nFor learn how to run and access json , open this file in your editor and learn about this file")
print("\nThank You\n")
