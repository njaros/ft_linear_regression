### What is that ?

The rule of this project is to discovered the linear regression, which is an important part of machine learning.
  
A linear regression of a dataset is an equation line y = ax + b which approximate at most as possible the point cloud formed by the dataset  

The linear regression line is able to predict a value y form an x consistent with the dataset  

### How to use the programs

# Step1:
	To "train" the a and b of the linear regression line, go to the root of the project and type :  
	python3 training.py data.csv ( + optionnals [learningRate as a float] [iterations as an int])
	exemples :
		- python3 training.py data.csv 0.5 1000
		- python3 training.py data.csv

	The program will show some curves and create a file "thetas_scale_values.json"  
	You can do it with different learningRate and iterations values until the curves seems good.  
  
# Step2:
	To predict values, type in a terminal :
	python3 predict.py thetas_scale_values.json

![image](https://github.com/jajalecapouet/ft_linear_regression/assets/90960943/19686abf-61c1-4683-8bf5-3f5c389b9269)
![image](https://github.com/jajalecapouet/ft_linear_regression/assets/90960943/f6be2ce5-b0c8-42db-a945-051db681c286)


### DOC

- http://grasland.script.univ-paris-diderot.fr/STAT98/stat98_1/stat98_1.htm
- https://www.youtube.com/watch?v=8Y3r7F47Xfo&ab_channel=MachineLearnia

