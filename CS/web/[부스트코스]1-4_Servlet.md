## Servlet - BE

### 서블릿에 대한 이해

* 자바 웹 어플리케이션
  * WAS에 설치되어 동작하는 어플리케이션
  * 자바 웹 어플리케이션에는 html, css, 이미지, 자바로 작성된 클래스, 각종 설정 파일 등이 포함됨
  * 폴더 구조
    * WEB INF 폴더
      * lib 폴더: jar 파일
      * classes 폴더: java 패키지, class들
    * web.xml(배포기술자, 3.0 이상은 어노테이션 대체)
      * web.xml은 특정 url 이 클라이언트로부터 들어 왔을 때 해당 서블릿을 매핑해주는 역할을 함. 여기 없으면, 404 에러가 나옴
    * 스프링 쓸 때는 필요할듯
    * 리소스: 각종 폴더, 이미지, 다양한 리소스들
  
* Servlet 이란?

  * 자바 웹 어플리케이션의 구성요소 중 동적인 처리를 하는 프로그램

  * 정의

    * WAS에서 동작하는 자바 클래스

    * HttpServlet 클래스를 상속받아야 함

    * Servlet 과 JSP 로부터 최상의 결과를 얻으려면, 웹 페이지를 개발할 때 이 두 가지를 조화롭게 사용해야 한다.

      예: 웹 페이지를 구성하는 화면(html)은 jsp로 표현하고, 복잡한 프로그램은 서블릿으로 구현

      

### 서블릿 작성법

* Servlet 3.0 미만에서 사용하는 방법
  * Servlet 을 등록할 때 web.xml 파일에 등록



* Servlet 3.0 이상에서 사용 하는 방법
  * web.xml 파일 대신 자바 어노테이션 사용



* 실습 중 중요한 부분

  * 프로젝트 만들 때 Content root, Servlet 만들 때 url mapping 이름에 따라 url 주소가 결정됨

  * 서블릿은 자바 웹 어플리케이션의 구성 요소 중 하나로, 동적으로 응답 결과를 처리하는 프로그램임. 이미 응답할 페이지를 만들어서 가지고 있는게 아니라, 요청이 들어 왔을 때 이 서블릿이 실행되며 응답할 코드를 만들어 내고 응답을 하는 것.

  * 서블릿 코드

    ```java
    @WebServlet("/ten")
    
    public class TenServlet extends HttpServlet {
    	private static final long serialVersionUID = 1L;
        public TenServlet() {
    	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    		// TODO Auto-generated method stub
    		response.setContentType("text/html;charset=utf-8");
    		PrintWriter out = response.getWriter();
    		out.print("<h1>1-10까지 출력!</h1>");
    		for(int i=1; i<11; i++) {
    			out.print(i+"<br>");
    		}
    		out.close();
    	}
    }
    ```

    * 클라이언트가 요청하면 서버는 응답함. 클라이언트가 요청할 때 서버는 요청을 받아내는 객체와 응답을 하기 위한 객체를 디폴트로 만들어 냄. 
    * 요청은 위 코드 내의 HttpServletRequest request 객체 내에 가지고 있고 응답은 HttpServletResponse response 객체에 가지고 있음.
    * 위 reponse.setContentType은 서버에서 전송하는 정보의 타입을 알려줌
    * 통로를 얻어내야 함. response.getWriter()은 PrintWriter를 리턴하는 메소드임
    * html이니까 `println` 으로 개행 불가, `<br>` 필요
    * `@WebServlet("/ten")` 이 부분이 어노테이션 인데, 값을 바꾸면 url mapping 을 바꿀 수 있음



* web.xml

  ```java
  xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd" 
  version="2.5">
      <display-name>exam25</display-name>
      <welcome-file-list>
          <welcome-file>index.html</welcome-file>
          <welcome-file>index.htm</welcome-file>
          <welcome-file>index.jsp</welcome-file>
          <welcome-file>default.html</welcome-file>
          <welcome-file>default.htm</welcome-file>
          <welcome-file>default.jsp</welcome-file>
      </welcome-file-list>
      <servlet>
          <description></description>
          <display-name>TenServlet</display-name>
          <servlet-name>TenServlet</servlet-name>
          <servlet-class>exam.TenServlet</servlet-class>
      </servlet>
      <servlet-mapping>
          <servlet-name>TenServlet</servlet-name>
          <url-pattern>/ten</url-pattern>
      </servlet-mapping>
  </web-app>
  ```

  * `url-pattern` 여기서 요청이 들어오면 url 매핑에서 찾고 있다면 `servlet-name` 이걸로 같은 이름의 서블릿이 있는지 찾음 `servlet-class` 이건 경로



