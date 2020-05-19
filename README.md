# 2048 Game Simulation in Python

**Description**

This is my 2048 game simulation in Python. Please feel free to let me know your feedback through the comments section. To play the original game, [click here](https://2048game.com). Thanks!

**Compatibility**

This code has been developed and tested well in Windows in the Jupyter Notebook environment (specifically, the Anaconda distribution).

### Instructions

- If you would like to run the code in a Jupyter Notebook, CoLab, or similiar, download the py2048.ipynb version and run it on your environment of choice.
- If you would like to run it directly in your terminal, download the py2048.py version and run it from terminal. Note that this has clear_screen() functionality disabled since it does not work in terminal. 
- If you would like to run it on an android device's mobile browser or without any prior installation of python environments, the code will also work well in [Google's CoLab](https://colab.research.google.com/) environment. [Click here](https://colab.research.google.com/drive/1H18pd6iJFDYlfemcnhjYHYhXtovEwU4B?usp=sharing) to view and run my code in the CoLab environment. You may provide your comments there as well.
 
### Game Navigation

First, enter the size of the board. For example, if you want to play on a 3x3 board, enter 3.

Next, enter the winning value, which is the value at which you would win if you add up to it.

*Note: The default board size is 5 and win value is 2048. This is set incase of an invalid entry of either of the two respectively.*

Now, you may enter your move. To make a move, press either of the WASD keys, or press 'n' to stop the game or 'r' to clear the board and start over with the same board size and win value. You may do the aforementioned in CAPS LOCK as well.

The game will stop by itself if the win value is identified in the board or if further valid moves are not possible.
You will recieve your game stats at the end too !

**Special Notes:**

> 1. The program will randomly spawn a 2 or a 4 after every valid move if the board size is 5 or above. For values, lesser than 5, it would spawn only one 2.
> 2. Hidden developer option ! Press capital 'Z' at any point in the game to fill the empty spots of the board with just one entry. The spots would be filled randomly with a 2 or a 4 in accordance with the previous point. This is to test the game overall, but more specifically, the `move(<parameters>)` function.

**Demonstration**

Here's a simple demonstration of the game in .gif format.

> ![](py2048demo.gif)


```python

```


```python

```
