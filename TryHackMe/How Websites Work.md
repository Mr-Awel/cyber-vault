
## HTML Injection

**Analogy: Café Bulletin Board**  
Think of your page like a public bulletin board in a café. Every form submission is a “note” someone pins up. If you don’t inspect it first, they can sneak in hidden messages (HTML/JS) that rearrange or break your board.

---
### What It Is  
- A client-side vulnerability when **unfiltered user input** is rendered as HTML/JS.  
- Occurs if you use `innerHTML` (or similar) without sanitizing.

---
### Attack Flow  
1. Someone pins a note (user submits input).  
2. Your script sticks it on the board unchecked:

    document.getElementById("greeting").innerHTML = "Hello, " + userInput;

3. If the note is `<h1>Hacked!</h1>`, your page suddenly shows a giant “Hacked!” headline.

---
### Why It’s Dangerous  
- **Defacement:** Attacker can change your page’s look (fake alerts, banners).  
- **Malicious scripts:** They can inject `<script>` tags to steal cookies, redirect users, or load malware.  
- **Trust break:** Visitors lose confidence when your site suddenly misbehaves.

---

### How to Lock It Down
- Escape all user input before rendering:
  - Convert `<` to `&lt;` and `>` to `&gt;` so tags stay as text.
- Prefer safe APIs: use `element.textContent = userInput;` instead of `innerHTML`.
- Whitelist tags only if needed:
  - If you must allow some HTML (e.g. `<b>`, `<i>`), strip everything else.

Keep picturing that bulletin board: every note gets inspected before it goes up. Once you enforce that check, HTML injection is just harmless doodling.


---
## **Questions**

What term best describes the component of a web application rendered by your browser?
**=Front End**

What does the S in HTTPS stand for?
**=Secure**

What HTTP protocol is being used in the above example?
**=HTTP/1.1**

What HTTP protocol is being used in the above example?
**=Content-Length**