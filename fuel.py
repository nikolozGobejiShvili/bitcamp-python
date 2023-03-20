while True:
        try:
            status=input("fraction: ").split("/")
            x= int(status[0])
            y= int(status[1])

            f=int((x * 100 / y))

            if f != 100 and f != 0 and f <100:
                  print(str(f) + "%" )
                  break
                  
            elif  99 <= f == 100:
                  print("F")
                  break
            
            elif  f == 0:
                  print("E")
                  break
            
            elif f > 100:
                  continue
            
        except(Exception):
            continue
          


    
      

    