# Absurd_Agents_Server
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)

## Usage

Git clone the repository 
```bash
git clone https://github.com/Ritvik25goyal/Absurd_Agents_Server.git
```
change the working directory to the server
```
cd Absurd_Agents_Server
```


### building Docker file

For Linux Terminal
```bash
docker build . -t servername
```

For Windows (Powershell)
```bash
docker buildx build . -t servername
```

### For running the server

For Linux terminal
```bash
docker run -p 12345:12345 -v $(pwd)/dictionaries:/app/dictionaries servername
```

For Windows (Powershell)
```bash
docker run -p 12345:12345 -v ${PWD}\dictionaries:/app/dictionaries servername
```
