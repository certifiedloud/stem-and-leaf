

```python
from StemAndLeaf import StemAndLeafPlot as st
```


```python
import random
```


```python
nums = random.sample(range(150), 50)
```


```python
plot = st(nums)
```


```python
plot.plot()
```

    0   | 2 4 5 6 8 
    1   | 7 9 
    2   | 1 4 5 
    3   | 1 2 3 4 5 9 
    4   | 0 2 3 4 7 
    5   | 1 3 4 
    6   | 4 7 
    7   | 2 
    8   | 4 5 6 7 
    9   | 2 3 7 
    10  | 1 3 4 7 8 9 
    11  | 0 4 9 
    12  | 0 1 2 6 
    13  | 0 3 
    14  | 8 
    
    Key: 1 | 2 = 12



```python
print(sorted(nums)) # For reference
```

    [2, 4, 5, 6, 8, 17, 19, 21, 24, 25, 31, 32, 33, 34, 35, 39, 40, 42, 43, 44, 47, 51, 53, 54, 64, 67, 72, 84, 85, 86, 87, 92, 93, 97, 101, 103, 104, 107, 108, 109, 110, 114, 119, 120, 121, 122, 126, 130, 133, 148]

