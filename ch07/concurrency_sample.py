"""
Concurrency (동시성)

- CPU 가용성 극대화 위해 Paralleism 의 단점 및 어려움을 소프트웨어(구현) 레벨에서 해결하이 위한 방법
- 싱글 코어에 멀티스레드 패턴으로 작업을 처리
- 동시 작업에 있어서 일정량 처리 후 다음 작어븡로 넘기는 방식
- 즉 제어권 주고 받으며 작업 처리 패턴, 병렬적은 아닌, 유사한 처리 방식

동시성 : 논리적, 동시실행패턴(논리적), 싱글코어, 멀티코어에서 실행 가능, 한개의 작업 공유처리, 디버깅
병렬성 : 물리적, 물리적으로 동시 실행, 멀티코어에서 구현 가능, 주로 별개의 작업 처리, 디버깅 어려움
"""

"""
CPU Bound vs I/O Bound - Blocking VS Non-Blocking IO
Keyword - Blocking IO, Non-Blocking IO, Sync, Async


blocking IO vs Non-blocking IO
    blocking IO
    - 시스템 콜 요청 시 -> 커널 IO 작업 완료 시 까지 응답 대기
    - 제어권(IO작업) -> 커널 소유 -> 응답(Response) 전 까지 대기(Block) -> 다른 작업 수행 불가(대기)
    
    Non-blocking IO
    - 시스템 콜 요청 시 -> 커널 IO 작업완료 여부 상관없이 즉시 응답
    - 제어권(IO작업) -> 유저프로세스 -> 다른 작업 수행가능(지속) -> 주기적으로 시스템 콜 통해서 IO 작업 완료여부 확인
    
    Async vs Sync
        Async : IO 작업 완료 여부에 대한 Noty 는 커널(호출되는 함수) -> 유저프로세스(호출하는 함수)
        Sync : IO 작업
"""


