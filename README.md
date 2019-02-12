# chickenstrumentation

## Update Raspbian

    $ sudo apt update && sudo apt upgrade

## Install Docker

    $ curl -sSL https://get.docker.com | sh

## Download code

    $ sudo apt install git -y
    $ git clone https://github.com/collinlavoie/chickenstrumentation.git

## Build image

    $ cd chickenstrumentation/docker/app/
    $ sudo docker build -t chickenpi:raspbian.stretch.$(date +%Y.%m.%d) .
