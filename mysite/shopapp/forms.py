from django import forms
from .models import Product


class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True  # ← вот это ключевое


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        # Обработка списков/кортежей файлов
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "description", "price", "discount", "preview"]

    # Дополнительное поле для множественных изображений
    images = MultipleFileField(
        required=False,
        label="Дополнительные изображения"
    )


class CSVImportForm(forms.Form):
    csv_file = forms.FileField()
