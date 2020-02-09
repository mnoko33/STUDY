# 1. Mongodb 설치하기

1. [MongoDB Download Center](https://www.mongodb.com/download-center?)
2. `Community Server` 에서  windows 버전으로 .msi 파일을 다운로드
3. install
   1. setup Type에서 `complete` 와 `custom` 이 있다. 
      * `complete` : 기본 경로인 `C:\Program Files` 에 설치
      * `custom` :  본인이 원하는 경로에 설치
   2. 설치 중 run as a service 부분을 기본 설정을 진행할 경우 환경 설정을 할 필요가 없다.
   3. `MongoDB Compass` : GUI 버전인데 무시하고 나중에 Robo를 설치
4. 환경설정 (3-2에서 클릭을 해제했을 경우만... 하지 말자)
   1. 경로 속에 mongod라는 실행파일이 있는데 직접 경로로 들어가지 않아도 실행할 수 있도록 환경변수를 추가
   2. 환경변수 편집으로 가서 PATH에 `C:\Program Files\MongoDB\Server\4.2\bin` 를 추가
   3. 여기서 cmd에서 `mongod`를 입력하면 NoExistentPath 에러가 발생
   4. `C:\data\db\`  폴더가 없는 것이기 때문에 이를 생성

