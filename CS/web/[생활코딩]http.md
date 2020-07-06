# HTTP 통신 과정

* HTTP는 인터넷 전송 프로토콜임.

![image](https://user-images.githubusercontent.com/46865281/71986278-8ad20600-326f-11ea-8aae-9de40f9a3ec8.png)

* web이 존재하기 위해서 최소한 두 대의 컴퓨터가 필요함, **클라이언트**와 **서버**
* 웹의 동작은 클라이언트가 TCP 프로토콜로 서버로부터 html을 요청하고, 서버가 이를 응답하는 통신 과정
* 더 구체적으로 이 과정을 서술하자.
  1. 유저는 클라이언트 컴퓨터에 설치된 웹 브라우저(IE, chrome, firefox) 라는 소프트웨어에 도메인 네임을 입력함
  2. 브라우저는 **DNS 서버**로 가서 **도메인 네임**과 **IP 주소**(웹 서버의 논리적 주소)를 변환함
  3. 브라우저는 이 주소로 해당 웹 서버로 감
  4. html 문서의 사본을 요청(SYN) -> 서버의 승인 및 준비 됐음(SYN-ACK) -> 클라이언트의 응답(ACK) 과정을 거침
  5. 위 과정은 통신의 **신뢰성 보장**을 위해 필요하며 **Handshake**라 함
  6. 서버는 클라이언트에게 데이터(html)를 보냄
  
* 위 과정을 **HTTP**(HyperText Transfer Protocol) 통신이라 함. 즉 HTTP는 말 그대로 html을 전송하는 프로토콜, 80 port

![image](https://images-wixmp-ed30a86b8c4ca887773594c2.wixmp.com/f/e0f95975-50d8-40f0-b4bd-419d10589d0a/d24ajgf-f899cb2a-4848-4b4a-87d3-7345e36405d1.jpg/v1/fill/w_1032,h_774,q_70,strp/how_internet_works_by_vladstudio_d24ajgf-pre.jpg?token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1cm46YXBwOjdlMGQxODg5ODIyNjQzNzNhNWYwZDQxNWVhMGQyNmUwIiwiaXNzIjoidXJuOmFwcDo3ZTBkMTg4OTgyMjY0MzczYTVmMGQ0MTVlYTBkMjZlMCIsIm9iaiI6W1t7ImhlaWdodCI6Ijw9MTIwMCIsInBhdGgiOiJcL2ZcL2UwZjk1OTc1LTUwZDgtNDBmMC1iNGJkLTQxOWQxMDU4OWQwYVwvZDI0YWpnZi1mODk5Y2IyYS00ODQ4LTRiNGEtODdkMy03MzQ1ZTM2NDA1ZDEuanBnIiwid2lkdGgiOiI8PTE2MDAifV1dLCJhdWQiOlsidXJuOnNlcnZpY2U6aW1hZ2Uub3BlcmF0aW9ucyJdfQ.jIXoBTe0CJuKJVhnDwiXbk3EfEF6z-kQVduMojmhz_k)
