
Uses CP-SAT solver -> Constraint Programming


## Description
Given a set of employees per department, allocate them per shift for 7 days a week.
Try make it equal.
Using predicted demand data


Shop opening hours = 10am - 7pm
Someone has to be an hour in before to open up

### Shift setups
9am - 7pm (10hrs)    

----
Could try both of these approaches:

9am - 5pm (8hrs)    
11am - 7pm (8hrs)    

-----
9am - 2pm (5hrs)    
2pm - 7pm (5hrs)    

---> Doesn't matter as long as we have shifts per day


### Hard constraints
- EEs can't work more than 8 hours per day, 40 hrs per week
- No 2 EEs on the same shift at the same time
- No 2 shifts in a row for an EE


### Soft constraints
- If days off requested
- Scheduling too parsley
- Preferred days / shifts



#### Example


#### Notes
Objective function -> Function that is desired to be maximized


V1 = Simple scheduler by shifts needed per department per day