

```python
from StemAndLeaf import StemAndLeafPlot as st
```


```python
import random
```


```python

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

    0 | 5 6 7 
    1 | 0 4 8 
    2 | 0 1 4 
    3 | 4 7 
    4 | 0 2 4 
    5 | 0 7 
    6 | 7 8 
    7 | 2 3 
    8 | 0 1 3 5 7 9 
    9 | 1 4 5 
    10 | 6 8 9 
    11 | 1 3 5 6 9 
    12 | 2 3 4 6 9 
    13 | 0 2 3 
    14 | 3 4 5 7 8 
    
    Key: 1 | 2 = 12



```python
print(sorted(nums)) # For reference
```

    [5, 6, 7, 10, 14, 18, 20, 21, 24, 34, 37, 40, 42, 44, 50, 57, 67, 68, 72, 73, 80, 81, 83, 85, 87, 89, 91, 94, 95, 106, 108, 109, 111, 113, 115, 116, 119, 122, 123, 124, 126, 129, 130, 132, 133, 143, 144, 145, 147, 148]

