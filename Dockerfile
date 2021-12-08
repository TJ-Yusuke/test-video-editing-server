FROM python:3
USER root

RUN apt-get update
RUN apt-get -y install locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8

ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt-get install -y vim less

RUN apt-get install build-essential
RUN wget https://www.imagemagick.org/download/ImageMagick.tar.gz
RUN tar xvzf ImageMagick.tar.gz
RUN cd ImageMagick-7.1.0-17 && \
     ./configure && \
    make && \
    make install
RUN ldconfig /usr/local/lib
RUN cd ../../ && rm -rf  ImageMagick*

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN python -m pip install moviepy
