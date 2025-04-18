# assessment3

Overview: The project explains a requsition system which handles item requests from the staff members. The  performs tasks like collecting staff and requisition information, calculating costs, approving the status on the basis of the rules and allowing managed decisions on pending requsitions. the statistics of number of approved, pending and rejected requests are also stored and displayed. the system supports more than one requisitons in a single run by enclosing the system into a single class.

Breakdown of the code/ steps of the code: 
Global: To receive a unique ID for each requisition, a global variable requisition_counter is intialized to 10000 and the requsitions submitted are stored in a class-level list requisitions.
Class Initialization: The attributes need for each requistion, such as date, staff name, staff Id, Status, total cost and approval reference number.
Staff information: The user is asked for staff name, ID and date by method staff_info and creates a unique requisition ID for each requsition by incrementing global counter.
Requisiton details: Items name and price are collected in the method requsitions_details() in a loop. 
Automatic Approval: The method requsition_approval() evaluates the total cost, if it is below $500 the requisition is automatically approved and if it is equal or more than $500 the requsition remains in pending state.
Managerial response: The manager is asked the manager to either approve, reject or leave the request pending by method respond_requisition()
Display Functions: display_requisition() shows individual requisition details. display_all_requisition() iterates requisition details. show_statistics() provides a count of approved, pending and rejected requistions.
Application loop: the users are allowed to input requistions more than one time. manager reveiws all the requistions and decides to approve or reject it.

Design Evaluation Using Software Principles:
KISS: clear task is performed by each method  making the system easy to follow users input. it can be made easy by separating input, output and processing.
DRY: there are instances of repeated codes. it can be made easier by reusing logic instead of copying code.
Open/Closed Principle: the system is not for extension without modifying existing methods. 
Composition Over Inheritance: method recombination is used to build all functions instead of inheritance heirarchies.
Single Responsibility Principle: theres alot of work done by a single method it can be made easier by breaking down big methods into smaller ones.
Separation of concerns: data input, output and processing is handled all within one class, it can be made easier by dividing responsibilities into layers or classes.
YAGNI: functionality is currently included in the code, it cane be improved by focusing on features that directly serve the intended goal.
Avoid Premature Optimization: the main focus of code is functionality and clarity rather than performance. by ensuring the design is clean and requirements are met the code can be made more easier to understand.
Refactor: refractoring would improve readability.
Clean code: clarity over cleverness is prioritized in the code.

Conclusion: a solid foundation for a user driven item request and approval system is provided in the requistion system. Clear logic, effective use of object-oriented programming and an intuitive user experience. it is well aligned with many clea code and software engineering principles. A few improvements can be made arounf separation of concerns, method refactoring and modularity to make the system more maintainable, professional and less confusing.
