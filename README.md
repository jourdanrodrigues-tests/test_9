# Mozio Test

_Generated from [this Django template][template-link]._

This project runs entirely on Docker containers. Make sure to [have it][docker-download] in your environment.

## Setting up development environment

Before doing anything, run the following:

```bash
./scripts/setup_dev_env.sh
```

## Database

This project is setup on top of PostgreSQL, and the connection is established through an environment variable
called DATABASE_URL. For more details, check the files [.env.example](.env.example) and
[docker-compose.yml](docker-compose.yml).

## Running the app

To make your life slightly easier, the script [`compose.sh`](compose.sh) is there for you to run commands in your
container. It's just a wrapper for `docker-compose`, so you might want to take a look at
[its documentation][docker-compose-docs].

### Production mode

```bash
./compose.sh up
```

### Development mode

```bash
./compose.sh dev up
```

[template-link]: https://github.com/jourdanrodrigues/django-template
[docker-download]: https://www.docker.com/community-edition#/download
[docker-compose-docs]: https://docs.docker.com/compose/reference/
[django-template]: https://github.com/jourdanrodrigues/django-template
