# Wagtail Habitat

This is a purpose build environment for Wagtail developers to run automated and manual
tests against (built with frontend testing in mind).

** DO NOT TAKE INSPIRATION FOR YOUR PRODUCTION WEBSITE FROM THIS PROJECT **

## Requirements

- Docker

## Setup

- `docker-compose up --build -d`
- `docker-compose run app ./manage.py migrate`
- `docker-compose run app ./manage.py testdata`
- `docker-compose up`

### Access admin

- `docker-compose up`

The project should now be available at `http://localhost:8000/admin`. There is no frontend,
so don’t bother looking there.

### Running tests

- `docker-compose up -d`
- `docker exec -it habitat_app_1 npm test`

## TODO

- Flesh out models so that all Wagtail views/states are reachable
- Test out how this goes inside Travis
- Deal with messiness in `Dockerfile`

## Code of conduct

This project follows the same [code of conduct](https://github.com/wagtail/wagtail/blob/master/CODE_OF_CONDUCT.md) as
Wagtail.

## Maintenance

This is a proof of concept to deal with some issues facing some Wagtail developers.
It may never go past the initial commit.

## License

BSD
