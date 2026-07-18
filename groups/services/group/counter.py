from django.db import transaction
from groups.models import GroupCounter

model = GroupCounter


def get_order(prefix: str):
    with transaction.atomic():
        counter, _ = model.objects.select_for_update().get_or_create(
            prefix=prefix,
        )
        order = counter.order
        counter.order += 1
        counter.save()

    return order
