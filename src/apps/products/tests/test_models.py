import pytest
from django.utils.text import slugify
from faker import Faker

from apps.products.models import Product


@pytest.mark.django_db
def test_create_product_model(faker: Faker) -> None:
    title = faker.text(max_nb_chars=50)
    product = Product.objects.create(title=title)

    assert product.title
    assert product.slug == slugify(title)
