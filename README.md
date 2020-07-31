# AmazonApp
Simple script which uses BeautifulSoup &amp; smtplib to send an email notification when a chosen item on Amazon moves below a given price point.

Be sure to `pip install bs4` if you haven't already. All other imports should already be included with Python3.

If you don't know your user agent information, just google "my user agent" and copy and paste that into `headers` (line 10)

This code only works if an item is in stock, change the id in `soup2.find(id="")` (line 22) to fit your needs.
