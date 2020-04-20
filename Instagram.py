#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import instaloader
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json
import os, errno

class Insta_Info_Scraper:

    def getinfo(self, url):
        html = urllib.request.urlopen("https://www.instagram.com/navhas", context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'
                             })
        text = data[0].get('content').split()
        user = '%s %s %s' % (text[-3], text[-2], text[-1])
        followers = text[0]
        following = text[2]
        posts = text[4]
        L = instaloader.Instaloader()
        # Login or load session
        L.login("fniazi4u", "Byzz059@@")  # (login)
        try:
            os.remove("followers.txt")
        except OSError as e:  # this would be "except OSError, e:" before Python 2.6
            if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
                raise  #

        file = open("followers.txt", "a+")
        # Obtain profile metadata
        profile = instaloader.Profile.from_username(L.context, "navhas")
        #file.write("User :" + user)
        file.write(profile.username)
        file.write("\n")
        file.write("Total Followers :" + str(profile.followers))
        file.write("\n")
        file.write("Total Following :" + str(profile.followees))
        file.write("\n")
        #file.write("Total Posts :" + profile. )
        file.write("\n")
        file.write("---------------------------")
        file.write("\n")
        # Print list of followees
        follow_list = []
        count = 0
        for followee in profile.get_followers():
            #follow_list.append(followee.username +" Followed :" + str(followee.followed_by_viewer))
            follow_list.append(followee.username)
            file.write(follow_list[count])
            file.write("\n")
            #file.close()
            #print(follow_list[count])
            count = count + 1
        #follow_list.sort()
        #for p in range(len(follow_list)):
         #   print(follow_list[p])

        file.close()
        #print('User:', user)
        #print ('Followers:', followers)
        #print ('Following:', following)
        #print ('Posts:', posts)
        #print ('---------------------------')
    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        #with open('users.txt') as f:
        #self.content = f.readlines()
        #self.content = [x.strip() for x in self.content]
        #for url in self.content:
        self.getinfo("https://www.instagram.com/fniazi4u")
if __name__ == '__main__':
    obj = Insta_Info_Scraper()
    obj.main()
