# Bot for M

This is an asynchronous Telegram bot that helps you 
memorize words while learning a new language in a 
quiz format.

## Quick start

0. Get your Telegram bot token from [BotFather](https://t.me/BotFather).

1. ```cd``` to an acceptable directory for this project.

2. Clone repository to the directory using ```git-scm```:

```bash
git clone https://github.com/mdncv/bot_for_m.git
```

3. Add the _.env_ file to the project 
(_.example.env_ might help you).  

Variables of configuration:  

| Name              | Type   | Example                        | Description        |
|-------------------|--------|--------------------------------|--------------------|
|||||
| TOKEN             | String | "0123456789:SoMeSyMbOlShErE-Q" | Telegram bot token |
|||||
| POSTGRES_DB       | String | "postgres"                     | Database name      |
| POSTGRES_USER     | String | "postgres"                     | Database user      |
| POSTGRES_HOST     | String | "postgres"                     | Database host      |
| POSTGRES_PASSWORD | String | "1234"                         | Database password  |
|||||
| REDIS_HOST        | String | "redis"                        | Redis host         |

P.S. _For the love of God, please use **strong** passwords._  
P.P.S. _These hosts examples are for docker-compose 
use only. Use the standard option 
(something like **127.0.0.1** or **0.0.0.0**) in case 
you are running services separately._

4. Run services using ```docker-compose```:

```bash
docker-compose up -d --build
```

P.S. _Use ```sudo``` to fix the error with mounting 
database volume._

5. Find your bot using Telegram search, click 
```START``` button and enjoy!

99. In case you want to stop services:

```bash
docker-compose stop
```

P.S. _Use ```down``` instead of ```stop``` to remove 
containers and networks if needed._

## Usage

1. Select the language you are learning and your native 
language by typing language codes:

```
It

En
```

2. Add words by clicking ```add```.

3. Remove words by clicking ```remove```.

4. Start quiz by clicking ```quiz```.

5. See your stats by clicking ```stats```.

## Contributing

Bug reports and/or pull requests are welcome :)
