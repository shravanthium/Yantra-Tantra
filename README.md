# Yantra-Tantra(ಯಂತ್ರ-ತಂತ್ರ )
An attempt to learn, explore and experiment with Machine Learning Algorithms. 

###Problem 1: Warmup Stats
Given an array of N integers separated by spaces, all in one line. 

Display the following: 

1. Mean (m):  

...The average of all the integers.
2. Median: 

...In case, the number of integers is odd, the middle element; else, the average of the middle two elements.
3. Mode: 

...The element(s) which occurs most frequently. 

...If multiple elements satisfy this criteria, display the numerically smallest one.

4. Standard Deviation (SD):  

...SD = (((x1-m)2+(x2-m)2+(x3-m)2+(x4-m)2+...(xN-m)2))/N)0.5

...where xi is the ith element of the array

5. Confidence Interval: 

...Lower and Upper Boundary of the 95% Confidence Interval for the mean, separated by a space.

* Input Format 
```
The first line contains the number of integers. 
The second line contains space separated integers for which you need to find 
the mean, median, mode, standard deviation and confidence interval boundaries.
```
* Constraints
```
..10 <= N <= 2500 
..0 < xi <= 105
```
* Output Format
```
A total of five lines are required.
Mean (format:0.0) on the first line
Median (format: 0.0) on the second line
Mode(s) (Numerically smallest Integer in case of multiple integers)
Standard Deviation (format:0.0) 
Lower and Upper Boundary of Confidence Interval (format: 0.0) with a space between them.
```
* Sample Input
```
10
64630 11735 14216 99233 14470 4978 73429 38120 51135 67060
```
* Sample Output
```
43900.6
44627.5
4978
30466.9
25017.0 62784.2
```
