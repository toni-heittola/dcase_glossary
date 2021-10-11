#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import os
import glob
import yaml
import argparse

def main(argv):
    parser = argparse.ArgumentParser(description='Script to investigate glossary file.')
    parser.add_argument("-D", "--definitions", help="show terms with empty definitions", action="store_true")
    parser.add_argument("-FI", "--fi", help="show terms without Finnish translation", action="store_true")
    parser.add_argument("-ES", "--es", help="show terms without Spanish translation", action="store_true")
    parser.add_argument("-FR", "--fr", help="show terms without French translation", action="store_true")
    parser.add_argument("-DE", "--de", help="show terms without German translation", action="store_true")
    parser.add_argument("-PL", "--pl", help="show terms without Polish translation", action="store_true")

    args = parser.parse_args()

    print('Checking glossary file')
    print('========================================================')
    print()

    glossary_file = 'glossary.yaml'
    # Read template
    with open(glossary_file, 'r') as file:
        glossary = yaml.load(file, Loader=yaml.FullLoader)

    data = {}
    for item in glossary['glossary']:
        data[item['term'].lower()] = item
    sorted_terms = sorted(data)

    items_without_definition = 0
    items_fi = 0
    items_pl = 0
    items_es = 0
    items_fr = 0
    items_de = 0
    items_wikipedia = 0
    items_wiktionary = 0
    for term in sorted_terms:
        if 'definition' not in data[term]:
            items_without_definition += 1

        if 'fi' in data[term]:
            items_fi += 1
        if 'pl' in data[term]:
            items_pl += 1
        if 'es' in data[term]:
            items_es += 1
        if 'fr' in data[term]:
            items_fr += 1
        if 'de' in data[term]:
            items_de += 1

        if 'wikipedia' in data[term]:
            items_wikipedia += 1
        if 'wiktionary' in data[term]:
            items_wiktionary += 1

    print('=== Items ===')
    print('Items                         :', len(glossary['glossary']))
    print('Items without definition (%)  :', round((items_without_definition / len(glossary['glossary'])) * 100.0), '%  ', '(', items_without_definition, ')')
    print()
    print('=== Languages ===')
    print('Items with Finnish translation:', round((items_fi / len(glossary['glossary'])) * 100.0), '%  ', '(', items_fi, ')')
    print('Items with Spanish translation:', round((items_es / len(glossary['glossary'])) * 100.0), '%  ', '(', items_es, ')')
    print('Items with French translation :', round((items_fr / len(glossary['glossary'])) * 100.0), '%  ', '(', items_fr, ')')
    print('Items with German translation :', round((items_de / len(glossary['glossary'])) * 100.0), '%  ', '(', items_de, ')')
    print('Items with Polish translation :', round((items_pl / len(glossary['glossary'])) * 100.0), '%  ', '(', items_pl, ')')
    print()
    print('=== Links ===')
    print('Items with wikipedia link     :', round((items_wikipedia/len(glossary['glossary']))*100.0), '%  ', '(', items_wikipedia, ')')
    print('Items with wiktionary link    :', round((items_wiktionary / len(glossary['glossary'])) * 100.0), '%  ', '(', items_wiktionary, ')')

    if args.definitions:
        print()
        print('=== Terms without definition ===')
        for term in sorted_terms:
            if 'definition' not in data[term]:
                print(' ', data[term]['term'])

    if args.fi:
        print()
        print('=== Terms without Finnish translation ===')
        for term in sorted_terms:
            if 'fi' not in data[term]:
                print(' ', data[term]['term'])

    if args.es:
        print()
        print('=== Terms without Spanish translation ===')
        for term in sorted_terms:
            if 'es' not in data[term]:
                print(' ', data[term]['term'])

    if args.fr:
        print()
        print('=== Terms without French translation ===')
        for term in sorted_terms:
            if 'fr' not in data[term]:
                print(' ', data[term]['term'])

    if args.de:
        print()
        print('=== Terms without German translation ===')
        for term in sorted_terms:
            if 'de' not in data[term]:
                print(' ', data[term]['term'])

    if args.pl:
        print()
        print('=== Terms without Polish translation ===')
        for term in sorted_terms:
            if 'pl' not in data[term]:
                print(' ', data[term]['term'])


if __name__ == "__main__":
    sys.exit(main(sys.argv))