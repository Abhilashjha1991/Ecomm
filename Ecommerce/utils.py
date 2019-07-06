from django.utils.text import slugify

def unique_slug_generator(model_instance,title,slug_field):
    print("world")
    slug=slugify(getattr(model_instance,title))
    model_class=model_instance.__class__ #this will return model name
    print(slug)
    print(model_class)
    while model_class._default_manager.filter(slug=slug).exists(): # this command is similsr to model.objects.filter()
        object_pk=model_class._default_manager.latest('pk')
        object_pk=object_pk.pk+1
        slug=f'{slug}-{object_pk}'
    return slug

def get_unique_slug(model_instance,slugable_field_name,slug_field_name):
    slug=slugify(getattr(model_instance,slugable_field_name))
    unique_slug=slug
    extension=1
    ModelClass=model_instance.__class__

    while ModelClass._default_manager.filter(**{slug_field_name:unique_slug}).exists():
        unique_slug='{}-{}'.format(slug,extension)
        extension+=1
    return unique_slug
    