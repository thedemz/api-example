# REST API server with ssh tunneling example

+ Python 3
+ Flask
+ HTTP
+ JSON
+ ssh
+ curl


## Python

Check the python version for your system:

```
python --version
```


Check where your python binary is located:

```
which python
```


Create a virtual environment for this project:

```
python -m venv pyX.Y.Z --copies
```


Check where the python version is for the virtual environment:

```
which pyX.Y.Z/bin/python
```


Check whats installed in yhe virtual environment:

```
pyX.Y.Z/bin/python -m pip freeze
```

> e.g. (this path can be different)

```
ls pyX.Y.Z/lib64/pythonX.Y/site-packages/
```


Install requirements:

> upgrade pip first

```
pyX.Y.Z/bin/python -m pip install --upgrade pip
```

> install packages that is defined in the requirements.txt file

```
pyX.Y.Z/bin/python -m pip install -r requirements.txt
```


Run the code:

```
pyX.Y.Z server.py
```


Open another terminal and query the API:

```
curl -X GET 127.0.0.1:8080 -v
```


### Python formatting

Format your code with the package/tool `black`:

```
pyX.Y.Z -m black server.py
```


## ssh port forwarding


To find the ip address:

```
ip addr
```


The ssh command with the `-L` option can create a connection beetwen to computers.

The command looks like this:

```
ssh -L [LOCAL_IP:]LOCAL_PORT:DESTINATION:DESTINATION_PORT [USER@]SSH_SERVER
```


To create a connection that listen on port `8080` and forwards it to port `8080` on the remote:

> In this example;
>    + remote ip: `192.168.88.200`
>    + host name: `jack`

```
ssh - L 127.0.0.1:8080:127.0.0.1:8080 jack@192.168.88.200
```








