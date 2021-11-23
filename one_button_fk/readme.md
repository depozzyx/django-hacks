# One-button foreign key changer

NOTE: Right now it is not the most conveniet nor good way to do this, but it works and you can walk your way out from here

## How to implement:

1. Download or copy contents of `custom_form.html` to your your templates (I will use path `your_app/templates/admin/custom_form.html`)
2. Open the downloaded html file, and replace `FOREIGN_KEY_FIELD_NAME` with name of foreign key field, that you wanna change to one button form in your Django administration
3. Go to your `admin.py` file and add `change_form_template`:

```python
# your_app/admin.py
class FooAdmin(admin.ModelAdmin):
    change_form_template = "admin/custom_form.html"
    ...
...
```
