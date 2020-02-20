[TOC]



# Web Server vs Web Application Server

### 01. Web Server

간단하게 클라이언트로부터 HTTP 요청을 받으면 이에 해당하는 웹 페이지(html+js+css+img)를 **정적**으로 처리하여 보내주는 프로그램으로 `apache` 와 `nginx` 가 있다.

### 02. WAS(Web Application Server)

HTTP 요청이 들어오면 이에 해당하는 로직을 처리하는 미들웨어(소프트웨어 엔진)이다. 웹 서버와 다르게 **동적** 서버 콘텐츠를 수행하며 `Tomcat`이 대표적이다.



# Apache vs Nginx

이러한 웹 서버에는 대표적으로 `apache`와 `nginx`가 있다. 우선 대표적인 웹 서버인 `apache`에 대해 알아보자

### 01. Apache

우리나라 대표적인 웹 서버로 거의 표준에 가까울 정도로 많은 기업들이 이용하고 있다. 이러한 아파치는 클라이언트로부터 요청을 받으면 MPM(Multi Processing Module: 다중처리모듈) 방식으로 처리를 한다. 이러한 MPM은 다음과 같은 두가지 방식이 존재한다

1. Perfork MPM

   각 프로세스는 한번에 한 연결만 1개의 스레드로 처리한다. 프로세스 간에 메모리 공유가 없기 때문에 안전한 것이 장점이다.

2. Worker MPM

   1개의 프로세스가 여러 스레드를 사용한다. 스레드간 메모리를 공유하기 때문에 메모리를 덜 사용한다.



### 02. Nginx

전세계적으로 관심이 크게 증가하고 있는 웹 서버이다. 이러한 Nginx의 특징은 바로 `Event Driven` 방식인 것이다. 해당 방식의 경우 요청이 들어오면 어떤 동작을 해야할지 알려주고 다른 요청을 처리한다. 즉 요청이 들어왔을 때, 하나의 프로세스가 이 요청을 담당하고 있는 것이 아니라 어떻게 동작할지 알려주고 다른 요청을 처리하다가 `Event Listener`가 해당 동작이 완료됐음을 인식하면 응답해주는 방식이다. (라고 이해... 이해한 것으로 보면 자바스크립트와 비슷해보인다..) 따라서 흐름이 끊기지 않고 응답이 빠르게 진행되어 1개의 프로세스로 빠르게 작업할 수 있다. 그 결과 동시 접속 처리에 특화되어있다.



# Nginx

### 01. Nginx의 역할

#### 1. 정적 파일을 처리하는 HTTP 서버로서의 역할

위에서 언급한 web server의 역할을 수행한다

#### 2. 응용프로그램 서버에 요청을 보내는 리버스 프록시로서 역할

클라이언트에서 요청이 오면 프록시 서버(nginx)에서 리버스 서버(WAS)로부터 데이터를 가져온다. 이렇게 한 단계를 거치는 이유는 request에 대한 버퍼링이 있기 때문이라고 한다. 클라이언트가 WAS에 직접 요청할 경우 WAS의 프로세스 1개가 응답 대기 상태가 되야하지만 프록시 서버가 중간에서 요청을 배분해준다면 효율적으로 자원을 사용할 수 있다. nginx의 nginx.conf 파일에서 보이는 `location`이 요청을 배분하기 위해 사용하는 지시어다



### 02. Nginx 설치 (ubuntu)

그렇다면 nginx를 AWS에 설치하는 과정을 알아보자 :sunglasses:

##### 설치 및 제거

```
sudo apt-get install nginx # 설치
sudo apt-get remove nginx # 제거
nginx -v: nginx/1.13.2 # 확인
```

위에서와 같이 `apt-get` 명령어를 이용해 설치할 경우 경로는 `/etc/nginx` 폴더에 설치된다. 다음과 같은 명령어로 경로를 찾아볼 수 있다

```
sudo find / -name nginx.conf
```



### 03. Nginx directory 구조

```text
├── conf.d # (디렉토리) nginx.conf에서 불러들일 수 있는 파일을 저장
├── fastcgi.conf # (파일) FastCGI 환경설정 파일
├── fastcgi_params
├── koi-utf
├── koi-win
├── mime.types
├── nginx.conf # 접속자 수, 동작 프로세스 수 등 퍼포먼스에 관한 설정들
├── proxy_params
├── scgi_params
├── sites-available # 비활성화된 사이트들의 설정 파일들이 위치한다.
│   └── default
├── sites-enabled # 활성화된 사이트들의 설정 파일들이 위치한다. 존재하지 않은 경우에는 디렉토리를 직접 만들 수도 있다.
│   └── default -> /etc/nginx/sites-available/default
├── snippets
│   ├── fastcgi-php.conf
│   └── snakeoil.conf
├── uwsgi_params
└── win-utf
```



