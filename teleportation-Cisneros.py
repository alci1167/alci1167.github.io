file = open("teleport.in", "r")
file = file.read()
#"a b x y"
a,b,x,y = map(int, file.split())

j = abs(a-b) #takes the absolute value of a-b
k = abs(a-x) + abs(b-y) #absolute value of a-x + b-y
l = abs(a-y) + abs(b-x) #absolute value of a-y + b-x

answer = min(j,k,l) #use min function to find minimum between j,k,l

out = open("teleport.out", "w") #writes answer to teleport.to
out.write(str(answer))
out.close()