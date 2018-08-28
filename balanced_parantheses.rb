# The expression contains parentheses: ( and ) 
# The expression does not contain any other symbols 
# Return true if the parentheses are balanced 
# Otherwise, return false 
# Examples: # () => true # (()()) => true # ( => false # )( => false 

def balance_parentheses(expression) 
 
  counter = 0 

  expression.each_char do |pr|
    counter+=1 if pr == "("
    counter-=1 if pr == ")"

  end

  return counter == 0 ? true : false
  
end

balance_parentheses("())()()()(((((")
