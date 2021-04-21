# docker_complete


#####https://hackernoon.com/efficient-development-with-docker-and-docker-compose-e354b4d24831

### Docker Project setup
#####url : https://docs.docker.com/compose/django/

1. Create a Dockerfile inside the project/python (or other respective) folder
    
        FROM python:3
        ENV PYTHONUNBUFFERED 1
        RUN mkdir /python
        WORKDIR /python
        ADD requirements.txt /python/
        RUN pip install -r requirements.txt
        ADD . /python/

2. Create a docker-compose.yml inside the project folder

        version: '3'

        services:
          python:
            build:
              context: ./project/python
              dockerfile: Dockerfile
            command: python3 manage.py runserver 0.0.0.0:8000
            volumes:
              - ./project/python/:/python
            ports:
              - "8000:8000"
              
3. Install docker for linux

        chose platform : https://docs.docker.com/install/#supported-platforms
        installation page : https://docs.docker.com/install/linux/docker-ce/ubuntu/
  
   Step 1: Install
  
        csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo apt-get update
        Install packages to allow apt to use a repository over HTTPS:

        csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo apt-get install \
            apt-transport-https \
            ca-certificates \
            curl \
            gnupg-agent \
            software-properties-common

   Add Docker’s official GPG key:

        csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
        
Verify that you now have the key with the fingerprint 9DC8 5822 9FC7 DD38 854A E2D8 8D81 803C 0EBF CD88, by searching for the last 8 characters of the fingerprint.

        csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo apt-key fingerprint 0EBFCD88
    
        pub   rsa4096 2017-02-22 [SCEA]
      9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
        uid           [ unknown] Docker Release (CE deb) <docker@docker.com>
        sub   rsa4096 2017-02-22 [S]
   
        csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo apt-get install \
            >     apt-transport-https \
            >     ca-certificates \
            >     curl \
            >     software-properties-common
            Reading package lists... Done
            Building dependency tree       
            Reading state information... Done
            ca-certificates is already the newest version (20170717~16.04.1).
            The following additional packages will be installed:
              libcurl3-gnutls python3-software-properties software-properties-gtk
            The following NEW packages will be installed:
              curl
            The following packages will be upgraded:
              apt-transport-https libcurl3-gnutls python3-software-properties software-properties-common software-properties-gtk
            5 upgraded, 1 newly installed, 0 to remove and 555 not upgraded.
            Need to get 427 kB of archives.
            After this operation, 350 kB of additional disk space will be used.
            Do you want to continue? [Y/n] Y
            Get:1 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libcurl3-gnutls amd64 7.47.0-1ubuntu2.11 [185 kB]
            Get:2 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 apt-transport-https amd64 1.2.29 [26.2 kB]
            Get:3 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 curl amd64 7.47.0-1ubuntu2.11 [139 kB]
            Get:4 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 software-properties-common all 0.96.20.7 [9,452 B]
            Get:5 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 software-properties-gtk all 0.96.20.7 [47.2 kB]
            Get:6 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 python3-software-properties all 0.96.20.7 [20.3 kB]
            Fetched 427 kB in 1s (270 kB/s)                       
            (Reading database ... 217690 files and directories currently installed.)
            Preparing to unpack .../libcurl3-gnutls_7.47.0-1ubuntu2.11_amd64.deb ...
            Unpacking libcurl3-gnutls:amd64 (7.47.0-1ubuntu2.11) over (7.47.0-1ubuntu2.9) ...
            Preparing to unpack .../apt-transport-https_1.2.29_amd64.deb ...
            Unpacking apt-transport-https (1.2.29) over (1.2.15ubuntu0.2) ...
            Selecting previously unselected package curl.
            Preparing to unpack .../curl_7.47.0-1ubuntu2.11_amd64.deb ...
            Unpacking curl (7.47.0-1ubuntu2.11) ...
            Preparing to unpack .../software-properties-common_0.96.20.7_all.deb ...
            Unpacking software-properties-common (0.96.20.7) over (0.96.20) ...
            Preparing to unpack .../software-properties-gtk_0.96.20.7_all.deb ...
            Unpacking software-properties-gtk (0.96.20.7) over (0.96.20) ...
            Preparing to unpack .../python3-software-properties_0.96.20.7_all.deb ...
            Unpacking python3-software-properties (0.96.20.7) over (0.96.20) ...
            Processing triggers for libc-bin (2.23-0ubuntu10) ...
            Processing triggers for man-db (2.7.5-1) ...
            Processing triggers for dbus (1.10.6-1ubuntu3.1) ...
            Processing triggers for shared-mime-info (1.5-2) ...
            Processing triggers for gnome-menus (3.13.3-6ubuntu3) ...
            Processing triggers for desktop-file-utils (0.22-1ubuntu5) ...
            Processing triggers for bamfdaemon (0.5.3~bzr0+16.04.20160415-0ubuntu1) ...
            Rebuilding /usr/share/applications/bamf-2.index...
            Processing triggers for mime-support (3.59ubuntu1) ...
            Processing triggers for hicolor-icon-theme (0.15-0ubuntu1) ...
            Setting up libcurl3-gnutls:amd64 (7.47.0-1ubuntu2.11) ...
            Setting up apt-transport-https (1.2.29) ...
            Setting up curl (7.47.0-1ubuntu2.11) ...
            Setting up python3-software-properties (0.96.20.7) ...
            Setting up software-properties-common (0.96.20.7) ...
            Setting up software-properties-gtk (0.96.20.7) ...
            Processing triggers for libc-bin (2.23-0ubuntu10) ...
            csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
            OK
            csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo apt-key fingerprint 0EBFCD88
            pub   4096R/0EBFCD88 2017-02-22
                  Key fingerprint = 9DC8 5822 9FC7 DD38 854A  E2D8 8D81 803C 0EBF CD88
            uid                  Docker Release (CE deb) <docker@docker.com>
            sub   4096R/F273FCD8 2017-02-22

