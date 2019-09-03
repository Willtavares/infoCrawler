# infoCrawler
Create a Python webcrawler using Beatifulsoup package.

**Criar um crawler que leia [este feed] (http://revistaautoesporte.globo.com/rss/ultimas/feed.xml) e retorne um json estruturado da seguinte forma**

```
{
    'feed': [
        'item': {
            'title': 'titulo da materia',
            'link': 'url da materia',
            'description': [
                {
                    'type': 'text',
                    'content': 'conteudo da tag'
                },
                {
                    'type': 'image',
                    'content': 'url da imagem'
                },
                {
                    'type': 'links',
                    'content': ['urls dos links', ...]
                }
            ]
        },
        'item': {
            ...
        },
        'item': {
            ...
        },
        'item': {
            ...
        }
    ]
}
```

## Install requirements
### Digite no terminal o seguinte comando
pip freeze -r requirements.txt


## Execute Crawler
Acesse o caminho: infocrawler\spiders\
### A Seguir digite no terminal o seguinte comando
scrapy crawl crawler -o crawler.json

Na raiz do projeto você terá o arquivo .json extraido conforme desejado.

> Thanks for the opportunity
