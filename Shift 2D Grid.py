class Solution:
    def shift(self,grid):
        filas=len(grid);
        columnas=len(grid[0]);
        temp=[[0 for _ in range(columnas)] for _ in range(filas)];
        print(temp);
        itemp=0;
        jtemp=0;
        i=0;
        j=0;
        while True:
            if jtemp+1 <columnas:
                jtemp+=1;
            else: 
                jtemp=0;
                if itemp+1 <filas:
                    itemp+=1;
                else:
                    itemp=0;
                    temp[itemp][jtemp]=grid[i][j];
                    return temp;
            temp[itemp][jtemp]=grid[i][j];
            j+=1;
            if j+1>columnas:
                i+=1;
                j=0;
    
    def shiftGrid(self,grid, k):
        for i in range(k):
            grid=self.shift(grid);
        return grid;