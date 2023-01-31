file = open("promote.in", "r")

bronze_in, bronze_out = map(int, file.readline().split()) #reading initial data for bronze, silver, gold, paltinum 
silver_in, silver_out = map(int, file.readline().split())
gold_in, gold_out = map(int, file.readline().split())
platinum_in, platinum_out = map(int, file.readline().split())

val1 = (silver_out + gold_out + platinum_out) - (silver_in + gold_in + platinum_in) #ending data - staring data to give us bronze to silver promotions 
val2 = (gold_out + platinum_out) - (gold_in + platinum_in) #ending data - staring data to give us silver to gold 
val3 = platinum_out - platinum_in #ending data - staring data to give us gold to plat

answer = (str(val1)) + "\n" + (str(val2)) + "\n" + (str(val3)) #outpout answer in a column 
out = open("promote.out", "w") #writes answer to promote.out
out.write(answer)
out.close()