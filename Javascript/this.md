# 1. this

일반적으로 this에 바인딩되는 객체는 **함수를 호출할 때 함수가 어떻게 호출되었는지에 따라 동적**으로 결정된다. 함수가 호출되는 방식은 다음과 같다.

> 1. 함수 호출
> 2. 메스드 호출
> 3. 생성자 함수 호출



## 1. 함수호출

일반적으로 함수를 호출할 경우 this는 전역객체를 의미한다.

```js
const foo = function () {
    console.log('this is ', this)
}

foo(); // Object [global] 
       // 브라우저에서는 window
```



함수 안에 있는 내부함수에서 함수를 호출했을 때, 바로 밖에 있는 함수를 this로 바인딩할 것 같지만 전역 객체를 this로 바인딩한다.

```js
function A() {
    console.log("A's this: ", this);
    function B() {
        console.log("B's this: ", this);
    }
    B();
}
A();
// console>> A's this: window
// console>> B's this: window
```



obj의 method인 `callname` **안**에 있는 함수 callme2(내부함수) 에서는 this로 전역객체를 잡는다.

하지만 내부함수를 `arrow function`로 사용할 경우 상위 스코프인 obj에 바인딩된다

```js
var name = 'mnoko'

var obj = {
	name: 'zaqwes',
    callname1: function() {
		console.log('callname1 :', this.name)
        const callme2 = function() {
            console.log('callname2:', this.name)
        }
        const callme3 = () => {
            console.log('callname3 :', this.name)
        }
        callme2();
        callme3();
    }
}

obj.callname1()
// console>> callname1 : zaqwes
// console>> callname2 : mnoko
// console>> callname3 : zaqwes
```



**콜백함수** 의 경우에도 this로 전역객체를 잡는다

```js
var cnt = 1;

var obj = {
    cnt: 100,
    foo: function() {
        setTimeout(function() {
            console.log("callback's cnt :", this.cnt);
        }, 100);
    }
}

obj.foo();
// console.log>> callback's cnt: 1
```



## 2. 메소드 호출

한편 함수가 객체의 메소드로서 호출되면 해당 객체에 this가 바인딩된다.

```js
const p1 = {
    name: "mnoko",
    sayName: function() {
        console.log(this.name);
    }
}

const p2 = {
    name: "zaqwes"
}

p2.sayName = p1.sayName;

p1.sayName();
p2.sayName();

// console>> mnoko
// console>> zaqwes
```



## 3. 생성자 함수 호출

우선 생성자란 객체를 생성하는 것을 의미한다. js에서는 기존 함수에 new를 붙여서 호출하면 해당 함수는 생성자 함수로 동작한다. 이렇게 생성자 함수로 호출이 되면 this는 반환된 인스턴스에 바인딩된다.

```js
function Person(name) {
    this.name = name;
}

var p1 = new Person("mnoko");
var p2 = Person("zaqwes");
console.log("p1's name :", p1.name);
console.log("p2's name :", p2);

// console>> p1's name : mnoko
// console?? p2's name : undefined
```



참고로 생성자 함수에 의해 인스턴스가 생성되는 과정은 다음과 같다

> 1. 빈 객체 생성 및 this 바인딩
>
>    생성자 함수의 코드가 실행되기 전 빈 객체가 생성된다. 이 빈 객체가 생성자 함수가 새로 생성하는 객체이다. 이후 **생성자 함수 내에서 사용되는 this는 이 빈 객체를 가리킨다.** 그리고 생성된 빈 객체는 생성자 함수의 prototype 프로퍼티가 가리키는 객체를 자신의 프로토타입 객체로 설정한다.
>
> 2. **this를 통한 프로퍼티 생성**
>
>    생성된 빈 객체에 this를 사용하여 동적으로 프로퍼티나 메소드를 생성할 수 있다. this는 새로 생성된 객체를 가리키므로 this를 통해 생성한 프로퍼티와 메소드는 새로 생성된 객체에 추가된다.
>
> 3. 생성된 객체 반환
>
>    (1) 반환문이 없는 경우, this에 바인딩된 새로 생성한 객체가 반환된다. 명시적으로 this를 반환하여도 결과는 같다.
>
>    (2) 반환문이 this가 아닌 다른 객체를 명시적으로 반환하는 경우, this가 아닌 해당 객체가 반환된다. 이때 this를 반환하지 않은 함수는 생성자 함수로서의 역할을 수행하지 못한다. 따라서 생성자 함수는 반환문을 명시적으로 사용하지 않는다.



## 4. 결론 

자바스크립트에서 `this` 는 다음과 같은 것들이 될 수 있다.

1. 전역객체 (일반함수, 내부함수, 메소드 안의 함수)
2. 객체 자기 자신 (생성자 함수에 의해 생성된 객체, 메소드 안)
3. 상위 스코프의 this (화살표 함수)
4. 모든 것!!! (call, apply, bind를 사용하면 모든 것이 this가 될 수 있다)



## 5. call, apply, bind

이렇게 this는 함수가 어떤 방식으로 호출되느냐에 따라 달라지는데 자신이 원하는 것을 this로 설정할 수 있다.

### 1. call, apply

우선 call과 apply는 함수를 호출해 실행시킨 다는 것이 특징이다. 또한 인자가 없다면 this는 전역객체를 가리킨다

```js
obj1 = {
    name: "mnoko",
    callme: function() {
        console.log(this.name)
    }
}

obj2 = {
    name: "zaqwes"
}

obj1.callme();
obj1.callme.call()
obj1.callme.call(obj2)

// console>> mnoko
// console>> mnoko
// console>> zaqwes
```



### 2. bind

이와 다르게 bind의 경우 함수를 호출하지 않고 반환만 한다

```js
var name = "global name"

obj1 = {
    name: "mnoko",
    callme: function() {
        console.log(this.name)
    }
}

obj2 = {
    name: "zaqwes"
}


obj1.callme.apply();

f1 = obj1.callme.bind(obj2)
f1()

f2 = obj1.callme.bind();
f2()

// console>> global name
// console>> zaqwes
// console>> global name
```

