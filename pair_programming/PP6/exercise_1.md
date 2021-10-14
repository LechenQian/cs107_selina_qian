Sharer and Coder: Han Truong, Listener: Selina Qian and Haochen Yang

| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v0 = x      | pi/2        | pi/2        |  1          |     1       |     0       |
| v1          | sin(v0)    |  1          |  cos(v0) * v0_dot|     0     |      0      |

| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v2 = y      | pi/3        | pi/3        |  1          |     0       |     1      |
| v3          | cos(v2)    |   1/2        | -sin(v2) * v2_dot|     0    |      - sqrt(3)/2   |


| trace       | elem op.    | value       | elem der.   | delta x     | delta y |
| ----------- | ----------- | ----------- | ----------- | ----------- | ----------- |
| v4      | v1-v3        | 1/2         |  v1_dot - v3_dot |    0        |     sqrt(3)/2       |
| v5      | v4^2      | 1/4         | 2 * v4 * v4_dot |     0       |     sqrt(3)/2       |
| v6      | -v5   | -1/4         | - v5_dot |     0       |     -sqrt(3)/2       |
| v7      | exp(v6)   | exp(-1/4)       | exp(v6) * v6_dot |     0       |      exp(-1/4)  *  -sqrt(3)/2      |



delta_f / delta_x = 0

delta_f / delta_y = 0.7788 *  -sqrt(3)/2
