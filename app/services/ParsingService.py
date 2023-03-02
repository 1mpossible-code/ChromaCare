from bs4 import BeautifulSoup
import requests
import re
import cssutils
import logging

cssutils.log.setLevel(logging.CRITICAL)


class ParsingService:
    def __init__(self, url):
        self.url = ParsingService.normalize_url(url)

    def parse_colors(self):
        page = requests.get(self.url)
        soup = BeautifulSoup(page.text, 'html.parser')
        page_text = soup.prettify()

        css_hrefs = re.findall(r'href=\"(.+\.css)\"', page_text, re.M)
        css_text = ""
        if css_hrefs:
            for href in css_hrefs:
                full_link = self.get_full_link(href)
                css_page = requests.get(full_link)
                css_text += css_page.text

        style_tags = soup.find_all('style')
        for tag in style_tags:
            css_text += tag.string

        sheet = cssutils.parseString(css_text)
        colors = []
        for rule in sheet:
            if rule.type == rule.STYLE_RULE:
                for prop in rule.style:
                    if prop.name in ['color', 'background', 'background-color']:
                        value = prop.value
                        if ParsingService.is_valid_color_code(value) and value not in colors:
                            colors.append(value)
        return colors

    @staticmethod
    def is_valid_color_code(color_code):
        if color_code.startswith("#"):
            if len(color_code) != 4 and len(color_code) != 7:
                return False
        elif color_code.startswith("rgba("):
            if not color_code.endswith(")"):
                return False
            rgba_values = color_code[5:-1].split(",")
            if len(rgba_values) != 4:
                return False
        elif color_code.startswith("rgb("):
            if not color_code.endswith(")"):
                return False
            # rgb_values = color_code[4:-1].split(",")
            # if len(rgb_values) != 3:
            #     return False
        else:
            return False
        return True

    def get_full_link(self, href):
        if href.startswith("http"):
            # link is already complete
            return href
        elif href.startswith("../") or href.startswith("./") or href.startswith("/") or href[0]:
            # link is shortened
            full_link = self.url + '/' + href
            return full_link
        else:
            # link is already complete
            return href

    @staticmethod
    def normalize_url(url):
        if url.startswith("http://") or url.startswith("https://"):
            # already in normal format
            return url
        else:
            # prepend "https://" to the beginning
            return "https://" + url

if __name__ == '__main__':
    url = "regex101.com"
    pars = ParsingService(url)
    c = pars.parse_colors()
    print(c)

