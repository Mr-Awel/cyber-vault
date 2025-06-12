

## 1. HTTP vs HTTPS
- **HTTP (HyperText Transfer Protocol)**  
  - Application-layer protocol for fetching resources (HTML, images, videos, etc.)  
  - Default port: 80  

- **HTTPS (HTTP Secure)**  
  - HTTP over TLS/SSL (encryption + server authentication)  
  - Default port: 443  

## 2. URL (Uniform Resource Locator)

`scheme://[user[:password]@]host[:port]/path[?query][#fragment]`

- **scheme**: Protocol to use (e.g. `http`, `https`, `ftp`)  
- **user:password**: Optional credentials for authentication (e.g. `user:pass@`)  
- **host**: Domain name or IP address of the server  
- **port**: TCP port (1–65535; defaults: 80 for HTTP, 443 for HTTPS)  
- **path**: Resource’s location on the server (e.g. `/index.html`)  
- **query**: Key/value pairs passed to the server (e.g. `?id=1&sort=asc`)  
- **fragment**: In-page reference or anchor (e.g. `#section2`; not sent to the server)  

## 3. HTTP Message Structure

### Request
    GET /path/resource HTTP/1.1
    Host: example.com
    User-Agent: MyBrowser/1.0
    [Other headers…]

    [Optional body]

### Response
    HTTP/1.1 200 OK
    Server: nginx/1.19.0
    Date: Tue, 01 Jan 2021 12:00:00 GMT
    Content-Type: text/html
    Content-Length: 1234
    [Other headers…]

    <html>…</html>

## 4. Common HTTP Methods

- **GET**  
  - Retrieves data from the server  
  - Safe (doesn’t change state) and idempotent  

- **POST**  
  - Submits data to create a new resource  
  - Non-idempotent (multiple calls can create multiple resources)  

- **PUT**  
  - Replaces or creates a resource at the given URL  
  - Idempotent (repeating has same effect as once)  

- **DELETE**  
  - Deletes the specified resource  
  - Idempotent (once deleted, further deletes do nothing)  

**Idempotence**:  
- Idempotent methods (safe to repeat): `GET`, `PUT`, `DELETE`  
- Non-idempotent: `POST`

## 5. Status Code Categories

| Range   | Meaning           |
|---------|-------------------|
| 1xx     | Informational     |
| 2xx     | Success           |
| 3xx     | Redirection       |
| 4xx     | Client errors     |
| 5xx     | Server errors     |

### Common Status Codes

- **200 OK**: Request succeeded.  
- **201 Created**: Resource created.  
- **301 Moved Permanently**: URL has changed permanently.  
- **302 Found**: Temporary redirect.  
- **400 Bad Request**: Malformed request or missing data.  
- **401 Unauthorized**: Authentication required.  
- **403 Forbidden**: Access denied.  
- **404 Not Found**: Resource doesn’t exist.  
- **405 Method Not Allowed**: HTTP method not supported on this resource.  
- **500 Internal Server Error**: Server encountered an unexpected condition.  
- **503 Service Unavailable**: Server overloaded or down for maintenance.  

## 6. HTTP Headers

### Request Headers
- **Host**: Specifies the domain name of the server (e.g. `Host: example.com`)  
- **User-Agent**: Identifies the client software and version (e.g. `User-Agent: MyBrowser/1.0`)  
- **Content-Length**: Byte length of the request body (e.g. `Content-Length: 512`)  
- **Accept-Encoding**: Compression schemes the client supports (e.g. `Accept-Encoding: gzip, deflate`)  
- **Cookie**: Key/value pairs stored by the browser (e.g. `Cookie: sessionId=abc123`)

### Response Headers
- **Set-Cookie**: Instructs the browser to store a cookie (e.g. `Set-Cookie: sessionId=abc123; Path=/; HttpOnly`)  
- **Cache-Control**: Caching directives (e.g. `Cache-Control: max-age=3600`)  
- **Content-Type**: Media type of the response body (e.g. `Content-Type: text/html; charset=utf-8`)  
- **Content-Encoding**: Compression applied to the response (e.g. `Content-Encoding: gzip`)  

## 7. Cookies

- **What are cookies?**  
  - Small `key=value` pairs stored by the browser  
  - Enable stateful behavior on HTTP’s stateless requests

- **Set-Cookie (response header)**  
  - Server instructs browser to store a cookie  
  - Example:  
    ```
    Set-Cookie: sessionId=abc123; Path=/; HttpOnly; Secure; Max-Age=3600
    ```

- **Cookie (request header)**  
  - Browser automatically sends stored cookies  
  - Example:  
    ```
    Cookie: sessionId=abc123; theme=dark
    ```

- **Common uses**  
  - **Session management** (authentication tokens)  
  - **User preferences** (theme, language)  
  - **Tracking** (visit counts, analytics)

- **Security flags**  
  - `HttpOnly`: Not accessible via JavaScript  
  - `Secure`: Sent only over HTTPS  
  - `SameSite`: Controls cross-site sending (`Lax`, `Strict`, or `None`)

---
## **Questions**

What does HTTP stand for?
**=HyperText Transfer Protocol**

What does the S in HTTPS stand for?
**=Secure**

What HTTP protocol is being used in the above example?
**=HTTP/1.1**

What HTTP protocol is being used in the above example?
**=Content-Length**

What method would be used to create a new user account?
**=POST**

What method would be used to create a new user account?
**=PUT**

What method would be used to remove a picture you've uploaded to your account?
**=DELETE**

What method would be used to view a news article?
**=GET**

What response code might you receive if you've created a new user or blog post article?
**=201**

What response code might you receive if you've tried to access a page that doesn't exist?
**=404**

What response code might you receive if the web server cannot access its database and the application crashes?
**=503**

What response code might you receive if you try to edit your profile without logging in first?
**=401**

What header tells the web server what browser is being used?
**=User-Agent**

What header tells the browser what type of data is being returned?
**=Content-Type**

What header tells the web server which website is being requested?
**=Host**

Which header is used to save cookies to your computer?
**=Set-Cookie**