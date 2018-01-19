*mark header using* `===` *or* `---`

first level header
=====

second level header
---

*or mark header using hash tags* `#`*, Github requires a space after the hash to be effective*

# first level header
## second level header
### third level header
#### fourth level header
##### fifth level header
###### sixth level header

*horizontal lines using* `-`*,* `*` *or* `_`

---
***
___


*insert a line break with two spaces and return:*

This is a break  
before the next line.

*start block with* `>` *or nested block with* `>>`

> This is a block.
>> This is a nested block.

*italic with single asteroids* `*italic*` *, bold in two astroids* `**bold**` *and both in three astroids* `***both***`

*italic*, **bold** and ***bold italic***

*unordered list starts with `-`, `*` or `+`*

- list item1 (with -)
* list item2 (with *)
+ list item3 (with +)

*ordered list `N.` (number+period) to escape (number+\\+period)*

1. item1
2. item2
3. item3

*inline hyperlinks:* `[attribute text](url "url title")`

Please search [Google](http://www.google.com "The google link")

*inline image:* `![attribute text](image url "image title")`

![Staff](https://www.harmony-church.org/wp-content/uploads/2016/09/praise-clipart-300x300.jpg "Music Staff")

*referenced links/image:* `[link attrib][link mark]` *then at the end of document, add* `[link mark]: link url "link title"`

[Sina News][Sina marker]

*directly show inline URL with brackets `<>`, e.g. `<url>`*

This is a link: <http://www.news.sina.com>

*wrap inline code with two back tips \`\`, e.g.* `python3 script.py`


*indent block of codes with a tab or 4 spaces (line breaks are explicitly given, empty indented lines in between are assumed in the same block*

	$scope.model = {
		hasMoreInfo: True,
		
		label: 'My Label'
	}

*wrap block of codes with triple \`\`\` and optionally followed by the language name (coding highlighting will be rendered on the server side*


```html
<input type="text" name="location" geo-location />
```

```python
import sys
for i in range(3):
	print("hello world")
```

*add relative links to docs on the server* `[attribute text](path relative to this md file)`

The link to [example.md](./example.md)

*add in-page nevigation*  `[Section Name](#section-name)`

- [Section 1](#section-1)
- [Section 2](#section-2)
- [Section 3](#section-3)


Section 1
----

Section 2
----

Section 3
----





[Sina marker]: http://www.news.sina.com/ "sina news page"







