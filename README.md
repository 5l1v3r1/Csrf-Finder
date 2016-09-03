CsrfFinder - Cross-Site Request Forgery Finder
Author: Alec Blance

Compatibility:

    Any system running Python 2.7


Requirements:

    Python 2.7


Description:
CsrfFinder is a tool designed for pentesters and hackers , who wants to check for CSRF vulnerability in website's forms. This tool checks how many forms present in the webpage and checks the form if it has the csrf protection activated.

Features:

    Csrf Scanning
    Detecting how many forms present
    showing forms that is vulnerable
    User-friendly UI

 
Usage:

Enter the target url : google.com
What number of form do you want to scan?: 1 


Output

Enter the target url

[+]: google.com

======================================================

The number of forms present in the http://google.com is 1

1. <form action=/search onsubmit=/>

======================================================

What number of form do you want to scan?

[+]: 1

<form action=/search> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)


<h2>Bugs? Errors?</h2>
http://facebook.com/alec.blance
blancealec1@gmail.com