### 서블릿 생명 주기

```Java
//... 생략

@WebServlet("/LifecycleServlet")
public class LifecycleServlet extends HttpServlet {	
	private static final long serialVersionUID = 1L;
       
    public LifecycleServlet() {
       System.out.println("LifecycleServlet 생성!!");
     }


    public void init(ServletConfig config) throws ServletException {
        System.out.println("init 호출!!");
	}

	public void destroy() {
		System.out.println("destroy 호출!!");
	}

	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
		System.out.println("service 호출!!");
	}
}
```

* **서블릿 라이프 사이클**

  * 위 코드는 HttpServlet의 3가지 메소드를 오버라이딩 함
  * **init()**, **service(request, response)**, **destroy()** + **생성자**

  1. 해당 url로 클라이언트가 서버한테 요청함.

  2. 서버는 url을 받아서 매핑된 서블릿을 찾음

  3. 이 클래스가 메모리에 존재함? 없다면(최초 실행) 객체를 생성 -> **생성자** 실행

  4. **init ** 실행

  5. **service** 호출

  6. 만약 브라우저를 새로고침 한다면, **service** 만 다시 호출됨

  7. 만약 서블릿을 수정한다면, 

     메모리에 올라가 있는 서블릿 객체는 사용할 수 없을 것이고, 따라서 **destroy** 호출됨

  8. 다시 1~5 시행

     

* **좀 더 이론**

  * <img src="https://user-images.githubusercontent.com/46865281/75983338-b568d400-5f2b-11ea-8b45-bd8144a0f5f3.png" alt="image" style="zoom:70%;" />

  * WAS는 서블릿 요청을 받으면 해당 서블릿이 메모리에 있는지 확인

  * ```
    if(메모리에 없음)
    {
    	* 해당 서블릿 클래스를 메모리에 올림(생성자)
    	* init() 메소드를 실행
    }
    * service() 메소드를 실행
    ```

  * WAS가 종료되거나, 웹 어플리케이션이 새롭게 갱신될 경우 `destroy()` 메소드가 실행됨

    

* **service(request, response) 메소드 동작**

  * 내가 만든 클래스가 서비스라는 메소드가 없는 경우 HttpServlet의 서비스 메소드를 실행. 직접 서비스를 만든 경우, Httpservlet의 서비스 메소드를 오버라이딩 한 것.

  * HttpServlet 서비스 메소드는 템플릿 메소드 패턴으로 구현되어 있음

    * 클라이언트 요청이  get인 경우 -> doGet 메소드 호출

    * 클라이언트 요청이 post인 경우 -> doPost 메소드 호출

      

* 실습 코드

  ```java
  //위와 동일
  
  	@Override
  	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
  		response.setContentType("text/html");
  		PrintWriter out = response.getWriter();
  		out.println("<html>");
  		out.println("<head><title>form</title></head>");
  		out.println("<body>");
  		out.println("<form method='post' action='/exam31/LifecycleServlet'>");
  		out.println("name : <input type='text' name='name'><br>");
  		out.println("<input type='submit' value='ok'><br>");                                                 
  		out.println("</form>");
  		out.println("</body>");
  		out.println("</html>");
  		out.close();
  	}
  
  	protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
  		System.out.println("실행됨");
  		response.setContentType("text/html");
  		PrintWriter out = response.getWriter();
  		String name = request.getParameter("name");
  		out.println("<h1> hello " + name + "</h1>");
  		out.close();
  	}
  
  //	protected void service(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
  //		System.out.println("service 호출!!");
  //	}
  
  ```

  * service 메소드 주석 처리 후 doGet, doPost 메소드 오버라이딩
  * Soruce -> Override/Implement Methods 선택
  * url에서 직접 요청할 때는 get으로 요청이 들어감. 위 코드에서는doGet 속의  form 태그에서 post를 요청함
  * 정확히, `		out.println("<form method='post' action='/exam31/LifecycleServlet'>");` 라고 요청하고 있음. 해당 메소드가 **post** 고, 서버의 어떤 위치에 있는지 명시함. url도 이곳이 됨.



### Request, Response 객체 이해하기

