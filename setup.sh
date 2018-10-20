sudo apt-get install build-essential checkinstall -y
sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev  -y
sudo add-apt-repository ppa:jonathonf/python-3.7 -y
sudo apt-get install virtualenv -y
virtualenv --python=python3.7 env
. ./env/bin/activate