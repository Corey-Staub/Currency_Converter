import requests
import json

def get_cache(og):
    url = 'http://www.floatrates.com/daily/' + og.lower() + ".json"
    search = requests.get(url).text
    conv = dict(json.loads(search))
    cache = dict()
    for x in conv:
        y = conv[x]['rate']
        cache.update({x:y})
    return cache

def usd_eur_cache(cache):
    current_cache = dict()
    dollar = cache['usd']
    euro = cache['eur']
    current_cache.update({'USD': dollar})
    current_cache.update({'EUR': euro})
    return current_cache

def check_cache(current_chace, second, money, old_cache):
    print('Checking the cache...')
    if second in current_cache:
        print('Oh! It is in the cache!')
        rate = current_cache[second]
        conversion = rate * int(money)
        print(f'You received {round(conversion, 2)} {second}.')
    else:
        print('Sorry, but it is not in the cache!')
        rawRate = old_cache[second.lower()]
        conversion = rawRate * int(money)
        print(f'You received {round(conversion, 2)} {second}.')
        current_cache.update({second:rawRate})


original = input().upper()
cacheOfRates = get_cache(original)
current_cache = usd_eur_cache(cacheOfRates)
while True:
    secondInput = input().upper()
    if secondInput == "":
        break
    money = input()
    test = check_cache(current_cache, secondInput, money, cacheOfRates)
