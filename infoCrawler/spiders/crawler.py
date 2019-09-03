from scrapy.spiders import XMLFeedSpider
from bs4 import BeautifulSoup


class Crawler(XMLFeedSpider):
    name = 'crawler'
    start_urls = ['http://revistaautoesporte.globo.com/rss/ultimas/feed.xml']

    # Retira-se de todo o site os Titulos, Conteudos e Links e os separam em uma Collection
    def parse_node(self, Response, node):
        item = {}
        item['title'] = self.get_title(node)
        item['link'] = self.get_link(node)
        item['content'] = self.get_content(node)
        return item

    # Retira-se os Titulos
    def get_title(self, node):
        return node.xpath('title/text()').extract_first() or ""

    # Retira-se os links
    def get_link(self, node):
        return node.xpath('link/text()').extract_first() or ""

    # Dentro da descrição é convertido o conteudo para HTML e aplica-se o resultado dentro de uma lista.
    def get_content(self, node):
        raw_html = node.xpath('description/node()').extract_first()
        if not raw_html:
            return []
        soup = BeautifulSoup(raw_html, 'lxml')
        results = []
        for child in soup.body.children:
            item = self.get_item(child)
            if item:
                results.append(item)
        return results

    # Com a description retirada e convertida...
    # Retira-se o valor da <div><p><img> e <ul>
    def get_item(self, soup):
        if soup.name == 'p':
            return self.get_text(soup)
        elif soup.name == 'div' and soup.find('img'):
            return self.get_image(soup)
        elif soup.name == 'div' and soup.find('ul'):
            return self.get_links(soup)
        else:
            return None

    # Captura-se o conteúdo descritivo da matéria.
    def get_text(self, soup):
        text = soup.text.strip()
        if text:
            return {"type": "text", "content": text}
        else:
            return None

    # Retirado o caminho da Imagem
    def get_image(self, soup):
        link = soup.img.get('src')
        return {"type": "image", "content": link}

    # Retirado o caminho dos Links
    def get_links(self, soup):
        links = []
        for li in soup.ul.find_all('a'):
            link = li.get('href')
            links.append(link)
        return {"type": "links",
                "content": links}