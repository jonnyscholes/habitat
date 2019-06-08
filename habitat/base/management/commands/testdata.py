import os
import pathlib

from django.conf import settings
from django.contrib.auth.models import User
from django.core.files.storage import default_storage
from django.core.management.base import BaseCommand
from wagtail.core.models import Site, Page
from wagtail.images.models import Image

from habitat.base.models import HomePage


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        self.make_superuser()
        self.setup_images(test_img_dir='/code/assets/media/original_images')
        self.make_homepage()
        self.make_site()

    def make_homepage(self):
        self.root_page = HomePage(
            title='Home',
            hero_text='a',
            hero_cta='a',
            slug='habitat-home')
        Page.objects.get(pk=1).add_child(instance=self.root_page)

    def make_site(self):
        self.site = Site.objects.create(
            hostname='localhost', port=8000,
            root_page=self.root_page,
            site_name='bakerydev',
            is_default_site=True)

    def make_superuser(self):
        User.objects.create_superuser(username='admin', email='', password='p')

    def setup_images(self, test_img_dir=None):
        Image.objects.all().delete()

        def _is_image(filename):
            extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp']
            return pathlib.Path(filename).suffix.lower() in extensions

        image_prefix = 'original_images/'
        dest_dirname = os.path.join(settings.MEDIA_ROOT, image_prefix)

        if test_img_dir is None:
            HERE = os.path.join(os.path.dirname(__file__))
            test_img_dir = os.path.join(HERE, 'test_images')
        # Copy all images from test_img_dir to dest_dirname
        for filename in os.listdir(test_img_dir):
            image_src_path = os.path.join(test_img_dir, filename)
            image_dest_path = os.path.join(dest_dirname, filename)
            if not default_storage.exists(image_dest_path) and _is_image(filename):
                with open(image_src_path, 'rb') as f:
                    default_storage.save(image_dest_path, f)
        # Create Image models for each image in dest_dirname
        for filename in os.listdir(dest_dirname):
            if _is_image(filename):
                image_path = os.path.join(dest_dirname, filename)
                Image.objects.create(title=filename, file=image_path)
