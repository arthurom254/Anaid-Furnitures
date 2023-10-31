from django import template

register=template.Library()
@register.filter(name='rating_stars')
def rating_stars(rating):
    full_stars = int(rating)
    half_stars = float(rating) % 1 >= 0.5
    empty_stars = 5 - full_stars - half_stars
    return f"<i class='ri-star-fill text-dark mr-1'></i>"*full_stars + f"<i class='ri-star-half-fill text-dark mr-1'></i>"*half_stars +f"<i class='ri-star-fill mr-1 text-muted opacity-25'></i>"*empty_stars
