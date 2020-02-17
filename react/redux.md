[TOC]

# Redux

### 1. Store

상태가 저장되어 있는 곳



### 2. Action / Action Creator

`Action` 

* Store에 무엇인가 변화를 주고 싶은 경우 Action을 발행

* store의 문지기가 Action의 발생을 감지하면 state가 갱신

* action의 형태

  ```js
  {
      type: "액션의 종류를 식별할 수 있는 문자열 or 심볼",
      payload: "액션의 실행에 필요한 데이터"
  }
  ```

`Action Creator`

* 이러한 action을 발행해주는 것이 action creator이다.

  ```js
  export const addValue = amount => ({
      type: ADD_VALUE,
      payload: amout
  });
  ```



### 3. Reducer

store의 문지기와 비슷한 역할을 하는 존재로 이전 상태와 Action을 합쳐 새로운 state를 만드는 조작을 의미

```react
import { ADD_VALUE } from './actions';

export default (state = {value:0}, action) => {
    switch (action.type) {
        case ADD_VALUE:
            return { ...state, value: state.value + action.payload }
    };
    default:
    	return state; 
}
```

여기서 state안에 value를 새로운 값으로 바꾸는 것이 아니라 기존의 state가 아닌 새로운 값을 가진 state로 아예 바꾸는 것이다.

> **`combineReducers`**
>
> Reducer를 미세하게 분할하고 싶은 경우 redux에서 제공하는 `combineReducers` 함수를 활용할 수 있다.



### 4. Connect

React의 component는 Redux에 바로 적용할 수 없다. 따라서 ReactRedux에서 제공하는 `connect` 함수를 이용한다.

* `함수형 Component`

  ```react
  import React from 'react';
  import { connect } from 'react-redux';
  import { addValue } from './actions';
  
  const Counter = ({ value, dispatchAddValue }) => (
      <div>
          Value: {value}
          <a href="#" onClick={e => dispatchAddValue(1)}>+1</a>
          <a href="#" onClick={e => dispatchAddValue(2)}>+2</a>
      </div>
  );
  
  export default connect(
      state => ({ value: state.value }),
      dispatch => ({ dispatchAddValue: amount => dispatch(addValue(amount)) })
  )(Counter)
  ```

* `클래스형 Component`

  ```react
  import React, { Component } from 'react';
  import { connect } from 'react-redux';
  import { addValue } from './actions';
  
  class Counter extends Component {
      render() {
          const { value, dispatchAddValue } = this.props;
          return (
              <div>
                  Value: {value}
                  <a href="#" onClick={e => dispatchAddValue(1)}>+1</a>
                  <a href="#" onClick={e => dispatchAddValue(2)}>+2</a>
              </div>
          );
      }
  }
  
  export default connect(
      state => ({ value: state.value }),
      dispatch => ({ dispatchAddValue: amount => dispatch(addValue(amount)) })
  )(Counter)
  ```



> **`component와 props`**
>
> component가 store로부터 정보를 받을 때, `props`로 받는다. 이 props는 immutable하다. 따라서 props만 변경되는 것이 아니라, 상태가 변경될 때마다 새로운 component를 그리는 것이다. 

* `mapStateToProps` : store에 있는 `state`를 `props`로 만드는 함수
* `mapDispatchToProps` : Reducer에서 action을 알리는 함수 `dispatch`를 `props`에 연결하는 함수
* 이 두 가지가 적용된 props를 받을 component를 정한다



`bindActionCreator`

```react
import React, { Component } from 'react';
import { bindActionCreators } from 'redux';
import { connect } from 'react-redux';
import { addValue } from './actions';

const Counter = ({ value, addValue }) => (
    <div>
        Value: {value}
        <a href="#" onClick={e => addValue(1)}>+1</a>
        <a href="#" onClick={e => addValue(2)}>+2</a>
    </div>
);

export default connect(
    state => ({ value: state.value }),
    dispatch => bindActionCreators({ addValue }, dispatch)
)(Counter)
```

다음과 같이 간략하게 작성도 가능하다

```react
import React, { Component } from 'react';
import { connect } from 'react-redux';
import { addValue } from './actions';

const Counter = ({ value, addValue }) => (
    <div>
        Value: {value}
        <a href="#" onClick={e => addValue(1)}>+1</a>
        <a href="#" onClick={e => addValue(2)}>+2</a>
    </div>
);

export default connect(
    state => ({ value: state.value }),
    { addValue }
)(Counter)
```



