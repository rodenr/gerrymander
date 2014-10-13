In the small neighborhood it checks every valid move (extra credit) and goes
to the terminal node

In the large neighborhood it checks every valid move given the parameters of a
move by Professor Hoenigman.  Large Neighborhood stops after 4 moves, however
this can be changed at the top of the minimax function to make it whatever
depth desired.

The Heuristic for large neighborhood returns either 2,1,0,-1, or -2.  Which of
these is selected depends on a comparison between districts already selected
and the remaining blocks.
