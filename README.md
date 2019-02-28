# chickenstrumentation

## Update Raspbian

    $ sudo apt update && sudo apt upgrade

## Install Docker

    $ curl -sSL https://get.docker.com | sh

## Download code

    $ sudo apt install git -y
    $ git clone https://github.com/collinlavoie/chickenpi.git
    $ cd chickenpi

## Select environment

### Application

    $ cd docker/app/

### Development

    $ cd docker/dev/

## Build image

    $ image="chickenpi:raspbian.stretch.$(date +%Y.%m.%d)"
    $ sudo docker build -t ${image} .

# Run

    $ sudo docker run -d -p 80:5000 -p 2222:22 --device=/dev/vchiq ${image}
