#course work 1
#question 1
#analysing marks

while True:

  mark=0
  count=0
  total=0
  countA=0
  countB=0
  countC=0
  countD=0
  Max_mark=0
  Min_mark=100
  max_count=0

  #introducing a list called mark_list
  mark_list=[]
   
  #checking if the marks are above 0
  while mark>=0:

    try:

      #program says to input the marks 
      mark=int(input("enter the marks, to exit enter any negetive number:  "))
    
    
    
      #if marks are below 0 print " you have entered a mark below 0"
      if mark<0:
         
         print("you have entered a mark below 0")

         #exit the while loop
         break

      #if marks are above 100 print " you have entered a mark above 100"
      if mark>100:

         print("you have entered a mark above 100")

         #goes to the begining of the while loop
         continue

      
             
          
         
      #check if the mark are in range 0 and 29
      if 0<=mark<=29:

          #1 is added to countA if the mark in range 0 and 29
          countA+=1


      #check if the mark are in range 30 and 39   
      elif 30<=mark<=39:

          #1 is added to countB if the mark in range 30 and 39
          countB+=1


      #check if the mark are in range 40 and 69    
      elif 40<=mark<=69:

          #1 is added to countC if the mark in range 40 and 69
          countC+=1
              
      #check if the mark are in range 70 and 100    
      else:

          #1 is added to countD if the mark in range 70 and 100
          countD+=1
              
      #1 is added to count (only marks between 0 to 100)
      count+=1

      #entered mark is added to total(only marks between 0 to 100)
      total+=mark

      #mark_list is modified when a mark is entered(only marks between 0 to 100)
      mark_list.append(mark)

      if mark>Max_mark:
         Max_mark=mark

      if mark<Min_mark:
         Min_mark=mark
            
             
    except:
      #if user enters a input otherthan an intiger program prints "you have entered a invalid index"
      print("you have entered a invalid index")
          
      
   

   

           
  print("\n")       
  #if user enteres a negative number program print "you choose to exit the program"
  print("you choose to exit the program")
  print("\n")


  #prints the maximum mark
  print( "maximum mark is",Max_mark)

  #prints the minimum mark
  print("minimum mark is",Min_mark)

  #print the count of the marks entered 
  print("count of the marks entered is" ,len(mark_list))


  try:

   #print the average if count is not equal to 0  
   print("average is",total/count)

  except:

    #print "count is 0 can' give an average"
    print("count is 0 can't get an average")

  #by adding countC and countD program finds the pass number of students 
  print("number of students with a pass mark is",countC+countD)

  #print in a new line
  print("\n")



  #printing stars horizontly


  print("0-29",end='    ')
  for mark in range(countA):
      print("*",end="")
  print("")
      
  print("30-39",end='   ')
  for mark in range(countB):
      print("*",end="")
  print("")
     
      
  print("40-69",end='   ')
  for mark in range(countC):
      print("*",end="")
  print("")
      
  print("70-100",end='  ')
  for mark in range(countD):
      print("*",end='')
  print("\n")



  #printing stars verticaly 



    
  #check if the countA is greater than count B
  if countA>=countB:
         #if so max_count is countA
         max_count=countA
         
  #check if the countB is greater than count C        
  if countB>=countC:
         #if so max_count is countB
         max_count=countB
         
  #check if the countD is greater than count C       
  if countC>=countD:
         #if so max_count is countC
         max_count=countC
         
  if countD>countC:
     #or else max_count is countD
     max_count=countD
     
        
         



         
        
         
         
           
  # prinr "0-29"
  print("0-29",end='   ' )

  #print "30-39"
  print("30-39",end='   ')

  #print "40-69"
  print("40-69",end='   ')  

  #print"70-100"
  print( "70-100")         

  #his will run while max_count is equal to 0
  while max_count!=0:

     #if countA is over 0 print a star
     if countA>0:
        print("*",end='        ')
        
     #if it is 0 print a space   
     else:
        print(' ',end='        ')
        
     #subtract 1 from countA   
     countA=countA-1   

     #if countB is over 0 print a star
     if countB>0:
        print("*",end='        ')

     #if it is 0 print a space    
     else:
        print(' ',end='        ')
        
     #subtract 1 from countB  
     countB=countB-1
     
      #if countC is over 0 print a star
     if countC>0:
        print("*",end='        ')

     #if it is 0 print a space    
     else:
       print(' ',end='        ')

     #substracting 1 from countC   
     countC=countC-1  

     #if countD is over 0 print a star
     if countD>0:                 
        print("*")

    #if it is 0 print a space 
     else:
        print(' ')

     #substracting 1 from countD   
     countD=countD-1
     
     #1 is substract from max_count
     max_count=max_count-1

     print("")





     

   
