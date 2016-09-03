#Tool : Csrf Finder 1.1
#Author : Alec Blance
#Desc : This tool scans for csrf vulnerability in websites

import urllib #URL library
import re #Regular Expression Library 
from bs4 import BeautifulSoup #Beautiful Soup Library
import httplib
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("+    ____________  ____    _______  _____ ________    +")
print ("+   / __/  __| _ \|  _|   |  _| | \ | |  \|  _| _ \   +")
print ("+  | (__\__  \ __/| _|    | _|| | |\| | - |__|_ __/   +")
print ("+   \___|____/_|_\|_|     |_| |_|_| \_|__/|___|_|_\   +")
print ("+                                                     +")
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("+                                                     +")
print ("+ Info : Cross-Site Request Forgery Finder is an      +")
print ("+ aplication used for finding CSRF Vulnerabilities in +")
print ("+ a website.                                          +")
print ("+                                                     +")
print ("+ Developer:      Alec B. Blance                      +")
print ("+ Researcher:     Alexis B. Ligahon                   +")
print ("+                                                     +")
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print ("                                                       ")
print ("Choose what is your target. [L]ocal source file or [U]rl")
choose = raw_input ("[+] ")
if choose == "L":
    print ("Enter the name of the file (it should have .html)")
    file = raw_input ("[+] ")
    fileurl = urllib.urlopen (file).read()
    soupmainer = BeautifulSoup(fileurl,"html.parser")
    count = fileurl.count ("<form")
    if count == 0:
        print ("There are no forms found")
    exit()
    if count == 1:
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
    if count == 2:
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
        inputer2 = soupmainer.findAll ("form")[1]
        count2 = inputer2 ['action']
        counter2 = "/"
        for code in inputer1:
	        try:
		        counter2 = inputer2 ['onsubmit']
	        except KeyError:
		        continue
    if count == 3 :
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
        inputer2 = soupmainer.findAll ("form")[1]
        count2 = inputer2 ['action']
        counter2 = "/"
        for code in inputer1:
	        try:
		        counter2 = inputer2 ['onsubmit']
	        except KeyError:
		        continue
        inputer3 = soupmainer.findAll ("form")[2]
        count3 = inputer3 ['action']
        counter3 = "/"
        for code in inputer3:
	        try:
		        counter3 = inputer3 ['onsubmit']
	        except KeyError:
		        continue
    if count == 4:
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
        inputer2 = soupmainer.findAll ("form")[1]
        count2 = inputer2 ['action']
        counter2 = "/"
        for code in inputer1:
	        try:
		        counter2 = inputer2 ['onsubmit']
	        except KeyError:
		        continue
        inputer3 = soupmainer.findAll ("form")[2]
        count3 = inputer3 ['action']
        counter3 = "/"
        for code in inputer3:
	        try:
		        counter3 = inputer3 ['onsubmit']
	        except KeyError:
		        continue
        inputer4 = soupmainer.findAll ("form")[3]
        count4 = inputer4 ['action']
        counter4 = "/"
        for code in inputer4:
	        try:
		        counter4 = inputer4 ['onsubmit']
	        except KeyError:
		        continue
    if count == 5:
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
        inputer2 = soupmainer.findAll ("form")[1]
        count2 = inputer2 ['action']
        counter2 = "/"
        for code in inputer1:
	        try:
		        counter2 = inputer2 ['onsubmit']
	        except KeyError:
		        continue
        inputer3 = soupmainer.findAll ("form")[2]
        count3 = inputer3 ['action']
        counter3 = "/"
        for code in inputer3:
	        try:
		        counter3 = inputer3 ['onsubmit']
	        except KeyError:
		        continue
        inputer4 = soupmainer.findAll ("form")[3]
        count4 = inputer4 ['action']
        counter4 = "/"
        for code in inputer4:
	        try:
		        counter4 = inputer4 ['onsubmit']
	        except KeyError:
		        continue
        inputer5 = soupmainer.findAll ("form")[4]
        count5 = inputer5 ['action']
        counter5 = "/"
        for code in inputer5:
	        try:
		        counter5 = inputer5 ['onsubmit']
	        except KeyError:
		        continue
    print ("======================================================")
    print ("The number of forms present in the {} is {}".format(url , count))
    if count == 1:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
    if count == 2:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
        print ("2. <form action={} onsubmit={}>".format (count2,counter2))
    if count == 3:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
        print ("2. <form action={} onsubmit={}>".format (count2,counter2))
        print ("3. <form action={} onsubmit={}>".format (count3,counter3))
    if count == 4:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
        print ("2. <form action={} onsubmit={}>".format (count2,counter2))
        print ("3. <form action={} onsubmit={}>".format (count3,counter3))
        print ("4. <form action={} onsubmit={}>".format (count4,counter4))
    if count == 5:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
        print ("2. <form action={} onsubmit={}>".format (count2,counter2))
        print ("3. <form action={} onsubmit={}>".format (count3,counter3))
        print ("4. <form action={} onsubmit={}>".format (count4,counter4))
        print ("5. <form action={} onsubmit={}>".format (count5,counter5))
    print ("======================================================")
    print ("What number of form do you want to scan?")
    form = raw_input ("[+]: ")
    if form == "1" :
        page1 = urllib.urlopen (url)
        soup1 = BeautifulSoup (page1 , "html.parser")
        input1 = soup1.findAll ('form')[0]
        action1 = input1 ['action']
        token = input1.find ("input",{"name":"token"})
        if token == None:
	        token1 = input1.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input1.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action1))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action1))
	        else:
		        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action1))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action1))
    if form == "2" :
        page2 = urllib.urlopen (url)
        soup2 = BeautifulSoup (page2 , "html.parser")
        input2 = soup2.findAll ('form')[1]
        action2 = input2 ['action']
        textt2 = input2.input
        token = input2.find ("input",{"name":"token"})
        if token == None:
	        token1 = input2.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input2.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action2))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action2))
	        else:
		        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action2))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action2))
    if form == "3" :
        page3 = urllib.urlopen (url)
        soup3 = BeautifulSoup (page3 , "html.parser")
        input3 = soup3.findAll ('form')[2]
        action3 = input3 ['action']
        token = input3.find ("input",{"name":"token"})
        if token == None:
	        token1 = input3.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input3.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action3))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action3))
	        else:
		        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action3))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action3))
    if form == "4" :
        page4 = urllib.urlopen (url)
        soup4 = BeautifulSoup (page4 , "html.parser")
        input4 = soup4.findAll ('form')[3]
        action4 = input4 ['action']
        token = input4.find ("input",{"name":"token"})
        if token == None:
	        token1 = input4.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input4.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action4))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action4))
	        else:
		        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action4))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action4))
    if form == "5" :
        page5 = urllib.urlopen (url)
        soup5 = BeautifulSoup (page5 , "html.parser")
        input5 = soup5.findAll ('form')[4]
        action5 = input5 ['action']
        token = input5.find ("input",{"name":"token"})
        if token == None:
	        token1 = input5.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input5.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action5))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action5))
	        else:
		        print ("<form action={}> is NOT VULNERABLE! (Keep in mind that this may be sometimes falsepositive)".format(action5))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action5))
