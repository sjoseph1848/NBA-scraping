from bs4 import BeautifulSoup
html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>First HTML Page</title>
</head>
<body>
  <div id="first">
    <h3 data-example="yes">hi</h3>
    <p>more text.</p>
  </div>
  <ol>
    <li class="special super-special">This list item is special.</li>
    <li class="special">This list item is also special.</li>
    <li>This list item is not special.</li>
  </ol>
  <div data-example="yes">bye</div>
</body>
</html>
"""

soup = BeautifulSoup(html, "html.parser")
# print(soup.body.div)
d = soup.find_all("div")

#select based on id
c = soup.find(id="first")
# print(c)
#select based on class 
g = soup.find_all(class_="special")
# print(g)

#select based off attribute
h = soup.find_all(attrs={"data-example":"yes"})
# print(h)

#css selectors 
n = soup.select('#first')
# print(n)

k = soup.select('div')

l = soup.select('.special')[0]
# print(l)

#select by an attribute
z = soup.select("[data-example]")
# print(z)


#This is how you take data out of html values
# for el in soup.select(".special"):
#   print(el.get_text())


# for el in soup.select(".special"):
  # print(el.name)
  # print(el.attrs['class'])
# d = soup.select("[data-example]")
# print(d)


attr = soup.find("div").attrs["id"]
print(attr)
