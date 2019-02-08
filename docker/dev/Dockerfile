ARG DOCKER_IMAGE=raspbian/stretch
FROM $DOCKER_IMAGE
RUN apt-get update && apt-get install -y openssh-server python python-pip git vim tmux
RUN apt-get install -y curl
RUN pip install -U pytest
RUN pip install requests
RUN pip install Flask
RUN pip install pytest-bdd
RUN pip install pytest-flask
RUN pip install pytest-mock
RUN pip install bs4
RUN apt-get install -y python-dev python-setuptools
RUN apt-get install -y zlib1g-dev
RUN apt-get install -y libjpeg-dev
RUN pip install pillow
RUN pip install selenium
RUN cat /proc/cpuinfo
RUN grep -q Intel /proc/cpuinfo; \
    if [ $? -eq 0 ]; \
    then export PLATFORM=linux64; \
    else export PLATFORM=arm7hf; \
    fi ; \
    wget $(echo http://github.com$(curl -sL  https://github.com/mozilla/geckodriver/releases/tag/v0.23.0 | grep -Eo "/mozilla.*$PLATFORM.tar.gz"))
RUN tar -xvzf geckodriver-*.tar.gz && rm geckodriver-*.tar.gz
RUN pip install --upgrade pip
RUN mkdir /var/run/sshd
RUN echo 'root:secretpassword' | chpasswd

RUN echo "alias g=git" >> /etc/skel/.bash_aliases
RUN echo "export PYTHONPATH=src/" >> /etc/skel/.bashrc
COPY .gitconfig /etc/skel/.gitconfig
COPY .tmux.conf /etc/skel/.tmux.conf
RUN git clone https://github.com/collinlavoie/chickenstrumentation.git /etc/skel/chickenstrumentation

RUN useradd -m -s /bin/bash developper
RUN echo 'developper:mysecretpassword' | chpasswd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22:22
EXPOSE 80:80
CMD ["/usr/sbin/sshd", "-D"]
