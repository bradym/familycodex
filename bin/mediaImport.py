#!/usr/bin/env python
# coding=utf-8
"""
Updates yaml files in data folder by reading metadata of media in the media folder. Also uploads
files to s3 where they'll be served to site visitors.

TODO: Add support for more filetypes, currently only works for audio files.
TODO: Refactor to use click for CLI handling and command line arguments.
"""

import glob
import os

import boto3
from eyed3.id3 import Tag
import yaml
from botocore.errorfactory import ClientError

base_dir = os.path.dirname(os.path.realpath(__file__))
media_dir = os.path.join('media')
base_url = 'https://www.familycodex.net'
data_path_template = '{}/data/people/{}.yaml'
bucket_name = 'www.familycodex.net'
aws_profile = 'familycodex'


def get_files(dir, extension):
    return glob.glob('media/**/{}/*.{}'.format(dir, extension))


def get_person_from_path(path):
    return path.split('/')[1]


def get_person_data(person):
    data_path = data_path_template.format(base_dir, person)
    if os.path.isfile(data_path):
        with open(data_path) as f:
            data = yaml.load(f)
    else:
        data = {}

    return data


def get_file_url(path):
    return '{}/{}'.format(base_url, path)


def search(url, data, key):
    return [element for element in data if element[key] == url]


def save_person_data(person, data):
    data_path = data_path_template.format(base_dir, person)
    with open(data_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)


# TODO: Refactor into a process_audio function
for file_path in get_files('audio', 'mp3'):
    tag = Tag()
    tag.parse(file_path)

    person = get_person_from_path(file_path)
    data = get_person_data(person)
    url = get_file_url(file_path)

    if 'audio' not in data:
        data['audio'] = []

    if not search(url, data['audio'], 'url'):

        data['audio'].append({
            'title': tag.title,
            'url': url
        })

        save_person_data(person, data)

        # TODO: break into separate function and only run when user specifies it should run.
        session = boto3.Session(profile_name=aws_profile)
        s3 = session.client('s3')

        try:
            s3.head_object(Bucket=bucket_name, Key=file_path)
        except ClientError as e:
            print('Uploading {} to s3'.format(file_path))
            s3.put_object(Bucket=bucket_name, Key=file_path, Body=open(file_path, 'rb'))