Next

    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$  sudo add-apt-repository \
    >    "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
    >    $(lsb_release -cs) \
    >    stable"
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo apt-get update
    Ign:1 http://dl.google.com/linux/chrome/deb stable InRelease
    Hit:2 https://repo.skype.com/deb stable InRelease
    Get:3 https://download.docker.com/linux/ubuntu xenial InRelease [66.2 kB]                                
    Hit:4 http://dl.google.com/linux/chrome/deb stable Release                                                                            
    Hit:6 http://archive.canonical.com/ubuntu xenial InRelease                                               
    Get:7 https://download.docker.com/linux/ubuntu xenial/stable amd64 Packages [5,491 B]
    Hit:8 http://ppa.launchpad.net/mozillateam/firefox-next/ubuntu xenial InRelease      
    Hit:9 http://archive.ubuntu.com/ubuntu xenial InRelease                                                                                            
    Hit:10 http://archive.ubuntu.com/ubuntu xenial-updates InRelease                                                                                   
    Ign:11 http://dell.archive.canonical.com/updates xenial-dell InRelease
    Hit:12 http://security.ubuntu.com/ubuntu xenial-security InRelease
    Hit:13 http://archive.ubuntu.com/ubuntu xenial-backports InRelease       
    Hit:14 http://dell.archive.canonical.com/updates xenial-dell Release
    Fetched 71.7 kB in 2s (24.4 kB/s)
    Reading package lists... Done
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo apt-get install docker-ce
    Reading package lists... Done
    Building dependency tree       
    Reading state information... Done
    The following additional packages will be installed:
      aufs-tools cgroupfs-mount containerd.io docker-ce-cli libseccomp2 pigz
    The following NEW packages will be installed:
      aufs-tools cgroupfs-mount containerd.io docker-ce docker-ce-cli pigz
    The following packages will be upgraded:
      libseccomp2
    1 upgraded, 6 newly installed, 0 to remove and 554 not upgraded.
    Need to get 50.4 MB of archives.
    After this operation, 243 MB of additional disk space will be used.
    Do you want to continue? [Y/n] Y
    Get:1 http://archive.ubuntu.com/ubuntu xenial/universe amd64 pigz amd64 2.3.1-2 [61.1 kB]
    Get:2 http://archive.ubuntu.com/ubuntu xenial-updates/main amd64 libseccomp2 amd64 2.3.1-2.1ubuntu2~16.04.1 [38.7 kB]
    Get:3 http://archive.ubuntu.com/ubuntu xenial/universe amd64 aufs-tools amd64 1:3.2+20130722-1.1ubuntu1 [92.9 kB]
    Get:4 https://download.docker.com/linux/ubuntu xenial/stable amd64 containerd.io amd64 1.2.0-1 [19.9 MB]
    Get:5 http://archive.ubuntu.com/ubuntu xenial/universe amd64 cgroupfs-mount all 1.2 [4,970 B]
    Get:6 https://download.docker.com/linux/ubuntu xenial/stable amd64 docker-ce-cli amd64 5:18.09.0~3-0~ubuntu-xenial [13.0 MB]                                                                                    
    Get:7 https://download.docker.com/linux/ubuntu xenial/stable amd64 docker-ce amd64 5:18.09.0~3-0~ubuntu-xenial [17.4 MB]                                                                                        
    Fetched 50.4 MB in 24s (2,041 kB/s)                                                                                                                                                                             
    Selecting previously unselected package pigz.
    (Reading database ... 217697 files and directories currently installed.)
    Preparing to unpack .../pigz_2.3.1-2_amd64.deb ...
    Unpacking pigz (2.3.1-2) ...
    Preparing to unpack .../libseccomp2_2.3.1-2.1ubuntu2~16.04.1_amd64.deb ...
    Unpacking libseccomp2:amd64 (2.3.1-2.1ubuntu2~16.04.1) over (2.2.3-3ubuntu3) ...
    Processing triggers for man-db (2.7.5-1) ...
    Processing triggers for libc-bin (2.23-0ubuntu10) ...
    Setting up libseccomp2:amd64 (2.3.1-2.1ubuntu2~16.04.1) ...
    Processing triggers for libc-bin (2.23-0ubuntu10) ...
    Selecting previously unselected package aufs-tools.
    (Reading database ... 217705 files and directories currently installed.)
    Preparing to unpack .../aufs-tools_1%3a3.2+20130722-1.1ubuntu1_amd64.deb ...
    Unpacking aufs-tools (1:3.2+20130722-1.1ubuntu1) ...
    Selecting previously unselected package cgroupfs-mount.
    Preparing to unpack .../cgroupfs-mount_1.2_all.deb ...
    Unpacking cgroupfs-mount (1.2) ...
    Selecting previously unselected package containerd.io.
    Preparing to unpack .../containerd.io_1.2.0-1_amd64.deb ...
    Unpacking containerd.io (1.2.0-1) ...
    Selecting previously unselected package docker-ce-cli.
    Preparing to unpack .../docker-ce-cli_5%3a18.09.0~3-0~ubuntu-xenial_amd64.deb ...
    Unpacking docker-ce-cli (5:18.09.0~3-0~ubuntu-xenial) ...
    Selecting previously unselected package docker-ce.
    Preparing to unpack .../docker-ce_5%3a18.09.0~3-0~ubuntu-xenial_amd64.deb ...
    Unpacking docker-ce (5:18.09.0~3-0~ubuntu-xenial) ...
    Processing triggers for libc-bin (2.23-0ubuntu10) ...
    Processing triggers for man-db (2.7.5-1) ...
    Processing triggers for ureadahead (0.100.0-19) ...
    ureadahead will be reprofiled on next reboot
    Processing triggers for systemd (229-4ubuntu21.1) ...
    Setting up pigz (2.3.1-2) ...
    Setting up aufs-tools (1:3.2+20130722-1.1ubuntu1) ...
    Setting up cgroupfs-mount (1.2) ...
    Setting up containerd.io (1.2.0-1) ...
    Setting up docker-ce-cli (5:18.09.0~3-0~ubuntu-xenial) ...
    Setting up docker-ce (5:18.09.0~3-0~ubuntu-xenial) ...
    update-alternatives: using /usr/bin/dockerd-ce to provide /usr/bin/dockerd (dockerd) in auto mode
    Processing triggers for libc-bin (2.23-0ubuntu10) ...
    Processing triggers for systemd (229-4ubuntu21.1) ...
    Processing triggers for ureadahead (0.100.0-19) ...
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo docker container run hello-world
    Unable to find image 'hello-world:latest' locally
    latest: Pulling from library/hello-world
    1b930d010525: Pull complete 
    Digest: sha256:2557e3c07ed1e38f26e389462d03ed943586f744621577a99efb77324b0fe535
    Status: Downloaded newer image for hello-world:latest
    
    Hello from Docker!
    This message shows that your installation appears to be working correctly.
    
    To generate this message, Docker took the following steps:
     1. The Docker client contacted the Docker daemon.
     2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
        (amd64)
     3. The Docker daemon created a new container from that image which runs the
        executable that produces the output you are currently reading.
     4. The Docker daemon streamed that output to the Docker client, which sent it
        to your terminal.
    
    To try something more ambitious, you can run an Ubuntu container with:
     $ docker run -it ubuntu bash
    
    Share images, automate workflows, and more with a free Docker ID:
     https://hub.docker.com/
    
    For more examples and ideas, visit:
     https://docs.docker.com/get-started/
    
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ 
        

