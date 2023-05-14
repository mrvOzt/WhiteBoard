# WhiteBoard

An white board simulation project

The project simulates a whiteboard with the ability to draw in 9 different colors and an eraser function provided by a button. It offers a canvas for the user to freely draw on.

If the user wants to change the thickness of the drawing, they can easily do so using the slider below the color palette.

The project uses features such as canvas, color, and button using the Tkinter library.


## Features

- 9 different color options
- Ability to adjust the drawing size
- Eraser function
- Ability to adjust the size of the pen

## Usage/Examples

The project was developed using the tkinter library, as indicated in the documentation. As the tkinter library is useful enough for GUI design, no problem was encountered during the development phase that could not be solved. Below are some example code usages.


```python (sample code for the color palette)
id = colors.create_rectangle((10,10,30,30),fill = "black")
colors.tag_bind(id,'<Button-1>',lambda x: show_color('black'))

```

```python (code for the slider used to adjust the size of the pen)
slider = ttk.Scale(root,from_ = 0,to = 100,orient = "horizontal",command = slider_changed,variable = current_value)

```
  
```python (function created for the eraser function)
def new_canvas():
    canvas.delete('all')
    display_palette()

```
  
```python (function created for the drawing process)
def addLine(work):
    global current_x,current_y
    canvas.create_line((current_x,current_y,work.x,work.y),width=get_current_value(),fill=color,capstyle=ROUND,smooth = TRUE)
    current_x,current_y = work.x,work.y


```
## Sources

- https://docs.python.org/3/library/tkinter.html
- https://stackoverflow.com/questions/10533929/colors-of-rectangles-in-python
- https://docs.python.org/3/library/tkinter.ttk.html


## Prepared by

Merve Öztürk
