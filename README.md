# Python_DevHub

* Documentation: https://apideveloper.vantiv.com/docs/devhub-developer
* Forum: https://apideveloper.vantiv.com/forum
* FAQ: https://apideveloper.vantiv.com/faqs

##Overview

This repository demonstrates sending transactions to Vantiv DevHub.


##Prerequisites

* DevHub Account (https://apideveloper.vantiv.com)
* License from DevHub Account
* AcceptorID (merchantid)


##Step 1: Find Configuration Information and Setup

Login to your DevHub account, create an application, and click on that application to integrate.  You will see a webpage like the following.  You will need the LicenseId, the AcceptorID, and the endpoint URL's. Here are a few key resources to be aware of once you create an account and scope an application. 

![Image of DevHub developer dashboard](http://apideveloper.vantiv.com/sites/default/files/Dev%20dashboard%20Page.png)

Before using the sample application please locate the src\request\Config.py 
You'll need to enter the license Id you obtained in the portal into the "license" field. To learn more about how the code is setting the license, please reference the file src\request\Request.py to see how it's set in the HTTPS header.

```
license = ""
baseEndpoint = "apis.cert.vantiv.com"
version = 1
proxy = null
proxyAuth = ""
```

##Step 2: Build the Request

Resources

* The src\Test.py provides a way to begin trying out the different API transaction types. 
* API documentation for more information: https://apideveloper.vantiv.com/docs/devhub-developer
* Endpoint reference which provides the different endpoint URL's: https://apideveloper.vantiv.com/docs/endpoint-reference-devhub
* Postman examples (You can import the collection using this URL. Once imported you can try out tests once you enter the License in the header) https://www.getpostman.com/collections/332d5043da14439823aa

In the file src\Test.py you can simply uncomment the transactions you'd like to try out. For example, the following will send an example of an Authorization transactions.

```python
#^^^^^^^^^^^^^^^^^^^^^^^^CONFIGURE THE API^^^^^^^^^^^^^^^^^^^^^^^^#

#   Uncomment the sample transaction below that you would like to test

#  CREDIT
sampleCreditAuthorization()
#sampleCreditAuthorizationCompletion()
#sampleCreditCaptureGivenAuth()
```

To provide a more basic understanding of the message the sample code is sending, here's an example. Please note that although string building is an option, we generally recommend a more structured approach when sending transactions. Below in the header you'll see [Your License Id]. You'll need to replace [Your License Id] with the actual license Id you obtain in the DevHub portal. 

```Java
POST /payment/sp2/credit/v1/authorization
Content-Type: application/json
Authorization: VANTIV license="[Your License Id]"
Host: apis.cert.vantiv.com
Content-Length: 764

{
   "Credentials":
   {
      "AcceptorID":"1147003"
   },
   "Reports":
   {
      "ReportGroup":"1243"
   },
   "Transaction":
   {
      "ReferenceNumber":"1",
      "TransactionAmount":"10.00",
      "OrderSource":"ecommerce",
      "CustomerID":null,
      "PartialApprovedFlag":null
   },
   "Card":
   {
      "Type":"VI",
      "CardNumber":"4457010000000009",
      "ExpirationMonth":"01",
      "ExpirationYear":"16",
      "CVV":"349"
   },
   "Application":
   {
      "ApplicationID":"4306abfcc9a56e42df996a965"
   },
   "Address":
   {
      "BillingName":"John and Mary Smith",
      "BillingAddress1":"1 Main St.",
      "BillingCity":"Burlington",
      "BillingState":"MA",
      "BillingZipcode":"01803-3747",
      "BillingCountry":"US"
   }
}
```

##Step 3: Send the Request

Although the src\Test.python will handle setting everything for you, we wanted to call out how it works. Please reference the src\request\Request.py The "send()" function handles converting the object to a Json string, setting the header information for the request, and returns the string response.

```Python
    def send(self):
        if (Config.doNotSend):
            body = jsonpickle.encode(self, unpicklable = False)
            if (Config.printRequest):
                print(body)
            return body
        else:
            queryParamString = ''
            if (self.queryParams):
                queryParamString = "?"
                for key, value in self.queryParams.iteritems():
                    queryParamString += key + "=" + value + "&"
                queryParamString = queryParamString[:-1]
            url = self.url +queryParamString 
            body = jsonpickle.encode(self, unpicklable = False)
            if (Config.printRequest):
                print (body)
            if(Config.proxy):
                proxy = urllib2.ProxyHandler(Config.proxy)
                auth = urllib2.HTTPBasicAuthHandler()
                opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                urllib2.install_opener(opener)
            req = urllib2.Request(url)
            req.add_header('Authorization', 'VANTIV license=' + "\"" + Config.license + "\"" )
            req.add_header('Content-Type', 'application/json')
            try:
                resp = urllib2.urlopen(req, body)
                code = resp.getcode()
                if(Config.printStatus):
                    print(code)
                contents = resp.read() 
            except urllib2.HTTPError, error:
                contents = error.read() 
            if (Config.printResponse):
                print(contents)
            return contents
            
```


An example of locating specific meta data in the response can be found by referencing the src\request\Utilities.py The "getValueFromKey()" function. 

```Python
"""
* Extracts the value from a response and a key (Where the value, response, and key are String objects)
* @param response must be the response of a transaction
* @key must be the key of a Json key value pair
* @return the value as a String or None if not found
"""
def getValueFromKey(response, key):
    key = key + '\":\"'
    location = response.find(key)
    if location == -1:
        return None
    response = response[location + len(key):]
    location = response.find('\"')
    if location == -1:
        return None
    value = response[:location]
    return value

```

In this case we are extracting the TransactionID. 


```Python
transactionID = Utilities.getValue(response, 'TransactionID')
```


##Step 4: Validate a test

One of the key features of DevHub is the ability to provide automated scenario based validations of pre-defined tests in the portal. Here's an example of validating a test against the portal. Using the example JSON provided above, let's validate test "L_AC_1" in the "Authorization and Capture" set of tests. Please note that for certification, all of your tests must be run through the interface you write for your application. This example is only intended to show you how you can validate your solution.

First, follow the steps above to send an Authorization transaction.

In the response you'll see a "RequestID". The "RequestID" is used to uniquely identify the transaction sent through DevHub. We use this value to retrieve the message you just sent and validate it against a test defined in your application. In this case "L_AC_1". 

Here's an example of the JSON response.

```
{
  "litleOnlineResponse": {
    "@version": "9.3",
    "@response": "0",
    "@message": "Valid Format",
    "authorizationResponse": {
      "@id": "4306abfcc9a56e42df996a965",
      "@reportGroup": "1243",
      "@customerId": "345",
      "orderId": "1",
      "response": "000",
      "responseTime": "2016-02-16T23:18:09",
      "postDate": "2016-02-16",
      "message": "Approved",
      "authCode": "11111 ",
      "fraudResult": {
        "avsResult": "01",
        "cardValidationResult": "M"
      },
      "tokenResponse": {
        "tokenResponseCode": "802",
        "tokenMessage": "Account number was previously registered",
        "bin": "445701",
        "PaymentAccountID": "1111000194360009",
        "Type": "VI"
      },
      "enhancedAuthResponse": {
        "virtualAccountNumber": "false"
      },
      "TransactionID": "82917370336788986"
    }
  },
  "RequestID": "8f4e3838-576f-49e7-9e82-3d2e5b8f2906"
}
```

Now click into the feature you wish to validate. In this case the "Authorization and Capture"

![Dashboard Feature](http://apideveloper.vantiv.com/sites/default/files/Dashboard%20Feature.png)

Enter the TestId followed by the RequestID returned in the response. Now click on the yellow validate button. The system will provide a summary of all items that passed along with those that need to be fixed. 

![Validate a test](http://apideveloper.vantiv.com/sites/default/files/ValidateTest.png)


##Folder Contents
```
> src
        > Test.py : Used as a starting point to try out the API using the Sample Code.
        > request (folder)
               > Config.py: Used to set the base endpoint URL, license, and optional proxy settings should your company have a proxy.
               > Request.py: Contains examples of sending a tranaction, serializing an object to JSON, and getting the Json String response.
               > SampleRequests.py: The following data generator examples provide test values that can be set per each transaction type. 
               > Utilities.py: Useful example of code like extracting values from a string response. 
               > Boarding (folder): Transaction types definitions commonly used by payment facilitator partners.
               > Check (folder): Transaction type definitions
               > Credit (folder): Transaction type definitions
               > Model (folder): Data definition of the API.
               > Services (folder): Transaction type definitions for items used across Check and Credit.
```
        
        
####Copyright (c) 2016 Vantiv, Inc. - All Rights Reserved.

Sample Code is for reference only and is solely intended to be used for educational purposes and is provided ?AS IS? and ?AS AVAILABLE? and without warranty. It is the responsibility of the developer to  develop and write its own code before successfully certifying their solution.  

This sample may not, in whole or in part, be copied, photocopied, reproduced, translated, or reduced to any electronic medium or machine-readable form without prior consent, in writing, from Vantiv, Inc.

Use, duplication or disclosure by the U.S. Government is subject to restrictions set forth in an executed license agreement and in subparagraph (c)(1) of the Commercial Computer Software-Restricted Rights Clause at FAR 52.227-19; subparagraph (c)(1)(ii) of the Rights in Technical Data and Computer Software clause at DFARS 252.227-7013, subparagraph (d) of the Commercial Computer Software--Licensing clause at NASA FAR supplement 16-52.227-86; or their equivalent.

Information in this sample code is subject to change without notice and does not represent a commitment on the part of Vantiv, Inc.  In addition to the foregoing, the Sample Code is subject to the terms and conditions set forth in the Vantiv Terms and Conditions of Use (http://www.apideveloper.vantiv.com) and the Vantiv Privacy Notice (http://www.vantiv.com/Privacy-Notice).  
