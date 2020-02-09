## 자바스크립트 엔진

자바스크립트 엔진은 다음과 같은 두 가지 구성 요소로 이루어져 있다.

> **메모리 힙 (Memory Heap)**
>
> 객체와 변수에 대한 메모리 할당

> **호출 스택 (Call Stack)**
>
> 코드가 실행될 때 호출 스택이 쌓인다

###  

## 실행 환경 (브라우저)

이러한 자바스크립트는 브라우저 (또는 노드) 에서 실행된다. 따라서 자바스크립트가 직접 제공하지는 않지만 브라우저에서 제공하는 다양한 웹 api (DOM, ajax, setTimeOut 등...) 을 사용할 수 있다. 그리고 이러한 웹 api를 관리하기 위해 브라우저에는 `Event Queue` 와 `Event Loop` 가 존재한다.

###    

## 호출 스택 (Call Stack)

자바스크립트는 싱글 스레드 프로그래밍 언어이므로 단일 호출 스택이 있다. 즉 한 번에 하나의 일을 처리할 수 있다. 결과적으로 코드가 실행되면서 함수를 실행할 때, 해당 함수는 스택에 push된다. 그리고 함수의 결과값을 반환하면 스택에 쌓여있던 함수는 pop된다. 아래는 함수 예제와 호출 스택에서 push와 pop이 발생하는 과정이다.

```javascript
function multiply(x, y) {
    return x * y;
}
function getSquare(x) {
    var s = multiply(x, x);
    console.log(s);
}
getSquare(5);
```

#####  

###### 1. 함수 getSquare(5)이 호출 스택에 push - 함수 multiply가 먼저 나오지만 이는 함수 선언부일 뿐 실행은 아직 되지 않았기 때문에 getSquare가 가장 우선 스택에 쌓인다.

> ###### [ getSquare(5) ]

###### 2. 함수 getSquare가 실행되고 그 다음으로 multiply(x, x) 함수가 실행되고 그 다음 스택에 쌓인다.

> ###### [ getSquare(5), multiply(x, x) ]

###### 3. multiply(x, x) 함수가 끝나고 return 값이 s에 할당된 후, 스택에 있는 해당 함수는 제거된다.

> ###### [ getSquare(5) ]

###### 4. 그 다음 console.log(s) 가 실행되어 스택에 쌓이고, s 값을 출력한 후 스택에서 제거된다.

> ###### [ getSquare(5), console.log(s) ] > [ getSquare(5) ]

###### 5. 최종적으로 getSqure(5) 함수도 스택에서 제거된다.

> ###### [ ]

###   

또한 이러한 스택의 호출 과정은 예외 (Error) 가 발생했을 때 확인할 수 있다.

```javascript
function foo() {
    throw new Error('Error is occurred');
}
function bar() {
    foo();
}
function start() {
    bar();
}
start();
```

위의 코드는 다음과 같은 결과를 보여준다. 

> Uncaught Error: SessionStack will help you resolve crashes :)
>     at foo (<anonymous>:3:11)
>     at bar (<anonymous>:6:5)
>     at start (<anonymous>:10:5)
>     at <anonymous>:15:1

해당 에러가 foo 함수에서 발생했고, 해당 함수는 bar 함수 내에서 실행됐고, 그 함수는 start 함수내에서 실행된 것으로 확인할 수 있다. 즉 Call Stack에 함수가 실행될 때마다 기록했기 때문에 특정 오류가 발생했을 때, 이 오류가 어떤 함수로부터 시작됐는지 확인할 수 있다.

###  

## 싱글 스레드 문제점과 해결책

싱글 스레드는 하나의 작업을 하나씩 수행한다. 이로 인해 멀티 스레드와 다르게 `Dead Lock` 이 발생할 일이 없다. 

>  **Dead Lock**
>
> 한정된 자원을 여러 개의 프로세스가 사용하려고 할 때 발생하는 교착 상태. 프로세스1이 자원 a를 사용 중이고 프로세스2가 자원 b를 사용 중일 때, 프로세스1이 자원 b를 사용하기 위해 대기하고 프로세스2가 자원 a를 이용하기 위해 대기하고 있을 때, 두 프로세스는 실행 상태로 변경될 수 없고 이것을 교착 상태라고 한다.

하지만 브라우저에서 자주 사용되는 자바스크립트 엔진은 싱글 스레드이기 때문에 큰 문제가 존재한다. 만약 브라우저가 싱글 스레드로 작동한다면 화면을 그리던 중 시간이 오래걸리는 작업을 할 때, 이 작업을 하는 동안 나머지 화면이 그려지지 않고 결과적으로 유저는 멈춰있는 화면을 보고 있어야한다. 이러한 상황을 해결하기 위해 비동기 콜백 `Asynchronous callbacks` 을 이용한다. 비동기 콜백이란 콜백 함수를 바로 스택에 push하는 것이 아니라 나중에 쓸 수 있도록 콜백 큐 `callback Queue` 에 push한다.

브라우저는 `DOM 이벤트` , `http 요청` , `setTimeout` 등과 같은 비동기 함수인 web api가 호출되면 call stack이 아닌 이벤트 큐 `Event Queue` (`callback Queue`) 에 push한다. 이벤트 루프 `Event Loop` 는 스택과 큐를 지켜보다가 스택이 비는 시점에 큐에 있는 콜백 함수를 스택에 push한다.



