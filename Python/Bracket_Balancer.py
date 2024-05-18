# balanced parentheses in an expression
ol = ["[","{","("]
cl = ["]","}",")"]
  
# Function to check parentheses
def check(myStr):
    st = []
    for i in myStr:
        if i in ol:
            st.append(i)
        elif i in cl:
            pos = cl.index(i)
            if st and ol[pos] == st[-1]:
                st.pop()
            else:
                return "Unbalanced"
    return "Balanced" if not st else "Unbalanced"
  
  
STR = "{[]{()}}"
print(STR,"-", check(STR))
  
STR = "[{}{})(]"
print(STR,"-", check(STR))
