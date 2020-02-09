[TOC]

# 0. 전체구조

![image-20200119170511498](C:\Users\mnoko\AppData\Roaming\Typora\typora-user-images\image-20200119170511498.png)

# 1. Controller

`@RestController` 로 생각하면 요청 url에 따라 적합한 `service`의 method를 이용하여 처리한다. 하지만 service method를 정의하지 않고 바로 controller에서 business logic을 처리하는 경우도 있다. 

```java
@RestController
@RequestMapping("/api/users")
public class ApiUserController {
  @Autowired
  private UserService userService;  // service의 method

  @PostMapping("/login")
  public ResponseEntity login(@RequestBody final Object UserInfo) {
      userService.login(userInfo));  // userService method
      return new ResponseEntity<>(HttpStatus.OK);
  }
}
```



# 2. Service

Business Logic을 처리하는 곳으로 `DAO`로 DB에 접근하고 `DTO`로 데이터를 전달받은 후, business logic을 처리하고 적절한 데이터를 반환한다. `@AutoWired Repository` 를 통해 해당 repository(DAO)에 정의된 method를 이용한다

```
@Service
public class UserService {
	@Autowired
	private USerRepository userRepository;
	
	public User check(UserDto userDto) {
		if (userDto)
	}
}
```



# 3. Repository(DAO)

**DAO: Data Access Object**

* 실제로 DB에 접근하는 객체

* Service와 DB를 연결하는 고리 역할

* SQL 또는 JPA를 통해 DB에 접근한 후 적절한 CRUD API를 제공한다

  ```java
   package com.web.curation.dao.user;
  
   import com.web.curation.model.user.User;
   import org.springframework.data.jpa.repository.JpaRepository;
  
  
   public interface UserDao extends JpaRepository<User, String> {
       User getUserByEmail(String email);
       User findUserByEmailAndPassword(String email, String password);
  
   }
  
  ```

  `User.getUserByEmail(email=email)` 같은 CRUD method를 정의하고 이를 하나의 객체로 묶어 놓은 개념 같다. 이 객체를 service에서 불러와서 method를 호출하면 DAO에 작성한 코드가 작동하는 방식



# 4. DTO (Data Transfer Object)

**dto package**

* 계층간 데이터 교환을 위한 객체(Java Beans)
  * DB에서 데이터를 얻어 Service 또는 Controller 등으로 보낼 때 사용하는 객체
  * logic이 없는 순수한 데이터 객체로 data와 해당 data에 접근을 위한 `getter/setter` 메소드를 가진다.
  * 프로젝트에서 `model/user/SignupRequest`, `model/user/AuthenticationRequest`
* `VO` vs `DTO`
  * VO는 DTO와 동일한 개념이지만 `read only` 속성을 가진다
  * VO는 특정한 비즈니스 값을 담는 객체이고, DTO는 layer간의 통신 용도로 오가는 객체(controller와 service간의 통신 용도로 오가는 객체?)



# 5. Entity Class

**domain package**

* 실제 DB의 테이블과 매칭되는 클래스
* express의 sequelize 느낌
* 프로젝트에서 `model/user/User.java`