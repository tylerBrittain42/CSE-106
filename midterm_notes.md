# Lecture 5
## Modules
### **import**
- *import <module\>* use *module.function()* (uses namespace)
- *from <module\> import <function/class\>* does not require namespace
- *from <module\> import* \* allows us to reference without namespace
- use *as* to refer to custom namespace
## NumPy
Used for working with arrays. 

Various math purposes such as linear algebra and matrix manupulation,

- *axis*: dimensions: (think row)
- *length*: think column count
- *arrange*: think range
- *reshape*: reshapes array into specified rows/columns

# Lecture 6: Pandas
Better than numpy when large amounts of data (500k+ rows)

uses 2d table objects called data frames

</br>
 
## DataFrame Example
table2 = pd.DataFrame ({'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}, index=['Prod a','Prod b'])

- Bob is column title
- list is contents of column
- index is name of each row

## iloc and loc
Both use (row,i) notation

Both use rows for first value
- *iloc* -excludes last row value, column value is numeric
- *loc* - does not exclude last row value, column selection is label based
- **Both** are able to filter using the row column
- *example*: print(growth_info.loc[growth_info.height > 48, "age"] - returns all ages where height is over 48

# Slide 7: HTML
## Tables
- *tr* = table row
- *td* = table data (entry)
- *th* = table header

# Slide 10: JS -> jQuery
- everything is based off of *$*

## Key
- *$(p)* = p tag (grabs all)
- *$("#foo")* = foo id
- *$(".foo")* = foo class

# Slide 11
HTTP is:
- connectionless
- media independent
- stateless