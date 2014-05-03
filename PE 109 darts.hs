import Data.Array
wedges = [1..20]
zones = listArray (0,62) $ 0:25:50:wedges++map (2*) wedges++map (3*) wedges
checkouts = 
    [[a,b,c] |
    a <- 2:[23..42],
    b <- [0..62],
    c <- [b..62]
    ]
score = sum.map (zones!)    
problem_109 = length $ filter ((<100).score) checkouts

main = print $ problem_109