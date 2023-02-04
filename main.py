import datetime
import pandas
import argparse
import os

from age_helpers import get_winery_age, get_winery_age_form
from http.server import HTTPServer, SimpleHTTPRequestHandler

from jinja2 import Environment, FileSystemLoader, select_autoescape
from collections import defaultdict

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--path',
                        help='Путь до .xlsx файла. По умолчанию в корне программы',
                        default='')
    parser.add_argument('-n', '--name',
                        help='Название .xlsx файла. Указывается с форматом файла. По умолчанию - wine.xlsx',
                        default='wine.xlsx')
    args = parser.parse_args()
    
    env = Environment(
        loader=FileSystemLoader('.'),
        autoescape=select_autoescape(['html', 'xml'])
    )

    template = env.get_template('template.html')

    excel_wine = pandas.read_excel(os.path.join(args.path, args.name), na_values=None, keep_default_na=False).to_dict(orient='records')

    sorted_excel_wines = defaultdict(list)

    for product in excel_wine:
        sorted_excel_wines[product['Категория']].append(product)

    winery_age = get_winery_age()
    winery_age_form = get_winery_age_form(winery_age)

    rendered_page = template.render(
        winery_age=winery_age,
        winery_age_form=winery_age_form,
        drinks=sorted_excel_wines
    )

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()
