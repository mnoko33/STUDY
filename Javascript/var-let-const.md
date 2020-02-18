# var, const, let

|          | var              | const            | let              |
| -------- | ---------------- | ---------------- | ---------------- |
| scope    | 함수 레벨 스코프 | 블록 레벨 스코프 | 블록 레벨 스코프 |
| 재할당   | 가능             | 불가능           | 가능             |
| hoisting | O                | X                | X                |



## 1. 자바스크립트 변수 선언

자바스크립트에서 변수 선언하기

```js
// ES5
var name = "mnoko"

// ES6
const age = 100
let job = "student"
```



## 2. var, let, const

### 01. scope

`var` 는 기본적으로 **함수 레벨 스코프**를 가진다. 함수 레벨 스코프의 경우 함수 내에서 선언된 변수는 함수 내에서만 유효하며 함수 외부에서 참조할 수 없다. 즉, 함수 내부에서 선언한 변수는 지역 변수이며 함수 외부에서 선언한 변수는 모두 전역 변수이다.

반면 `let` 과 `const` 의 경우 **블록 레벨 스코프**를 가진다. 즉 `{}` 안에서만 변수가 유효하다. 이렇게 할 경우 의도치 않은 변수 변경으로 인한 에러를 막을 수 있다.

```js
// var, const, let
function callMe(name) {
    if (name) {
        console.log('my name is ' + name);
    } else {
        var errMsg1 = "this is var!!"
        let errMsg2 = "this is let!!"
    }
    console.log(errMsg1)
    console.log(errMsg2)
}

callMe()
// console>> this is var!!
// console>> ReferenceError: errMsg2 is not defined
```



### 02. hoisting

`var`를 사용할 경우 변수를 선언하기 이전에도 해당 변수를 사용할 수 있는 호이스팅 현상이 발생한다. 하지만 `let` 과 `const`의 경우 호이스팅 현상이 발생하지 않아 의도치 않은 실수를 줄일 수 있다.



> Hoisting

호이스팅이란 `var`를 이용하여 변수 또는 함수를 선언했을 때, 선언된 변수가 최상위로 끌어올려져 사용할 수 있어지는 현상을 의미한다. 이러한 현상은 자바스크립트가 코드를 실행하기 전에 가장 먼저 `var`와 `function`을 찾아서 스코프의 최상단에 변수와 함수를 미리 등록하기 때문에 발생한다. 이러한 이유로 변수 선언을 하지 않고 값을 초기화해도 에러가 발생하지 않는다. 

###### var

```js
name1 = "mnoko";
console.log('my name is ' + name1);
var name1

//console>> my name is mnoko
```

###### let

```js
name2 = "zaqwes";
console.log('my name is ' + name2);
let name2

//console>> ReferenceError: Cannot access 'name2' before initialization
```



### 3. 중복선언과 재할당

|           | var  | const | let  |
| :-------: | :--: | :---: | :--: |
| 중복선언  |  O   |   X   |  X   |
| immutable |  O   |   X   |  O   |

```js
// var
var name1 = "lee"
var name1 = "kim" 		// 중복선언
name1 = "lee" 			// 재할당

// const
const name2 = "park"
const name2 = "pak" 	// 중복선언 X
name2 = "park"			// 재할당 X

// let
let name3 = "kwon"	
let name3 = "choi"		// 중복선언 X
name3 = "lee" 			// 재할당 O
```



### 4. 클로저 관련

우선 클로저는 함수가 선언됐을 때의 렉시컬 환경(Lexical Environment)과의 조합...이다.....???

일단 해당 함수가 생성될 때의 환경을 기억하는 것이라고 생각하자. 그렇다면 이 클로저가 변수 선언과 어떤 관계가 있을까?

우선 for문을 돌면서 인덱스 값을 인자로 가지는 함수를 배열에 넣어준다. 그리고 해당 배열을 돌면서 함수를 실행했을 때, 함수를 선언할 때 인자로 넘기는 값을 출력할 것 같지만 실제로 그렇게 작동하지 않는다

```js
var funcs = [];

for (var i = 0; i < 3; i++ ){
    funcs.push(function() {console.log(i)})
}

funcs.forEach((func) => {func()})

// console>> 3
// console>> 3
// console>> 3
```

왜 그럴까?🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔🤔

이러한 결과가 발생하는 이유는 `i`가 전역 변수이기 때문이다. 즉 func 안에 push된 함수들이 전역 변수를 바라보고 있기 때문에 호출됐을 때 3이 되어버린 전역변수 i를 출력한다.

이러한 문제를 해결하기 위한 방법이 바로 `closure` 이다. 클로저는 함수가 선언됐을 때의 환경을 기억하게 하는 것이니 결국 함수가 선언됐을 때 i 값을 기억하고 그 i를 호출됐을 때 사용하도록 하는 것이다.

```js
var funcs = [];

for (var i = 0; i < 3; i++) {
    ((j) => {
    	funcs.push(function() { console.log(j) })   // i값을 함수에 인자로 전달했기 때문에
    })(i)										    // 해당 함수는 전역변수 i가 아닌 넘겨받은
}												    // 인자 j를 호출됐을 때 사용한다

funcs.forEach((func) => {
    func()
})

// console>> 0
// console>> 1
// console>> 2
```

그렇다면 i가 전역변수이기 때문에 발생하는 이슈라면 전역변수가 아니면 클로저는 필요 없을 것이다. 즉 let을 사용하면 쉽게 구현할 수 있다. let은  for문 안에서만 유효한 지역 변수이기 때문이다. 또한 자유변수이기 때문에 for문이 끝났어도 이를 참조하는 함수가 존재하는 한 계속 유지된다. (const의 경우 재할당이 불가능하기 때문에 사용불가)

```js
var funcs = [];

for (let i = 0; i < 3; i++) {
    funcs.push(function() { console.log(i) })
}

funcs.forEach(func => {
    func()
})

// console>> 0
// console>> 1
// console>> 2
```