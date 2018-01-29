[chrome extension home page](https://developer.chrome.com/extensions)
[chrome Javascript APIs](https://developer.chrome.com/extensions/api_index)

A Chrome extension is a collection of HTML/CSS/Javascripts packaged with a manifest file and tells Chrome how to integrate their functionality into the browser. It can use Chrome API to control and utilize the browser. 


### 3 parts of a Chrome extension

* **background page**: an HTML page running in the background (can be monitored from Chrome Task Manager). A background page can be a persistent page or an event page. It can modify the DOM of the HTML pages of extension. 

* **UI page**: an HTML page displaying the UI for an extension (e.g. the extension option page), can invoke functions in the background page. It can modify the DOM of the HTML pages of extension. 

* **content scripts**: scripts that are injected and executed when pages are loaded in the browser. It can not modify the DOM of HTML pages of extension. It can communicate with background page or UI page to perform actions on the web page. 


### 2 types extension action

* *browser actions* are related to the browser components like toolbar buttons. 

* *page actions* are functions or UI specific to a page. 


### difference between extension and plug-in

* **plug-ins** run outside of the sandbox of browser and interact with the browser. They can be found at `chrome://plugins` (e.g. Adobe Flash Player, Windows Media Player)

* **extensions** run within the browser and conform to a specific APIs and capabilities exposed by Chrome. They are safer to run, and they extend the capabilities of the browser. They can be found at `chrome://extensions`



