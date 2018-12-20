# import libraries
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen

from bs4 import BeautifulSoup

#open file to write to (courses.txt)
f= open("courses.txt","w+")
departments = []

# specify the intial url (for page of all departments)
quote_page = 'https://courses.students.ubc.ca/cs/main?pname=subjarea'

# query the website and return the html to the variable 'page'
from urllib.request import urlopen
page = urlopen(quote_page)

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

#find all course abbreviation parts, which are used to query for dept pages
dept_html = soup.tbody.find_all("a")

#for each, add course abbreviations to list of departments
for dept_name_html in dept_html:
    #remove starting and trailing tags
     dept_name = dept_name_html.text.strip()
     departments.append(dept_name)

#loop through all departments to get specific course number info
for dept in departments:
    #department pages can just be found by substituting the department abbreviation at the end of the url
     department_page = 'https://courses.students.ubc.ca/cs/main;jsessionid=5thttU6EsuCe4w8Z6mUwB5JH?pname=subjarea&tname=subjareas&req=1&dept=' + dept
     page_f = urlopen(department_page)
     soup_inner = BeautifulSoup(page_f, 'html.parser')
     #find all courses and print them into courses.txt
     course_html = soup_inner.tbody.find_all("a")
     for c in course_html:
        course = c.text.strip()
        f.write(course + '\n');

f.close()
