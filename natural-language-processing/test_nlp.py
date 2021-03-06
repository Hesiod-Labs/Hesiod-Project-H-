# test class

import os
from vde_environment import Topic, VDE, CSV


# creating a generic topic
def test_topic():
    topic = Topic(['Prose', 'American History', 'Liberty'], ['Prose.zip', 'AmericanHistory,zip', 'LincolnLibterty.zip'])
    print(topic.topic_dict)


# creating a generic vde environment
def test_vde_environment():
    topic = Topic(['Prose', 'AmericanHistory', 'Liberty'], ['Prose.zip', 'AmericanHistory.zip', 'Liberty.zip'])
    VDE.main('VDE_Repository', topic)
    for title in topic.titles:
        assert os.path.exists(title)


# read the csv files and return some arbitrary information
def test_csv_environment():
    CSV.topic_model('NMF', 'studentscores.zip', 'gender')
    CSV.topic_model('LDA', 'suiciderates.zip', 'country')
