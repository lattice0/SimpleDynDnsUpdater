# SimpleDynDnsUpdater

Edit the file with `username`, `password` and `hostname` and edit the minutes of interval of updates (3 minutes is default)

# Run 
```
python3 SimpleDynDnsUpdater.py
```

# Run with Docker (automatically starts at boot)

Warning: if you want IPv6 in docker then your docker containers must support ipv6, there are tutorials on this. If they don't support you'll just get a warnng every 3 minutes but things will work.

``` 
sudo docker build -t simpledyndnsupdater .
sudo docker run -it --restart unless-stopped -v "$PWD":/usr/src/myapp -w /usr/src/myapp simpledyndnsupdater python SimpleDynDnsUpdater.py
```
