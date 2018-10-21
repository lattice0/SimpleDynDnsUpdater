# SimpleDynDnsUpdater

# Run 
```
python3 SimpleDynDnsUpdater.py
```

# Run with Docker (automatically starts at boot)

```sudo docker run -it --restart unless-stopped --name SimpleDynDnsUpdater -v "$PWD":/usr/src/myapp -w /usr/src/myapp python:3 python SimpleDynDnsUpdater.py```
