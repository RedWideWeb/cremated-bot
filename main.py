from os import environ
import sys, requests, telebot

ENV = bool(environ.get('ENV', False))

if ENV:
    BOT_TOKEN = environ.get('BOT_TOKEN', None)
    PROJECT_NAME = environ.get('PROJECT_NAME', None)
else:
    sys.exit(0)


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['prices'])
def price(message):

    answer = ''
    try:
        xch = requests.get('https://www.okex.com/api/v5/market/ticker?instId=XCH-USDT').json()['data'][0]
        # pool = requests.get("https://www.hpool.com/api/datastatistics/pool?language=en&type=chia").json()['data']
        coins = requests.get('https://api.coinranking.com/v1/public/coins?symbols=BTC,ETH,DOGE,NANO,SC,BTT,STORJ,FIL,MYST').json()['data'][
            'coins']
    except Exception as e:
        print(e)
        return


    try:
        mass = requests.get('https://api.coinlore.net/api/ticker/?id=44195').json()[0]
        btc = coins[0]
        eth = coins[1]
        doge = coins[2]
        nano = coins[3]
        sc = coins[4]
        btt = coins[5]
        storj = coins[6]
        fil = coins[7]
        myst = coins[8]
    except Exception as e:
        print(e)
        return

    answer += '`{:<7}{:>7.2f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.2f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.0f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.0f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.4f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.2f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.4f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.4f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.2f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.2f} $ {:>+7.2f}%\n' \
              '{:<7}{:>7.2f} $ {:>+7.2f}%`'.format(
        'XCH:',
        float(xch['last']), 100 / (float(xch['last']) / (float(xch['last']) - float(xch['open24h']))),
        'MASS:',
        float(mass['price_usd']), float(mass['percent_change_24h']),
        'BTC:',
        float(btc['price']), float(btc['change']),
        'ETH:',
        float(eth['price']), float(eth['change']),
        'DOGE:',
        float(doge['price']), float(doge['change']),
        'NANO:',
        float(nano['price']), float(nano['change']),
        'SC:',
        float(sc['price']), float(sc['change']),
        'BTT:',
        float(btt['price']), float(btt['change']),
        'STORJ:',
        float(storj['price']), float(storj['change']),
        'FIL:',
        float(fil['price']), float(fil['change']),
        'MYST:',
        float(myst['price']), float(myst['change']),
    )
    bot.send_message(message.chat.id, answer, parse_mode='markdown')


bot.polling(none_stop=True)
