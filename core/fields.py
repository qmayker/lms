from django.db.models import PositiveSmallIntegerField


class OrderedField(PositiveSmallIntegerField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instance, add):
        pass
