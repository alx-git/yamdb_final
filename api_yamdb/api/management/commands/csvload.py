from django.core.management.base import BaseCommand
import pandas as pd

from django.apps import apps


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('models', nargs='+')

    def handle(self, **kwargs):
        names = kwargs['models']
        models = {
            model.__name__: model for model in apps.get_models()
        }

        for name in names:
            try:
                df = pd.read_csv(f'static/data/{name}.csv')
                dict = df.to_dict('records')
                for i in range(len(dict)):
                    models[name].objects.get_or_create(**dict[i])
                print(f'The model {name} imported sucessfully!')
            except BaseException as e:
                print(f'For the model {name} {e}')