if choose == "U":
    print ("Enter the target url ")
    url = raw_input ("[+]: ")
    if 'https://' in url:
        pass
    elif 'http://' in url:
        pass
    else:
        url = 'http://' + url 
    mainpage = urllib.urlopen (url) .read()
    soupmainer = BeautifulSoup(mainpage,"html.parser")
    count = mainpage.count ("<form")
    if count == 0:
        print ("There are no forms found")
        exit()
    if count == 1:
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
    if count == 2:
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
        inputer2 = soupmainer.findAll ("form")[1]
        count2 = inputer2 ['action']
        counter2 = "/"
        for code in inputer1:
	        try:
		        counter2 = inputer2 ['onsubmit']
	        except KeyError:
		        continue
    if count == 3 :
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
        inputer2 = soupmainer.findAll ("form")[1]
        count2 = inputer2 ['action']
        counter2 = "/"
        for code in inputer1:
	        try:
		        counter2 = inputer2 ['onsubmit']
	        except KeyError:
		        continue
        inputer3 = soupmainer.findAll ("form")[2]
        count3 = inputer3 ['action']
        counter3 = "/"
        for code in inputer3:
	        try:
		        counter3 = inputer3 ['onsubmit']
	        except KeyError:
		        continue
    if count == 4:
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
        inputer2 = soupmainer.findAll ("form")[1]
        count2 = inputer2 ['action']
        counter2 = "/"
        for code in inputer1:
	        try:
		        counter2 = inputer2 ['onsubmit']
	        except KeyError:
		        continue
        inputer3 = soupmainer.findAll ("form")[2]
        count3 = inputer3 ['action']
        counter3 = "/"
        for code in inputer3:
	        try:
		        counter3 = inputer3 ['onsubmit']
	        except KeyError:
		        continue
        inputer4 = soupmainer.findAll ("form")[3]
        count4 = inputer4 ['action']
        counter4 = "/"
        for code in inputer4:
	        try:
		        counter4 = inputer4 ['onsubmit']
	        except KeyError:
		        continue
    if count == 5:
        inputer1 = soupmainer.findAll ("form")[0]
        count1 = inputer1 ['action']
        counter1 = "/"
        for code in inputer1:
	        try:
		        counter1 = inputer1 ['onsubmit']
	        except KeyError:
		        continue
        inputer2 = soupmainer.findAll ("form")[1]
        count2 = inputer2 ['action']
        counter2 = "/"
        for code in inputer1:
	        try:
		        counter2 = inputer2 ['onsubmit']
	        except KeyError:
		        continue
        inputer3 = soupmainer.findAll ("form")[2]
        count3 = inputer3 ['action']
        counter3 = "/"
        for code in inputer3:
	        try:
		        counter3 = inputer3 ['onsubmit']
	        except KeyError:
		        continue
        inputer4 = soupmainer.findAll ("form")[3]
        count4 = inputer4 ['action']
        counter4 = "/"
        for code in inputer4:
	        try:
		        counter4 = inputer4 ['onsubmit']
	        except KeyError:
		        continue
        inputer5 = soupmainer.findAll ("form")[4]
        count5 = inputer5 ['action']
        counter5 = "/"
        for code in inputer5:
	        try:
		        counter5 = inputer5 ['onsubmit']
	        except KeyError:
		        continue
    print ("======================================================")
    print ("The number of forms present in the {} is {}".format(url , count))
    if count == 1:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
    if count == 2:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
        print ("2. <form action={} onsubmit={}>".format (count2,counter2))
    if count == 3:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
        print ("2. <form action={} onsubmit={}>".format (count2,counter2))
        print ("3. <form action={} onsubmit={}>".format (count3,counter3))
    if count == 4:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
        print ("2. <form action={} onsubmit={}>".format (count2,counter2))
        print ("3. <form action={} onsubmit={}>".format (count3,counter3))
        print ("4. <form action={} onsubmit={}>".format (count4,counter4))
    if count == 5:
        print ("1. <form action={} onsubmit={}>".format (count1,counter1))
        print ("2. <form action={} onsubmit={}>".format (count2,counter2))
        print ("3. <form action={} onsubmit={}>".format (count3,counter3))
        print ("4. <form action={} onsubmit={}>".format (count4,counter4))
        print ("5. <form action={} onsubmit={}>".format (count5,counter5))
    print ("======================================================")
    print ("What number of form do you want to scan?")
    form = raw_input ("[+]: ")
    if form == "1" :
        page1 = urllib.urlopen (url)
        soup1 = BeautifulSoup (page1 , "html.parser")
        input1 = soup1.findAll ('form')[0]
        action1 = input1 ['action']
        token = input1.find ("input",{"name":"token"})
        if token == None:
	        token1 = input1.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input1.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action1))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action1))
	        else:
		        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action1))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action1))
    if form == "2" :
        page2 = urllib.urlopen (url)
        soup2 = BeautifulSoup (page2 , "html.parser")
        input2 = soup2.findAll ('form')[1]
        action2 = input2 ['action']
        textt2 = input2.input
        token = input2.find ("input",{"name":"token"})
        if token == None:
	        token1 = input2.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input2.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action2))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action2))
	        else:
		        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action2))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action2))
    if form == "3" :
        page3 = urllib.urlopen (url)
        soup3 = BeautifulSoup (page3 , "html.parser")
        input3 = soup3.findAll ('form')[2]
        action3 = input3 ['action']
        token = input3.find ("input",{"name":"token"})
        if token == None:
	        token1 = input3.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input3.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action3))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action3))
	        else:
		        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action3))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action3))
    if form == "4" :
        page4 = urllib.urlopen (url)
        soup4 = BeautifulSoup (page4 , "html.parser")
        input4 = soup4.findAll ('form')[3]
        action4 = input4 ['action']
        token = input4.find ("input",{"name":"token"})
        if token == None:
	        token1 = input4.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input4.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action4))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action4))
	        else:
		        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action4))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action4))
    if form == "5" :
        page5 = urllib.urlopen (url)
        soup5 = BeautifulSoup (page5 , "html.parser")
        input5 = soup5.findAll ('form')[4]
        action5 = input5 ['action']
        token = input5.find ("input",{"name":"token"})
        if token == None:
	        token1 = input5.find ("input",{"name":"CSRFTOKEN"})
	        if token1 == None:
		        token2 = input5.find ("input",{"name":"authenticity_token"})
		        if token2 == None:
			        print ("<form action={}> is VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action5))
		        else :
			        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action5))
	        else:
		        print ("<form action={}> is NOT VULNERABLE! (Keep in mind that this may be sometimes falsepositive)".format(action5))
        else :
	        print ("<form action={}> is NOT VULNERABLE!(Keep in mind that this may be sometimes falsepositive)".format(action5))
    exit ()
