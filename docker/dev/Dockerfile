ARG DOCKER_IMAGE=raspbian/stretch
FROM $DOCKER_IMAGE

RUN apt-get update && apt-get install -y \
        openssh-server sudo python python-pip git vim tmux curl wget \
        python-dev python-setuptools zlib1g-dev libjpeg-dev gpac; \
        apt-get clean

RUN sed -i 's/%sudo.*ALL=(ALL:ALL).*ALL/%sudo   ALL=NOPASSWD:ALL/g' /etc/sudoers
RUN pip install -U requests pytest Flask pytest-flask \
        pytest-bdd pytest-mock bs4 selenium pillow

COPY vimrc.local /etc/vim/vimrc.local

RUN echo "dtoverlay=w1-gpio" >> /boot/config.txt \
    && echo "gpu_mem=128" >> /boot/config.txt \
    && echo "start_x=1" >> /boot/config.txt \
    && echo "dtparam=spi=on" >> /boot/config.txt

# Determine platform for geckodriver - Should be revisited
RUN grep -q Intel /proc/cpuinfo; \
    if [ $? -eq 0 ]; \
    then export PLATFORM=linux64; \
    else export PLATFORM=arm7hf; \
    fi ; \
    wget $(echo http://github.com$(curl -sL  https://github.com/mozilla/geckodriver/releases/tag/v0.23.0 | grep -Eo "/mozilla.*$PLATFORM.tar.gz")) \
        && tar -xvzf geckodriver-*.tar.gz \
        && rm geckodriver-*.tar.gz


RUN useradd -m -s /bin/bash developer
RUN echo 'developer:mysecretpassword' | chpasswd
RUN for group in adm dialout cdrom sudo audio video plugdev games users input netdev pi spi i2c gpio; do sed -i "/^${group}/ s/$/developer/" /etc/group; done

COPY .tmux.conf /home/developer/.tmux.conf
COPY .gitconfig /home/developer/.gitconfig
COPY .vimrc /home/developer/.vimrc
RUN echo "alias g=git" >> /home/developer/.bash_aliases \
    && echo 'alias startapp="cd ~/chickenpi/;FLASK_APP=src/chickenstrumentation/app.py FLASK_ENV=development flask run --host=0.0.0.0"' >> /home/developer/.bash_aliases \
    && echo "export PYTHONPATH=src/" >> /home/developer/.bashrc \
    && git clone https://github.com/collinlavoie/chickenpi.git /home/developer/chickenpi

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

RUN mkdir /var/run/sshd

EXPOSE 22:22
EXPOSE 80:80
CMD ["/usr/sbin/sshd", "-D"]
