from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet
from .models import Article, Article_Scope, Scope


class Article_ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        i = 0
        for form in self.forms:
            dictionary = form.cleaned_data
            if not dictionary.get('main'):
                continue
            elif dictionary['main'] is True:
                i += 1
        if i == 0:
            raise ValidationError('Выберите главную тему')
        elif i > 1:
            raise ValidationError('Главной темой может быть только одна')
        return super().clean()


class Article_ScopeInline(admin.TabularInline):
    model = Article_Scope
    formset = Article_ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','text',)
    inlines = (Article_ScopeInline,)


@admin.register(Scope)
class ScopeAdmin(admin.ModelAdmin):
    list_display = ('scope',)
    inlines = (Article_ScopeInline,)



