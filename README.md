# SimpleDynDnsUpdater

# Run 
```
python3 SimpleDynDnsUpdater.py
```

# Run with Docker (automatically starts at boot)

Warning: if your docker image does not support IPv6 then you need to change `enable_ipv6` to `False`

``` 
sudo docker build -t simpledyndnsupdater .
sudo docker run -it --restart unless-stopped -v "$PWD":/usr/src/myapp -w /usr/src/myapp simpledyndnsupdater python SimpleDynDnsUpdater.py
```
