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
import urllib.request as req
import time
class Insta_Info_Scraper:
    def getinfo(self, url):
        html = urllib.request.urlopen("https://www.instagram.com/egupta", context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all('meta', attrs={'property': 'og:description'                             })
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
        time.sleep(10)
        profile = instaloader.Profile.from_username(L.context, "egupta")
        file.write(profile.username)

        file.write("\n")
        file.write("Total Followers :" + str(profile.followers))
        file.write("\n")
        file.write("Total Following :" + str(profile.followees))
        file.write("\n")
        file.write("Profile biography :"+profile.biography)
        file.write("\n")
        file.write("---------------------------")
        file.write("\n")
        file.write("\Followers List")
        file.write("\n")
        follow_list = []
        count = 0
        for followee in profile.get_followers():
            #follow_list.append(followee.username +" Followed :" + str(followee.followed_by_viewer))
            follow_list.append(followee.username)
            req.urlretrieve(followee.get_profile_pic_url(),followee.username+".jpg")
            for post in profile.get_posts():
                L.download_post(post, target=followee.username)
            file.write(follow_list[count])
            file.write("\n")
            #file.close()
            #print(follow_list[count])
            count = count + 1
        file.close()
    def main(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE
        self.getinfo("https://www.instagram.com/egupta")
if __name__ == '__main__':
    obj = Insta_Info_Scraper()
    obj.main()