* HttpServletRequest, HttpServletResponse 이해하기

  <img src="https://user-images.githubusercontent.com/46865281/76078347-d3930a80-5fe5-11ea-94ae-ba6851991db9.png" alt="image" style="zoom:50%;" />
  * WAS는 클라이언트(웹 브라우저)로부터 servlet 요청을 받으면

    * HttpServletRequest 객체 생성, 요청할 때 가지고 있는 정보 저장
    * HttpServletResponse 객체 생성, 웹 브라우저에게 응답을 보낼 때 사용하기 위해서
    * 이 두 객체를 요청 정보의 path로 매핑된 서블릿에 전달함. 그럼 doGet 뭐 이런 메소드의 파라미터로 들어감

    

  * HttpServletRequest

    * http 프로토콜의 request 정보를 서블릿에게 전달하기 위한 목적으로 사용
    * 헤더 정보, 파라미터, 쿠키, url 등의 정보들을 읽고 저장하는 메소드를 가짐

    

  * HttpServletResponse

    * WAS는 요청을 보낸 클라이언트에게 다시 응답을 하기 위해 해당 객체를 생성해서 서블릿에게 전달
    * 서블릿은 해당 객체를 이용해서 content type, 응답 코드, 응답 메세지 등을 전송



* 실습: 헤더 정보 읽어 들이기

  * 웹 브라우저가 요청 정보에 담아서 보내는 헤더 값을 읽어들여 출력해보자.

    ```java
    	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    		response.setContentType("text/html");
    		PrintWriter out = response.getWriter();
    		out.println("<html>");
    		out.println("<head><title>form</title></head>");
    		out.println("<body>");
    
    		Enumeration<String> headerNames = request.getHeaderNames();
    		while(headerNames.hasMoreElements()) {
    			String headerName = headerNames.nextElement();
    			String headerValue = request.getHeader(headerName);
    			out.println(headerName + " : " + headerValue + " <br> ");
    		}		
    		
    		out.println("</body>");
    		out.println("</html>");
    	}
    
    ```

  * `request.getHeaderNames();` request 객체의 getheaderNames() 메소드는 헤더의 모든 이름을 enumeration 객체로 리턴해줌.

  * 해당 이름들을 `getHeader` 메소드에 넣어서 헤더 값을 리턴받음

  * 결과물

    ```html
    host : localhost:8080 
    connection : keep-alive 
    upgrade-insecure-requests : 1 
    accept : text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8 
    user-agent : Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Safari/522.0 
    accept-language : ko-kr 
    cache-control : no-cache 
    accept-encoding : gzip, deflate 
    ```

    

* 실습: 파라미터 읽어 들이기
  
  * `http://localhost:8080/firstweb/parm?name=kim&age=5` 물음표 기준으로 뒤에 있는 것들이 파라미터임. `&` 가 각 파라미터들의 기준점임.  `=` 을 기준으로 좌항이 이름, 우항이 값



* 실습: 다양한 요청 정보 출력

  ```java
  	protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
  		response.setContentType("text/html");
  		PrintWriter out = response.getWriter();
  		out.println("<html>");
  		out.println("<head><title>info</title></head>");
  		out.println("<body>");
  
  		String uri = request.getRequestURI();
  		StringBuffer url = request.getRequestURL();
  		String contentPath = request.getContextPath();
  		String remoteAddr = request.getRemoteAddr();
  		
  		
  		out.println("uri : " + uri + "<br>");
  		out.println("url : " + url + "<br>");
  		out.println("contentPath : " + contentPath + "<br>");
  		out.println("remoteAddr : " + remoteAddr + "<br>");
  		
  		out.println("</body>");
  		out.println("</html>");
  	}
  ```

  * 결과물

    ```java
    uri : /exam31/info
    url : http://localhost:8080/exam31/info
    contentPath : /exam31
    remoteAddr : 0:0:0:0:0:0:0:1
    ```

    

  * URI, URL, PATH, Remote host 등에 대한 정보 출력

    1. URI ( Uniform Resource Identifier)
       * 자원 식별자, 정보를 구별하는 인터넷에 있는 자원을 나타내는 유일한 주소.
       * URI는 URL, URN을 포함하는 큰 개념임
    2. URL ( Uniform Resource Locator)
       * 자원(파일) 위치
       * 특정 서버의 한 리소스에 대한 구체적인 위치
       * 예컨대, `http://localhost:8080/firstweb/pram?name=kim&age=5` 여기서 URL은 `pram` 전까지임. 위 주소는 URI지만 URL은 아님 내가 원하는 정보를 얻기 위해 식별자를 추가한 것이기 때문 

    3. URN(Uniform Resource Name)
       * 리소스의 위치에 영향을 받지 않는 유일한 이름
       * 즉 디렉토리가 변경되더라도, 유지되는 리소스명을 의미
       * 예컨대, `urn:isbn:0451450523` 1926년에 출간된 the Last Unicorn의 도서식별번호