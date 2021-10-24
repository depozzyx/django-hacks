from dataclasses import dataclass
from typing import Any
from django.contrib import admin


def fake_admin_factory(
    app: str,
    view_id: str,
    name: str,
    name_plural: str,
    fake_model: Any,
):
    @dataclass
    class FakeChangeList:
        formset = []  # type: ignore
        list_editable = []  # type: ignore
        opts = {"app_label": app}  # type: ignore
        result_list = []  # type: ignore
        result_count = 0
        title = name
        is_popup = False
        to_field = name

    class FakeMeta:
        verbose_name = name
        verbose_name_plural = name_plural

    class FakeAdmin(admin.ModelAdmin):
        def get_changelist_instance(self, request):
            return FakeChangeList()

    return (
        type(view_id, (fake_model,), {"Meta": FakeMeta, "__module__": app}),
        FakeAdmin,
    )
