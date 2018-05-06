# -*- coding: utf-8 -*-
import scrapy
import json

class PostSpider1(scrapy.Spider):
    name = "crypt_btc"
    start_urls = [
        'https://ru.investing.com/crypto/bitcoin/chat/2235',
        'https://ru.investing.com/crypto/bitcoin/chat/2234',
        'https://ru.investing.com/crypto/bitcoin/chat/2233',
        'https://ru.investing.com/crypto/bitcoin/chat/2232',
        'https://ru.investing.com/crypto/bitcoin/chat/2231',
        'https://ru.investing.com/crypto/bitcoin/chat/2230',
        'https://ru.investing.com/crypto/bitcoin/chat/2229',
        'https://ru.investing.com/crypto/bitcoin/chat/2228',
        'https://ru.investing.com/crypto/bitcoin/chat/2227',
        'https://ru.investing.com/crypto/bitcoin/chat/2226',
    ]

    def parse(self, response):
        for i in response.css('div.mainComment'): 
            yield {
                'text' : i.css('span.js-text ::text').extract(),
                'postDate' : i.css('div.mainComment span.js-date ::text').extract(),
                'author' :  i.css('div.mainComment a.js-user-link ::text').extract(),
                'topic' : response.css('h1 ::text').extract(),
            }

class PostSpider2(scrapy.Spider):
    name = "crypt_eth"
    start_urls = [
        'https://ru.investing.com/crypto/ethereum/chat/140',
        'https://ru.investing.com/crypto/ethereum/chat/139',
        'https://ru.investing.com/crypto/ethereum/chat/138',
        'https://ru.investing.com/crypto/ethereum/chat/137',
        'https://ru.investing.com/crypto/ethereum/chat/136',
    ]

    def parse(self, response):
        for i in response.css('div.mainComment'): 
            yield {
                'text' : i.css('span.js-text ::text').extract(),
                'postDate' : i.css('div.mainComment span.js-date ::text').extract(),
                'author' :  i.css('div.mainComment a.js-user-link ::text').extract(),
                'topic' : response.css('h1 ::text').extract(),
            }

class PostSpider3(scrapy.Spider):
    name = "crypt_eos"
    start_urls = [
        'https://ru.investing.com/crypto/eos/chat/3',
        'https://ru.investing.com/crypto/eos/chat/2',
        'https://ru.investing.com/crypto/eos/chat/1',
    ]

    def parse(self, response):
        for i in response.css('div.mainComment'): 
            yield {
                'text' : i.css('span.js-text ::text').extract(),
                'postDate' : i.css('div.mainComment span.js-date ::text').extract(),
                'author' :  i.css('div.mainComment a.js-user-link ::text').extract(),
                'topic' : response.css('h1 ::text').extract(),
            }

class PostSpider4(scrapy.Spider):
    name = "crypt_ltc"
    start_urls = [
        'https://ru.investing.com/crypto/litecoin/chat/61',
        'https://ru.investing.com/crypto/litecoin/chat/60',
        'https://ru.investing.com/crypto/litecoin/chat/59',
        'https://ru.investing.com/crypto/litecoin/chat/58',
        'https://ru.investing.com/crypto/litecoin/chat/57',
    ]

    def parse(self, response):
        for i in response.css('div.mainComment'): 
            yield {
                'text' : i.css('span.js-text ::text').extract(),
                'postDate' : i.css('div.mainComment span.js-date ::text').extract(),
                'author' :  i.css('div.mainComment a.js-user-link ::text').extract(),
                'topic' : response.css('h1 ::text').extract(),
            }

class PostSpider5(scrapy.Spider):
    name = "crypt_rpl"
    start_urls = [
        'https://ru.investing.com/crypto/ripple/chat/437',
        'https://ru.investing.com/crypto/ripple/chat/436',
        'https://ru.investing.com/crypto/ripple/chat/435',
        'https://ru.investing.com/crypto/ripple/chat/434',
        'https://ru.investing.com/crypto/ripple/chat/433',
    ]

    def parse(self, response):
        for i in response.css('div.mainComment'): 
            yield {
                'text' : i.css('span.js-text ::text').extract(),
                'postDate' : i.css('div.mainComment span.js-date ::text').extract(),
                'author' :  i.css('div.mainComment a.js-user-link ::text').extract(),
                'topic' : response.css('h1 ::text').extract(),
            }
