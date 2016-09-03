<h2>CsrfFinder - Cross-Site Request <h2>Forgery Finder</h2>
<h2>Author: Alec Blance</h2>

<h2>Compatibility:</h2>

    Any system running Python 2.7


<h2>Requirements:</h2>

    Python 2.7


<h2>Description:</h2>
CsrfFinder is a tool designed for pentesters and hackers , who wants to check for CSRF vulnerability in website's forms. This tool checks how many forms present in the webpage and checks the form if it has the csrf protection activated.

<h2>Features:</h2>

    Csrf Scanning
    Detecting how many forms present
    showing forms that is vulnerable
    User-friendly UI

 
<h2>Usage:</h2>

Enter the target url : google.com
What number of form do you want to scan?: 1 


<h2>Output</h2>

Enter the target url : google.com

======================================================

The number of forms present in the http://google.com is 1

1. form action=/search onsubmit=/

======================================================

What number of form do you want to scan? 1

form action=/search is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)


<h2>Bugs? Errors?</h2>
http://facebook.com/alec.blance
blancealec1@gmail.com
