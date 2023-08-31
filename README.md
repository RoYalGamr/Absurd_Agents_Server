# Absurd_Agents_Server
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)



## Usage

### building Docker file

For Linux Terminal
```docker
docker build path/to/Dockerfile -t servername
```

For Windows (Powershell)
```docker
docker buildx build path/to/Dockerfile -t servername
```

### For running the server

For Linux terminal
```docker
docker run -p 12345:12345 -v $(pwd)/dictionaries:/app/dictionaries servername
```

For Windows (Powershell)
```docker
docker run -p 12345:12345 -v ${PWD}\dictionaries:/app/dictionaries servername
```
