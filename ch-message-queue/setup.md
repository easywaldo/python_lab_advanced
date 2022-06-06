
### 설치 가이드
```shellß
brew install rabbitmq
```
[참고문서](https://sarc.io/index.php/osx/733-macos-rabbitmq)

[실행시 오류 해결](https://github.com/laradock/laradock/issues/2048)
> 아래의 오류가 발생하는 경우 
> {"Cookie file /Users/leejinam/.erlang.cookie must be accessible by owner only",
> 아래의 커맨드를 실행하여 해당 디렉터리를 삭제한다.
> rm .erlang.cookie

[rabbit-mq 프로듀싱-컨슈밍 예제](https://www.rabbitmq.com/tutorials/tutorial-one-python.html)