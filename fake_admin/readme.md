# Custom admin page / Fake admin page

## How to implement:

1. Download or copy contents of `fake_admin.py` to your project
2. Go to your `admin.py` file, import `fake_admin_factory` function, then create fake model and model admin objects:

```python
# your_app/admin.py
FakeBruhModel, FakeBruhAdmin = fake_admin_factory(
    "bot", "fake", "Fake Admin", "FakeAdmin", AnyOtherModel
)
```

Note: As you see, we actually need another model, but it is only for technical reasons. You can put there **any model from your app** and you can make any number of fake admin pages with that model. You do NOT need to create any new models for fake admin to work

3. Tada! You can now use your faked model and your faked admin as you would normally do:

```python
# your_app/admin.py
@admin.register(FakeBruhModel)
class FakeAdmin(FakeBruhAdmin):
    change_list_template = "admin/custom.html"

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(request, extra_context=extra_context)
        response.context_data["some_data"] = [1, 2, 3, "cool data"]
        return response
```

```html
<!-- your_app/templates/admin/custom.html -->
{% extends "admin/base_site.html" %}
<!--  -->
{% load i18n admin_urls static admin_list %}

<!--  -->
{% block content %}
<h1>Hi, this is faked admin page without model!</h1>

<section>
    <b>{{some_data}}:</b>
    <ul>
        {% for item in some_data %}
        <li>{{item}}</li>
        {% endfor %}
    </ul>
</section>
{% endblock %}
```

Tip: if you keep getting error from your linter in `admin.py` like `Variable "bot.admin.FakeBruhAdmin" is not valid as a type` you can add `FakeBruhAdmin: typing.Any` on top of your `fake_admin_factory` call
