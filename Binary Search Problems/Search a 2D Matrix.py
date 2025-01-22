def searchMatrix(matrix, target):
    startn=0
    endn=len(matrix)-1
    while(startn<=endn):
        midn=(startn+endn)//2
        startm=0
        endm=len(matrix[midn])-1
        if(matrix[midn][0]<=target and matrix[midn][endm]>=target):
            while(startm<=endm):
                midm=(startm+endm)//2
                if(matrix[midn][midm]==target):
                    return True
                elif(matrix[midn][midm]<target):
                    startm=midm+1
                elif(matrix[midn][midm]>target):
                    endm=midm-1
            return False
        elif(matrix[midn][0]>target):
            endn=midn-1
        elif(matrix[midn][endm]<target):
            startn=midn+1
            
    return False

matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(searchMatrix(matrix,13))