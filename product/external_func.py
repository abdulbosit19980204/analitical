import os
from django.utils import timezone


def product_image_upload_path(instance, filename):
    today = timezone.now().strftime('%Y%m%d')
    ext = filename.split('.')[-1]
    filename = f"{instance.product.article}_{instance.product.print_title}.{ext}"
    return os.path.join(f"images/products/", filename)
