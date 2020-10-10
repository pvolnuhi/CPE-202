#
#Polina Volnuhina
#014302388
#4/02/2019
#
#lab 0
#CPE 202-13
#Calculating how much a person would weight in pounds on Mars and Jupiter 


def weight_on_planets():
   # write your code here
   weight = int(input('What do you weigh on earth? '))
   m_weight = weight * 0.38 #surface gravity of mars
   j_weight = weight * 2.34 #surface gravity of jupiter

   print("\nOn Mars you would weigh %0.2f pounds.\nOn Jupiter you would weigh %0.2f pounds." %(m_weight, j_weight))
   
   
   
if __name__ == '__main__':
   weight_on_planets()
