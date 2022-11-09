from django.core.management.base import BaseCommand
from datetime import datetime
from uzlatekachny.models import Food
from bs4 import BeautifulSoup

class Command(BaseCommand):
    help = 'Import food menu from HTML file (exported from ODT)'

    def import_menu_from_html(self, html_menu):
        with open(html_menu, "r", encoding="cp1250") as html:
            soup = BeautifulSoup(html, 'html.parser')
            print("---------------FOOD CATEGORIES---------------")
            for cat_tag in soup.find_all(attrs={"class": "test"}):
                text = cat_tag.text.replace("\n", " ")
                category = [x for x in text.split(" - ") if len(x) > 2]
                cat_cze, cat_eng, cat_rus, cat_ger = category
                print(cat_cze, cat_eng, cat_rus, cat_ger)

        
        
        # for post in Post.objects.all():
            
        #     for tag in soup.find_all():
        #         if 'src' in tag.attrs:
        #             if 'soubory' in tag['src']:
        #                 index = tag['src'].index('soubory') + 7 # end of soubory
        #                 tag['src'] = f"/files{tag['src'][index:]}"
        #         if 'href' in tag.attrs:
        #             if 'soubory' in tag['href']:
        #                 index = tag['href'].index('soubory') + 7 # end of soubory
        #                 tag['href'] = f"/files{tag['href'][index:]}"
        #         if 'poster' in tag.attrs:
        #             if 'soubory' in tag['poster']:
        #                 index = tag['poster'].index('soubory') + 7 # end of soubory
        #                 tag['poster'] = f"/files{tag['poster'][index:]}"
            
        #     soup = str(soup)
        #     if 'soubory/' in soup:
        #         soup = soup.replace('soubory/', 'files/')

        #     post.content_cze = soup
        #     post.save()
    
    def add_arguments(self, parser):
        parser.add_argument('html_menu', nargs="?", default="menu.htm")

    def handle(self, *args, **options):
        start_time = datetime.now()
        html_menu = options['html_menu']
        self.import_menu_from_html(html_menu)
        time = datetime.now() - start_time
        self.stdout.write(self.style.SUCCESS(f'Successfully fixed URSl in posts and it takes {time.seconds//60} minutes and {time.seconds%60} seconds.'))
