

# 20.04 was 'latest' as of 3/21/21
FROM ubuntu:20.04

RUN apt-get update; apt-get clean

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

# ping doesn't seem to come with ubuntu 20.04 (nor does wget, they stripped this version bare!). If i can find a smaller footprint
# thing that says "don't exit immediately after starting", use it! this is slow to install.
RUN apt-get update && apt-get install -y iputils-ping

WORKDIR /tests
COPY . .

WORKDIR /tests/frameworks_demo/tests

CMD ping localhost