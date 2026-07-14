from django.db.models import PositiveSmallIntegerField, Max, Model


class OrderedField(PositiveSmallIntegerField):
    def __init__(self, *args, field_name: str|None = None, **kwargs):
        self.field_name = field_name
        super().__init__(*args, **kwargs)

    def get_filter_kwargs(self, model_instance: Model) -> dict[str, int]:
        return {self.field_name: getattr(model_instance, self.field_name)}

    def pre_save(self, model_instance, add):
        order_value = getattr(model_instance, self.attname)
        if add or not order_value:
            model = model_instance._meta.model
            previous_order = model.objects.filter(
                **self.get_filter_kwargs(model_instance=model_instance)
            ).aggregate(max=Max(self.attname, default=0))["max"]
            setattr(model_instance, self.attname, previous_order + 1)
        return super().pre_save(model_instance, add)
