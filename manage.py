import os
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import db, config_class, app, config

app.config.from_object(config_class)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
