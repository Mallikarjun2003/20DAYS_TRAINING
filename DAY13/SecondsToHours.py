# ip : 7262 seconds
# op : 2hr:1m:2sec
seconds = int(input())
hrs = seconds//(60*60)
min = (seconds - hrs*3600)//60
sec = seconds - hrs*3600 - min*60

print(f"{hrs}hrs:{min}min:{sec}sec")