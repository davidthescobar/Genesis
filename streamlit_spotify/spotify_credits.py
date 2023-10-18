import streamlit as st
import base64
import configargparse
import json
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import sys
import time

# import webdriver_util as wdu
# git+https://github.com/bbusse/webdriver-util

op = webdriver.ChromeOptions()
prefs = {'protocol_handler': {'excluded_schemes': {'spotify-player': 'true'}}}
op.add_experimental_option('prefs', prefs)
op.add_argument('--headless')
driver = webdriver.Chrome(options=op)
driver.get('https://open.spotify.com/search')


def spotify_song_credits(url):
    # TODO: Use the WebDriverWait() function
    # https://selenium-python.readthedocs.io/waits.html
    # spotify_accept_cookies(driver)
    time.sleep(1)
    spotify_search(driver, url)
    time.sleep(1)
    spotify_show_song_options(driver)
    time.sleep(1)
    spotify_show_credits(driver)
    time.sleep(1)
    credits = spotify_get_credits(driver)
    st.write(credits['written_by'])


def spotify_search(driver, url):
    search = driver.find_element(
        'xpath',
        "/html/body/div[3]/div/div[2]/div[3]/header/div[3]/div/div/form/input"
    )
    search.send_keys(url)
    search.submit()


def spotify_show_song_options(driver):
    show_options = driver.find_element(
        'xpath',
        '/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/div[2]/div/div/div[2]/main/section/div[3]/div[4]/div/div/div/div/button[2]'
    )
    show_options.click()
    return True


def spotify_show_credits(driver):
    driver.find_element("xpath", "//*[text() = 'Show credits']/parent::button").click()
    return True


def spotify_get_credits(driver):
    credits = {}
    credits['performed_by'] = driver.find_element("xpath", "//*[text() = 'Performed by']/following::span").text
    credits['written_by'] = driver.find_element("xpath", "//*[text() = 'Written by']/parent::div").text
    credits['produced_by'] = driver.find_element("xpath", "//*[text() = 'Produced by']/parent::div").text
    credits['source'] = ""
    credits_json = json.dumps(credits)
    credits_str = json.loads(credits_json)
    return credits_str


if __name__ == '__main__':
    url = st.text_input(
        'Insert track link'
    )
    if url:
        spotify_song_credits(url)
