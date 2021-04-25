

# 20.04 was 'latest' as of 3/21/21
FROM ubuntu:20.04

# The parts of this dockerfile that install xvfb, fluxbox, wmctrl, and chrome, and then runs bootstrap.sh script, all came from:
# https://medium.com/dot-debug/running-chrome-in-a-docker-container-a55e7f4da4a8
RUN apt-get update; apt-get clean

# do i need this? was from something else. home/apps?
# Add a user for running applications.
RUN useradd apps
RUN mkdir -p /home/apps && chown apps:apps /home/apps

RUN apt-get install python3-pip -y

# even though the selenium-hub container coordinates the selenium tests, we still need local selenium to be able to call webdriver.remote()
RUN pip3 install selenium

RUN pip3 install pytest

RUN  pip3 install pytest-html

RUN pip3 install requests


RUN cd /

# need selenium webdriver chrome. this explained how to get it (different version of ubuntu, 
# but same idea):  https://christopher.su/2015/selenium-chromedriver-ubuntu/

RUN apt-get install unzip

RUN apt-get install wget -y

RUN wget -N http://chromedriver.storage.googleapis.com/89.0.4389.23/chromedriver_linux64.zip

RUN unzip chromedriver_linux64.zip

RUN chmod +x chromedriver

RUN mv -f chromedriver /usr/local/share/chromedriver

RUN ln -s /usr/local/share/chromedriver /usr/local/bin/chromedriver

RUN ln -s /usr/local/share/chromedriver /usr/bin/chromedriver

# ping doesn't seem to come with ubuntu 20.04 (nor does wget, they stripped this version bare!). If i can find a smaller footprint 
# thing that says "don't exit immediately after starting", use it! this is slow to install.
RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /tests
# COPY elementexercise_looper.py elementexercise_looper.py
COPY . .

WORKDIR /tests/frameworks_demo/tests

CMD ping localhost
# CMD ping localhost && python3 elementexercise_looper.py