from mods.models import Category


def create_default_categories(sender, **kwargs):
    default_categories = [
        'Adventure',
        'Cursed',
        'Decoration',
        'Economy',
        'Equipment',
        'Food',
        'Game Mechanics',
        'Library',
        'Management',
        'Minigame',
        'Mobs',
        'Optimization',
        'Social',
        'Storage',
        'Technology',
        'Transportation',
        'Utility',
        'World Generation',
    ]

    for category in default_categories:
        Category.objects.get_or_create(label=category)
