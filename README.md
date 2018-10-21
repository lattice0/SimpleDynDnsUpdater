# SimpleDynDnsUpdater

# Run 
```
python3 SimpleDynDnsUpdater.py
```

# Run with Docker (automatically starts at boot)

``` 
sudo docker build -t simpledyndnsupdater .
sudo docker run -it --rm -v "$PWD":/usr/src/myapp -w /usr/src/myapp simpledyndnsupdater python SimpleDynDnsUpdater.py
```
