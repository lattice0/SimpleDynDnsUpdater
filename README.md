# SimpleDynDnsUpdater

Edit the file with `username`, `password` and `hostname`. Change `enable_ipv6` to `True` if your computer supports `ipv6` 

# Run 
```
python3 SimpleDynDnsUpdater.py
```

# Run with Docker (automatically starts at boot)

Warning: if you want IPv6 in docker then your docker containers must support ip, otherwise you'll get errors. 

``` 
sudo docker build -t simpledyndnsupdater .
sudo docker run -it --restart unless-stopped -v "$PWD":/usr/src/myapp -w /usr/src/myapp simpledyndnsupdater python SimpleDynDnsUpdater.py
```
