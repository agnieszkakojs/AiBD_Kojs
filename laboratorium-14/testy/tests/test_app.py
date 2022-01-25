#!/usr/bin/python
# -*- coding: utf-8 -*-
from app import extract_sentiment, text_contain_word, bubbleSort
import pytest

testdata = ["I think today will be a great day", "I do not think this will turn out well"]

@pytest.mark.parametrize('sample', testdata)
def test_extract_sentiment(sample):

    sentiment = extract_sentiment(sample)

    assert sentiment > 0

testdata = [('There is a duck in this text', 'duck', True), ('There is nothing here', 'duck', False)]

@pytest.mark.parametrize('sample, word, expected_output', testdata)
def test_text_contain_word(sample, word, expected_output):

    assert text_contain_word(word, sample) == expected_output

testdata = [[4, 2, 8, 6, 3, 6, 2], [11, 3, 7, 5, 2], [64, 34, 25, 12, 22, 11, 90]]

@pytest.mark.parametrize('sample', testdata)
def test_bubbleSort(sample):

    assert bubbleSort(sample) == sorted(sample)
