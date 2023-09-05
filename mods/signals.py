from mods.models import Category


def create_default_categories(sender, **kwargs):
    default_categories = [
        'Adventure',
        'Cursed',
        'Decoration'
    ]

    for category in default_categories:
        Category.objects.get_or_create(label=category)
