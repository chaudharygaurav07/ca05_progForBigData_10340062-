sum <- function(x, y) {
    return(x + y)
}

minus <- function(x, y) {
    return(x - y)
}

multiply <- function(x, y) {
    return(x * y)
}

divide <- function(x, y) {
    return(x / y)
}

exponent <-function(x,y) {
	return (x**y)
}

factorial <- function(x){ 
   y <- 1 
   for(i in 1:x){ 
     y <-y*((1:x)[i]) 
   } 
   return(y) 
 } 

 trig_cos <- function(x) { 
   return(cos(x*pi/180)) 
 } 
 
 
 trig_sin <- function(x) { 
   return(sin(x*pi/180)) 
 } 

 squareroot <-function(x) { 
   return (sqrt(x)) 
 } 
 
# take input from the user
print("Select operation.")
print("1.Sum")
print("2.Minus")
print("3.Multiply")
print("4.Divide")
print("5.exponent")
print("6.factorial")
print("7.trig_cos")
print("8.trig_sin")
print("9.squareroot")

choice = as.integer(readline(prompt="Enter choice[1/2/3/4/5/6/7/8/9]: "))
number1 = as.integer(readline(prompt="Enter first number: "))
number2 = as.integer(readline(prompt="Enter second number: "))
operator <- switch(choice,"+","-","*","/")
result <- switch(choice, sum(number1, number2), minus(number1, number2), multiply(number1, number2), divide(number1, number2),exponent(number1, number2),factorial(number1),trig_cos(number1),trig_sin(number1),squareroot(number1))
print(paste(number1, operator, number2, "=", result))
