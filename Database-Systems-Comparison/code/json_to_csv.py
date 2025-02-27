'''
With reference from Yelp dataset example https://github.com/Yelp/dataset-examples
'''
import json
import pandas as pd
import re
import argparse
import collections
import csv
import simplejson as json


data_path = '../data/'
tables = ['business', 'checkin', 'tip', 'user', 'review']

def read_and_write_file(json_file_path, csv_file_path, column_names):
    """Read in the json dataset file and write it out to a csv file, given the column names."""
    with open(csv_file_path, 'w', newline='', encoding='utf-8') as fout:
        csv_file = csv.writer(fout)
        csv_file.writerow(list(column_names))
        with open(json_file_path) as fin:
            for line in fin:
                line_contents = json.loads(line)
                csv_file.writerow(get_row(line_contents, column_names))

def get_superset_of_column_names_from_file(json_file_path):
    """Read in the json dataset file and return the superset of column names."""
    column_names = set()
    with open(json_file_path) as fin:
        for line in fin:
            line_contents = json.loads(line)
            column_names.update(
                    set(get_column_names(line_contents).keys())
                    )
    return column_names

def get_column_names(line_contents, parent_key=''):
    """Return a list of flattened key names given a dict.

    Example:

        line_contents = {
            'a': {
                'b': 2,
                'c': 3,
                },
        }

        will return: ['a.b', 'a.c']

    These will be the column names for the eventual csv file.

    """
    column_names = []
    for k, v in line_contents.items():
        column_name = "{0}.{1}".format(parent_key, k) if parent_key else k
        if isinstance(v, collections.abc.MutableMapping):
            column_names.extend(
                    get_column_names(v, column_name).items()
                    )
        else:
            column_names.append((column_name, v))
    return dict(column_names)

def get_nested_value(d, key):
    """Return a dictionary item given a dictionary `d` and a flattened key from `get_column_names`.
    
    Example:

        d = {
            'a': {
                'b': 2,
                'c': 3,
                },
        }
        key = 'a.b'

        will return: 2
    
    """
    if '.' not in key:
        if key not in d:
            return None
        return d[key]
    base_key, sub_key = key.split('.', 1)
    if base_key not in d:
        return None
    sub_dict = d[base_key]
    return get_nested_value(sub_dict, sub_key)

def get_row(line_contents, column_names):
    """Return a csv compatible row given column names and a dict."""
    row = []
    for column_name in column_names:
        line_value = get_nested_value(
                        line_contents,
                        column_name,
                        )
        if isinstance(line_value, str):
            row.append(line_value)
        elif line_value is not None:
            row.append('{0}'.format(line_value))
        else:
            row.append('')
    return row


for table in tables:

    # business table
    if table == 'business':
        input_file = data_path + 'yelp_academic_dataset_business.json'
        output_file = data_path + 'yelp_academic_dataset_business.csv'

        data_file = open(input_file)
        data = []
        for line in data_file:
            data.append(json.loads(line))
        business_df = pd.DataFrame(data)
        data_file.close()
        business_df.to_csv(output_file, index=False)

    # checkin table
    if table == 'checkin':
        input_file = data_path + 'yelp_academic_dataset_checkin.json'
        output_file = data_path + 'yelp_academic_dataset_checkin.csv'

        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write("business_id,date\n")  # Write CSV header
            for line in infile:
                # Parse each JSON object
                record = json.loads(line)
                business_id = record["business_id"]
                dates = record["date"]
                
                # Write each date as a new row in the CSV
                outfile.write(f'{business_id},"{dates}"\n')
    
    # review table
    if table == 'review':
        input_file = data_path + 'yelp_academic_dataset_review.json'
        output_file = data_path + 'yelp_academic_dataset_review.csv'
        column_names = get_superset_of_column_names_from_file(input_file)
        read_and_write_file(input_file, output_file, column_names)

    # tip table
    if table == 'tip':
        input_file = data_path + 'yelp_academic_dataset_tip.json'
        output_file = data_path + 'yelp_academic_dataset_tip.csv'

        def clean_text(text):
            cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
            cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
            return cleaned_text

        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            outfile.write("business_id,user_id,text,date,compliment_count\n")
            for line in infile:
                record = json.loads(line)
                text = clean_text(record["text"])
                dates = record["date"]
                compliment_count = int(record["compliment_count"])
                business_id = record["business_id"]
                user_id = record["user_id"]

                outfile.write(f'{business_id},{user_id},"{text}","{dates}",{compliment_count}\n')

    # user table
    if table == 'user':
        input_file = data_path + 'yelp_academic_dataset_user.json'
        output_file = data_path + 'yelp_academic_dataset_user.csv'
        column_names = get_superset_of_column_names_from_file(input_file)
        read_and_write_file(input_file, output_file, column_names)