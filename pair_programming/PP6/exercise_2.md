Sharer and Coder: Han Truong, Listener: Selina Qian and Haochen Yang

Top row:

| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v0 = x      | x     | 1       |  1          |     1       |     0       |
| v1          | v0^2   |  1          | 2 * v0 * v0_dot |     2     |      0      |

| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v2 = y      | y     | 1       |  1          |     0       |     1       |
| v3          | v2^2   |  1          | 2 * v2 * v2_dot |     0     |      2      |

| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v4       | v1 + v3    | 2       |  v1_dot + v3_dot          |     2       |     2       |



Bottom row:

| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v5 = x      | x     | 1       |  1          |     1       |     0       |


| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v6 = y      | y     | 1       |  1          |     0       |     1       |


| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v7       | v5 + v6    | 2       |  v5_dot + v6_dot          |     1       |     1       |
| v8       | exp(v7)    | exp(2)       |  exp(v7) * v7_dot          |     exp(2)       |     exp(2)         |


derivative        = [top_row, bottom_row]:


delta_f / delta_x = [2, exp(2)]

delta_f / delta_y = [2, exp(2)]
