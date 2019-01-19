eval "$(ssh-agent)" && ssh-agent -s
chmod 0600 /home/developper/.ssh/id_rsa
ssh-add /home/developper/.ssh/id_rsa
git clone git@github.com:collinlavoie/chickenstrumentation.git
cd chickenstrumentation