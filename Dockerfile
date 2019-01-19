FROM ubuntu:16.04

RUN apt-get update && apt-get install -y openssh-server python python-flask python-pip git vim tmux
RUN pip install -U pytest
RUN pip install pytest-bdd
RUN pip install pytest-flask
RUN pip install pytest-mock
RUN pip install bs4
RUN pip install --upgrade pip
RUN mkdir /var/run/sshd
RUN echo 'root:secretpassword' | chpasswd

RUN echo "alias g=git" >> /etc/skel/.bash_aliases
RUN echo "export PYTHONPATH=src/" >> /etc/skel/.bashrc
COPY .gitconfig /etc/skel/.gitconfig

RUN useradd -m -s /bin/bash developper
RUN echo 'developper:mysecretpassword' | chpasswd
RUN whoami
USER developper
RUN git clone https://github.com/collinlavoie/chickenstrumentation.git /etc/skel/chickenstrumentation
RUN whoami


# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22:22
EXPOSE 80:80
CMD ["/usr/sbin/sshd", "-D"]
