FROM raspbian/stretch
RUN apt-get update && apt-get install -y openssh-server python python-pip git
RUN pip install Flask
RUN pip install --upgrade pip
RUN mkdir /var/run/sshd
RUN echo 'root:secretpassword' | chpasswd

RUN echo "export PYTHONPATH=src/" >> /etc/skel/.bashrc
RUN git clone https://github.com/collinlavoie/chickenstrumentation.git /etc/skel/chickenstrumentation

RUN useradd -m -s /bin/bash chickenpi
RUN echo 'chickenpi:change_this_to_a_real_password' | chpasswd

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22:22
EXPOSE 80:80
CMD ["/usr/sbin/sshd", "-D"]
