### Add user
* ssh or login into your server with root user
```
wget https://raw.githubusercontent.com/bhickta/frappe-installation-script/master/add_user.py
python3 add_user.py
```

# Install node, npm and yarn
```
curl https://raw.githubusercontent.com/creationix/nvm/master/install.sh | bash
source ~/.profile
nvm install 18.16.0
sudo apt-get install npm
sudo npm install -g yarn
```