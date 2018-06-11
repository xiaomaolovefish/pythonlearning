
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpRequest
from django.shortcuts import render_to_response
from django.template import RequestContext,loader,Context

from ShareHouse.models import ShareH
from django.core.urlresolvers import resolve
from django.test import TestCase
from ShareHouse.views import share_house
class share_houseTest(TestCase):
    def test_root_url_resloves_to_share_house_view(self):
        found = resolve('/')
        self.assertEqual(found.func,share_house)


    def share_house_returns_to_content_html(self):
        request = HttpRequest()
        response = share_house(request)
        expected_html = render_to_string('share_house.html')
        self.assertEqual(response.content.decode(),expected_html)
