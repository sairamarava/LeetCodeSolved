class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(image[0])):
            c=-1
            for j in range(0,len(image)/2):
                image[i][j],image[i][c]=image[i][c],image[i][j]
                c-=1
        for i in range(len(image[0])):
            for j in range(0,len(image)):
                if image[i][j]==1:
                    image[i][j]=0
                else:
                    image[i][j]=1
        return image
        

        
