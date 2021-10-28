# Flask based app to get distance from MKAD

## Requirements

- Python 3.7
- IDE

## Set Up

- Create an virtual enviroment and make sure to run inside it
- Run `pip install -r requirements.txt` to install the dependencies

## Set Up environment variables (Linux)

Set up environment variable from root project directory
Set for development mode

```bash
export FLASK_ENV=development
export FLASK_APP=manage.py
export DATABASE_URL=postgresql://postgres:postgres@localhost:5432/delman
```

## Set Up database

Set up environment variable from root project directory
Set for development mode

```bash
python manage.py create_db
python manage.py seed_db
```

## Run the scheduler

```bash
cp vaccine-cron /etc/cron.d/vaccine-cron
chmod 0644 /etc/cron.d/vaccine-cron
crontab /etc/cron.d/vaccine-cron
```

# Create the log file to be able to run tail

RUN touch /var/log/cron.log

## Run tests

Run this command and access the web app at `localhost:5000`

```bash
pytest -vv
```

## Run

Run this command and access the app app at `localhost:5000`. You can check curl.sh to access di API

```bash
python manage.py run -h 0.0.0.0
```

## Run in docker

P.S. Currently not working, please run locally without docker

```bash
docker-compose up -d --build
docker-compose exec web python manage.py create_db
docker-compose exec web python manage.py seed_db
```

App running on `localhost:5000`. You can check curl.sh to access di API

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
