from tastypie.resources import ModelResource
from api.models import Url
from tastypie.authorization import Authorization
from django.core.cache import cache
import random

class UrlResource(ModelResource):
    class Meta:
        queryset = Url.objects.all()
        resource_name = 'url'
        authorization = Authorization()
        fields = ['long_url', 'short_url']
        filtering = {
            'long_url':['exact']
        }

    def hydrate_short_url(self, bundle):
        long_url = bundle.data['long_url']
        key = self.shortify()

        # while key is in cache find a new one
        while cache.get(key):
            key = self.shortify()

        cache.set(key, long_url, 30)
        bundle.data['short_url'] = key
        return bundle

    def shortify(self):
        return str(hex(random.getrandbits(128)))[2:7]
