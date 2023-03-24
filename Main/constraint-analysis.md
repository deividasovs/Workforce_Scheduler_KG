# Constraint analysis

### Hard constraints (penalty = 0)
- Minimum 2 rest days during the week
- Fixed staff assignments

### Soft constraints 
| Constraint   |  Penalty(s) |  
|---|---|
|  excess cover |  1 |   
|  penalized transitions |  2 |   
| request want | -1 |
| request don't want | 4 |
| 2 consecutive rest days | 0 |
| 3 consecutive rest days | 3 | 
| 3 total rest days | 3 | 