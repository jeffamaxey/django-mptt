def cached_field_value(instance, attr):
    try:
        # In Django 2.0, use the new field cache API
        field = instance._meta.get_field(attr)
        if field.is_cached(instance):
            return field.get_cached_value(instance)
    except AttributeError:
        cache_attr = f"_{attr}_cache"
        if hasattr(instance, cache_attr):
            return getattr(instance, cache_attr)
    return None
