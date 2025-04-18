requisition_counter = 10000 # clean code: naming clarity and spelling corrected from"requsition".

class RequisitionSystem:
    requisitions = [] # Yagni: no extra unused attributes - focused, revelant data structure.

    def __init__(self):
        #KISS : initialization is clear and minimal - good start.
        self.date = None
        self.staff_id = None
        self.staff_name = None
        self.requisition_id = None
        self.total = 0
        self.status = "Pending"
        self.approval_reference_number = "Not available"

    def staff_info(self):
        #Separation of concern: This method combines input logic and internl updates.
        #SRP: Doing multiple things - gather input, update counter, assign values.
        global requisition_counter
        self.staff_name = input("Enter Staff Name: ")
        self.date = input("Enter Date (DD/MM/YYYY): ")
        self.staff_id = input("Enter Staff ID: ")
        requisition_counter += 1
        self.requisition_id = requisition_counter

    def requisitions_details(self):
        #DRY: Repeated print statements 
        total = 0
        while True:
            item_name = input("Enter requisition item name (or type 'no' to stop): ")
            if item_name.lower() == "no":
                break
            else:
                item_price = float(input("Enter the price of the item: $"))
                total += item_price
                print(f"Item Name: {item_name}")#DRY opportunity
                print(f"Item Price: ${item_price:.2f}\n")#DRY opportunity
            
        self.total = total
        print(f"Total Requisition Cost: ${self.total:.2f}")

    def requisition_approval(self):
        #Open/Closed: Approval logic is hardcoded
        #SSRP: Method performs both logic and output
        if self.total < 500:
            self.status = "Approved"
            self.approval_reference_number = self.staff_id + str(self.requisition_id)
        else:
            self.status = "Pending"
            self.approval_reference_number = "Not available"

        print("\nRequisition Result:")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference_number}")

    def respond_requisition(self):
        #Combines processing logic and input 
        #Not easily extendale
        if self.status == "Pending":
            print(f"\nPending Requisition: ID {self.requisition_id}, Total: ${self.total}")
            decision = input("Manager decision (Approve / Not approved / Leave as is): ").lower()
            if decision == "approve":
                self.status = "Approved"
                self.approval_reference_number = self.staff_id + str(self.requisition_id)
            elif decision == "not approved":
                self.status = "Not approved"

    def display_requisition(self):
        #DRY: repeatedly used structure 
        print(f"\nDate: {self.date}")
        print(f"Requisition ID: {self.requisition_id}")
        print(f"Staff ID: {self.staff_id}")
        print(f"Staff Name: {self.staff_name}")
        print(f"Total: ${self.total}")
        print(f"Status: {self.status}")
        print(f"Approval Reference Number: {self.approval_reference_number}")

    @classmethod
    def display_all_requisitions(cls):
        #KISS: Simple , understandable logic.
        for req in cls.requisitions:
            req.display_requisition()

    @classmethod
    def show_statistics(cls):
        total = len(cls.requisitions)
        #Clean Code: Fix spelling mistakes
        approved = 0
        pending = 0
        not_approved = 0

        for request in cls.requisitions:
            if request.status == "Approved":
                approved += 1
            elif request.status == "Pending":
                pending += 1
            elif request.status == "Not approved":
                not_approved += 1

        print("Displaying the requsition statitics")
        print(f"The total number of requisitions submitted: {total}")
        print(f"The total number of approved requsitions: {approved}")
        print(f"The total number of pending requsitions: {pending}")
        print(f"The total number of not approved requsitions: {not_approved}")


while True:
    print("\nRequisition Entry")
    req =RequisitionSystem()
    req.staff_info()
    req.requisitions_details()
    req.requisition_approval()
    RequisitionSystem.requisitions.append(req)
    another = input("\nDo you want to enter another requisition? (yes/no): ")
    if another.lower() != "yes":
        break
# Manager responses
print("\nManager Review for Pending Requisitions")
for req in RequisitionSystem.requisitions:
    if req.status == "Pending":
        req.respond_requisition()
# Display final data
print("\nFinal Requisition Info")
RequisitionSystem.display_all_requisitions()
print("\nFinal Statistics")
RequisitionSystem.show_statistics()
