

 #ifndef  HEADER_H_
 #define  HEADER_H_
 
 /* 1- sum of two numbers with operator or without */
	int Sum (int num_1 , int num_2);
	int Sum_Without_OP(int num_1 , int num_2);
/*--------------------------------------------------------*/
/* 2- substarct of two numbers with operator or without */
    int Sub (int num_1 , int num_2);
	int Sub_Without_Op(int num_1 , int num_2) ;
/*--------------------------------------------------------*/
 /* 3- Mulitple of two numbers with operator or without */
    int Mulitple (int num_1 , int num_2);
	int Mulitple_Without_Op (int num_1 , int num_2);
 /* 4- Divition of two numbers with operator or without */	
    int Divide(int num_1 , int num_2);
	int Divide_without_Op(int num_1 , int num_2) ;
 /* 5- Reminder of two numbers with operator or without */	
	int Reminder (int num_1 , int num_2);
 /* 6- Average of two numbers with operator or without */	
	int Average (int num_1 , int num_2);
 /* 7- factors of number  */	
	int Factors_of_number(int num);
 /* 8- factorial of number  */	
	int factorial (int num); 
 /* 9- power  of number  */	
	int Power_number (int num , int power);
	
	int squre (int num);
	
	int sqroot(int n);
/*========================================================*/
 /* 10- prime of number or not */
     int prime(int n);
	 int primebetween2num(int number1 , int number2);
/*========================================================*/
  /* number and get the nearest 10th number */
     int nearest_10th(int num);	 
 /* 11- max of number between two numbers */	
	int Max_Number(int num_1 ,int  num_2);
 /* 12- min of number between two numbers */	
	int Min_Number(int num_1 ,int  num_2);
 /* 13- Reverse of number  */	
	int Reverse (int num);
/* 14- parlindrome of number or not */	
	int Palindrome (int num);// 12321
/*==========================================================*/	
/* 15- number is even or odd */
	int Odd_Even(int num);
/*===========================================================*/	
/* 16- how many digit in number */
	 int Number_Of_Digit (int num); //1235

/* 17- how many digit in number and sum it */	 
	 int Sum_Of_Digit (int num);
/* 18- sum of frist digit and last digit in number  */	 
	 int Sum_Frist_Last_Digit(int num);

/*===========================================================*/	 
 /*  19- Checking number is positive , negative , zero */
      int Check_Number (int num);
	  

 
 #endif  /* HEADER_H_*/
 