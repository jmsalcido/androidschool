# Deployment on Heroku

## Environment Vars
See ([app/config.py](../app/config.py)):

`heroku config:set VAR=value`

|Environment Var|Values|Description|
|----|----|----|
|**APP_SETTINGS**|`config.ProductionConfig, config.StagingConfig`| set the config class for the environment to use|
|**APP_SECRET_KEY**|| contact bear to know this value, default value at dev|
|**DATABASE_URL**|| use Heroku database. |

## Run migrations

Use this

`heroku run python manage.py db upgrade`
