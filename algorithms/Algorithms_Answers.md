Add your answers to the Algorithms exercises here.

A.) O(n) // single while loop

B.) O(n+10) // not entirely sure here... Lot's of things going on but it seems like the initial loop is O(n) 
    and the others are less than that, so the O(n) should override it, but again, not sure...

C.) O(n) // recursion

Exercise II

A.) I think the best scenario is to start on the middle floor and try to create a worse case O(log n) on average and best 
    case O(1) algorithm scenario. If you can keep cutting the floors in halves then you will quickly get your result, and
    potentially get it right the first time. Let's say there are 100 floors. If you drop the egg at 50 and it breaks, then
    you can disregard floors 50 to 100, so then go to floor 25 and if it still breaks then go to floor 12 and disregard 
    floors 25 to 49. If it does not break at 12 then you can disregard floors 1 - 11  but keep them in memory as they are safe
    places to drop from, and now you must explore the floors 12 to 24 by halving floors based on drop results. You want to
    get the maximum floor you can drop from. This same logic applies to guessing any number.