### 04. Nginx.conf 튜닝

 `nginx.conf` 파일에서 설정 값을 통해 Nginx가 동작해야할 방식을 설정할 수 있다.

단 설정을 한 후 nginx에 반영하기 위해선 reload 명령이 필요하다

```
sudo service nginx reload;
```



#### 1. 최상단 (core 모듈)

```python
user  nginx; # (디폴트값 : www-data) 
worker_processes  1;
error_log  /var/log/nginx/error.log warn;
pid        /var/run/nginx.pid;
```

`user` : 워커 프로세스의 권한을 지정하는 명령어이다. 

`worker_process` : nginx 프로세스 실행 가능 수를 의미한다. 워커 프로세스의 숫자를 정하는 것인데 auto도 무방하지만 명시적으로 서버에 장착되어 있는 코어 수 만큼 할당하는 것이 보통이며 이보다 더 높게 설정도 가능하다고 한다

`pid` : nginx 마스터 프로세스 ID 정보가 저장된다



#### 2. events block

```python
events { 
    worker_connections  1024;
    # multi_accept on; (디폴트값 : off) 
}
```

 `worker_connections` : 하나의 프로세스가 처리할 수 있는 커넥션을 의미 한다

결국 최대 접속자 수 = worker_processes * worker_connections



#### 3. http block

```python
http { 
    include       /etc/nginx/mime.types;
    default_type  application/octet-stream;
 
    log_format  main  '$remote_addr - $remote_user [$time_local] "$request" '
    '$status $body_bytes_sent "$http_referer" '
    '"$http_user_agent" "$http_x_forwarded_for"';
 
    access_log  /var/log/nginx/access.log  main;
 
    sendfile        on;
 
    #tcp_nopush     on; 
 
    keepalive_timeout  65;
 
    #gzip  on; 
 
    include /etc/nginx/conf.d/*.conf;
}
```

`keepalive_timeout` : 접속시 커넥션을 몇 초동안 유지할 것인지를 의미. 해당 값이 높으면 불필요한 커넥션을 유지하기 때문에 낮은값 or 0을 권장 (default = 10)

`gzip` : 성능 개선을 위해 `LZ77` 과 `허프만 코딩`을 이용한 `DEFLATE` 알고리즘에 기반하여 압축하는 것

`tcp_nopush` : TCP_NOPUSH socket option 혹은 Linux TCP_CORK socket option 을 사용하거나 사용하지 않거나의 여부를 정의 합니다. sendfile() 이 사용될때만 사용이 가능

`types_hash_max_size`, `server_names_hash_bucket_size` : 호스트의 도메인 이름에 대한 공간을 설정하는 것으로 이 값이 낮을 경우 많은 가상 호스트 도메인을 등록한다거나, 도메인 이름이 길 경우 bucket 공간이 모자라 에러가 생길 수 있으므로 넉넉하게 설정



#### 4. etc

`include` : 가상 호스트 설정이나 반복되는 옵션 항목을 불러오는 방법



### 05. 프록시 서버 만들기

우리는 80포트로 요청이 왔을 때, 이 요청을 3000포트에 있는 프론트서버로 전달해야합니다. 이를 사용하기 위해 프록시서버를 이용합니다. 우선 명령어로 nginx를 설치했다는 전제하에 `/etc/nginx/sites-available` 로 이동합니다. ( compile로 했을 경우 해당 경로로 이동 )

`sudo vi node-server` 를 통해 파일을 열고 다음과 같이 작성합니다

```
server {
	listen 80;
	server_name [ip address];
	location / {
		proxy_pass http://127.0.0.1:[port]
	}
}
```

그 후, `sudo ln -s /etc/nginx/sites-available/node-server /etc/nginx/sites-enabled/ ` 명령어를 입력합니다.  `ln`의 경우 링크파일을 만드는 명령어입니다.

그러고 난 후 `/etc/nginx/sites-enabled/` 로 이동하여 `ls -al` 를 입력해봅니다. 위에서 만든 node-server가 있다면 잘 연결된 것입니다.

`sudo service nginx restart` 를 통해 Nginx 서버를 재시작합니다.