### Installing docker-compose 
 url : https://docs.docker.com/compose/install/

    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ docker -v
    Docker version 18.09.0, build 4d60db4
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo curl -L "https://github.com/docker/compose/releases/download/1.23.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
      % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                     Dload  Upload   Total   Spent    Left  Speed
    100   617    0   617    0     0    308      0 --:--:--  0:00:01 --:--:--   308
    100 11.2M  100 11.2M    0     0   169k      0  0:01:07  0:01:07 --:--:--  202k
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo chmod +x /usr/local/bin/docker-compose
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ docker-compose --version
    docker-compose version 1.23.2, build 1110ad01

### Docker Compose the project

    docker-compose version 1.23.2, build 1110ad01
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo docker-compose -f docker-compose.yml build
    [sudo] password for csk: 
    Building python
    Step 1/7 : FROM python:3
     ---> db1c801f1c06
    Step 2/7 : ENV PYTHONUNBUFFERED 1
     ---> Using cache
     ---> c25338c072f0
    Step 3/7 : RUN mkdir /python
     ---> Running in 1940fc8cebf9
    Removing intermediate container 1940fc8cebf9
     ---> 2c7fdd18fc14
    Step 4/7 : WORKDIR /python
     ---> Running in b0737bcf2d2a
    Removing intermediate container b0737bcf2d2a
     ---> 77ff6b9570ea
    Step 5/7 : ADD requirements.txt /python/
     ---> a772cfbae5b3
    Step 6/7 : RUN pip install -r requirements.txt
     ---> Running in 25137091bbe2
    Collecting django (from -r requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/39/b0/2138c31bf13e17afc32277239da53e9dfcce27bac8cb68cf1c0123f1fdf5/Django-2.2.3-py3-none-any.whl (7.5MB)
    Collecting djangorestframework (from -r requirements.txt (line 2))
      Downloading https://files.pythonhosted.org/packages/1b/fe/fcebec2a98fbd1548da1c12ce8d7f634a02a9cce350833fa227a625ec624/djangorestframework-3.9.4-py2.py3-none-any.whl (911kB)
    Collecting pytz (from django->-r requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/3d/73/fe30c2daaaa0713420d0382b16fbb761409f532c56bdcc514bf7b6262bb6/pytz-2019.1-py2.py3-none-any.whl (510kB)
    Collecting sqlparse (from django->-r requirements.txt (line 1))
      Downloading https://files.pythonhosted.org/packages/ef/53/900f7d2a54557c6a37886585a91336520e5539e3ae2423ff1102daf4f3a7/sqlparse-0.3.0-py2.py3-none-any.whl
    Installing collected packages: pytz, sqlparse, django, djangorestframework
    Successfully installed django-2.2.3 djangorestframework-3.9.4 pytz-2019.1 sqlparse-0.3.0
    You are using pip version 18.1, however version 19.1.1 is available.
    You should consider upgrading via the 'pip install --upgrade pip' command.
    Removing intermediate container 25137091bbe2
     ---> 183140406526
    Step 7/7 : ADD . /python/
     ---> f44db05e17df
    Successfully built f44db05e17df
    Successfully tagged docker_complete_python:latest
    csk@csk-ai-revolution:~/PycharmProjects/git/docker_complete$ sudo docker-compose -f docker-compose.yml up
    Recreating docker_complete_python_1 ... done
    Attaching to docker_complete_python_1
    python_1  | Watching for file changes with StatReloader
    python_1  | Performing system checks...
    python_1  | 
    python_1  | System check identified no issues (0 silenced).
    python_1  | 
    python_1  | You have 2 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): auth.
    python_1  | Run 'python manage.py migrate' to apply them.
    python_1  | July 14, 2019 - 07:41:43
    python_1  | Django version 2.2.3, using settings 'djangoapi.settings'
    python_1  | Starting development server at http://0.0.0.0:8000/
    python_1  | Quit the server with CONTROL-C.
    python_1  | Not Found: /
    python_1  | [14/Jul/2019 07:49:36] "GET / HTTP/1.1" 404 2037
    python_1  | Not Found: /favicon.ico
    python_1  | [14/Jul/2019 07:49:37] "GET /favicon.ico HTTP/1.1" 404 2088 

### Check in postman rest api client

    POST /idealweight HTTP/1.1
    Host: 127.0.0.1:8000
    Content-Type: application/json
    Cache-Control: no-cache
    Postman-Token: c22b391a-6115-2f35-1ef1-754ad07e5ec9
    
    50
    

