from ..engine import SearchEngine
from ..config import PROXY, TIMEOUT, FAKE_USER_AGENT


class Bing(SearchEngine):
    '''Searches bing.com'''
    def __init__(self, proxy=PROXY, timeout=TIMEOUT, username: str or None = None, password: str or None = None, language: str or None = None):
        super(Bing, self).__init__(proxy, timeout, username, password, language)
        self._base_url = u'https://www.bing.com'
        self.set_headers({'User-Agent':FAKE_USER_AGENT})
        self.__language_dict = {
            "EN": "en",
            "ES": "es"
        }

    def _selectors(self, element):
        '''Returns the appropriate CSS selector.'''
        selectors = {
            'url': 'a[href]', 
            'title': 'h2', 
            'text': 'p', 
            'links': 'ol#b_results > li.b_algo', 
            'next': 'div#b_content nav[role="navigation"] a.sb_pagN'
        }
        return selectors[element]
    
    def _first_page(self):
        '''Returns the initial page and query.'''
        self._get_page(self._base_url)
        language = self.__language_dict[self._language] if self._language in self.__language_dict else "en"
        url = u'{}/search?q={}&search=&form=QBLH&setlang={}'.format(self._base_url, self._query, language)
        return {'url':url, 'data':None}

    def _next_page(self, tags):
        '''Returns the next page URL and post data (if any)'''
        selector = self._selectors('next')
        next_page = self._get_tag_item(tags.select_one(selector), 'href')
        url = None
        if next_page:
            url = (self._base_url + next_page) 
        return {'url':url, 'data':None}
