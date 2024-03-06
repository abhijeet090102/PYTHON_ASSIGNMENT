#  In a company, worker efficiency is determined on the basis of the time required for a worker to complete a particular job. If the time taken by the worker is between 2 – 3 hours, then the worker is said to be highly efficient. If the time required by the worker is between 3 – 4 hours, then the worker is ordered to improve speed. If the time taken is between 4 – 5 hours, the worker is given training to improve his speed, and if the time taken by the worker is more than 5 hours, then the worker has to leave the company. If the time taken by the worker is input through the keyboard, find the efficiency of the worker.
worker_effici = float(input("Enter worker efficiency work time "))
if(2<=worker_effici<=3):
    print("You are highly efficient")
elif(3<worker_effici<=4):
    print("You have to orderd to improve your speed")
elif(4<worker_effici<=5):
    print("You need training to improve your speed")
elif(5<worker_effici):
    print("You have to leave this company")