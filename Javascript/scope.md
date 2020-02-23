# Scope

scope란 변수가 영향을 미칠 수 있는 범위를 의미한다. 예를들어 함수 스코프인 경우 해당 함수 내에서만 사용할 수 있고 블록 스코프인 경우 해당 블록 내에서만 사용할 수 있다.

###### function scope

```js
function callMe() {
    var name = "mnoko"
    console.log('my name is ' + name)
}

console.log(name);
// console>>
callMe()
// console>> my name is mnoko
```

######  

###### block scope

```js
flag = true
if (flag) {
    const age = 999
}
console.log(age)
// console>> age is not defined
```

######  

위처럼 외부 함수에선 내부 함수에 접근하지 못하지만 반대로 내부 함수에서는 외부 함수에 접근할 수 있다. 함수 내부에서 전역 변수를 가져다 쓸 수 있는 것을 생각해보면 쉽다.

```js
var name = "mnoko"
function callMe() {
    console.log('my name is ' + name)
}

callMe()
// console>> my name is mnoko
```

######  

또한 내부 함수에서 해당 변수를 찾지 못했을 때, 외부 함수에서 해당 함수를 하나씩 찾아가는데 이를 **스코프 체인**이라고 부른다

###### scope chain

```js
function f1() {
    var name = 'mnoko'
    function f2() {
        var age = 999
        function f3() {
            console.log('my name is ' + name + ' and i am ' + age + ' years old')
        }
        f3()
    }
    f2()
}
f1()

// console>> my name is mnoko and i am 999 years old
```

######  

그렇다면 이러한 스코프는 함수를 선언할 때 생길까 아니면 함수를 호출할 때 생길까? 다음 예시를 보자. 함수 f1이 호출될 때, 바로 상단에 있는 "zaqwes"를 사용할 것 같지만 함수가 선언될 때의 "mnoko"를 사용하고 이러한 것을 **Lexical scoping**이라고 한다. (정적 스코핑이라고 이해하자!)

###### Lexical Scoping

```js
var name = 'mnoko'

// 함수 선언
function f1() {
    console.log(name)
}

// 함수 호출
function f2() {
    var name = "zaqwes"
    f1()
}
f2()

// console>> mnoko
```

######  

그런데 이러한 스코핑 방법 때문에 문제가 발생할 수 있다. 다음과 같은 상황을 가정해보자. 두 명의 개발자 A와 B가 코드를 작성하고 있다. 먼저 A가 전역변수 name을 사용하는 함수 f1을 정의했다. 그리고 다른 로직을 작성하다가 B가 전역변수 name을 사용하는 함수 f2를 사용했다. 나중에 A가 f1을 통해 name을 출력했을 때, 자신이 만들어놓은 변수가 아닌 다른 변수가 출력되는 상황이 발생한다.

###### 전역변수 사용시 문제점

```js
var name = "mnoko"
function f1() {
    console.log(name)
}

// ... some logic

var name = "zaqwes"
function f2() {
    console.log(name)
}

f1()
f2()

// console>> zaqwes
// console>> zaqwes
```

######  

이러한 상황이 발샐할 수 있기 때문에 전역변수를 만드는 것은 지양해야한다. 변수가 의도치않게 다른 변수로 덮어 씌워질 수 있기 때문이다. 이러한 문제를 해결하기 위해 전역 변수 대신 함수 안에 넣어 지역변수로 만들거나 객체 안의 속성으로 만들 수 있다. 

###### 네임스페이스

```js
var A = {
    name: "mnoko",
    f1: function() {
        console.log(this.name)
    }
}

var B = {
    name: "zaqwes",
    f2: function() {
        console.log(this.name)
	}
}

A.f1()
B.f2()

// console>> mnoko
// console>> zaqwes
```

######  

하지만 네임스페이스 또한 해당 객체의 값을 수정할 수 있기 때문에 문제가 발생할 수 있다. 따라서 변수의 수정 자체를 막는 방법은 다음과 같다

###### 비공개 변수

```js
var foo = function() {
    var name = "mnoko"
    var age = 999
    function sayName() {
        console.log(name)
    }
    function sayAge() {
        console.log(age)
    }
    return { sayName, sayAge }; // == { sayName: sayName, sayAge: sayAge }
}

var A = foo()
A.sayName()
A.sayAge()

// console>> mnoko
// console>> 999
```

이렇게 사용하면 foo 함수 내부에 있는 name과 age는 비공개 변수가 된다. 그리고 해당 비공개 변수는 sayName과 sayAge라는 공개 변수를 이용하여 확인만 가능하다. (수정 불가)

######  

한편 위의 코드를 `IIFE` (즉시 호출 함수 표현식)으로 간단하게 표현할 수 있다. 또한 이러한 방법을 **묘듈 패턴**이라고 한다.

###### IIFE

```js
var foo = (function() {
    var name = "mnoko";
    var age = 999
    return { 
        sayName: function() { console.log(name) },
        sayAge: function() { console.log(age) }
    }
})();

foo.sayName()
foo.sayAge()

// console>> mnoko
// console>> 999
```

