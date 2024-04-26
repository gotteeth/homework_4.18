service_tickets = {
    "Ticket001": {"Customer": "Alice", "Issue": "Login problem", "Status": "open"},
    "Ticket002": {"Customer": "Bob", "Issue": "Payment issue", "Status": "closed"}
}

def update_ticket(tickets):
    ticket_id = ("please enter you id:  ")
    if ticket_id in tickets:
        new_status = input("please enter new status (open/closed): ")
        tickets[ticket_id]["status"] = new_status
        print("ticket updated successfully.")
    else:
        print("ticket id not found.")


def display_ticket(tickets):
   filter_choice = input("Filter by status (open/closed/all): ").lower()
   if filter_choice in ["open" , "closed"]:
       filtered_tickets = {ticket_id: details for ticket_id, details in tickets.items() if details["Status"] == filter_choice}
       print("Filtered Tickets:")
       for ticket_id, info in filtered_tickets.items():
            print(ticket_id, info)
       for ticket_id, info in filtered_tickets.items():
            print(ticket_id, info)
       else:
          print("All Tickets:")
       for ticket_id, info in tickets.items():
            print(ticket_id, info)

       

    
        

def new_ticket(tickets):
     ticket_id = "service ticket" + str(len(tickets) + 1).zfill(3)#just learn about this.. pretty cool
     ticket_name = input("what is your name? ")
     ticket_issue = input(" please describe the problem you are having?  ")
   
     ticket_status = "open "
     tickets[ticket_id] = {"customer": ticket_name, "issue": ticket_issue, "status": ticket_status}
     print(f"your ticket id is ", ticket_id)
     print(tickets)

      
   
while True:
   choice = input(   
     """ what would you like to do
      
      1). open a new ticket
      2). update the status of a existing ticket
      3). display all ticket(s) of filter by status
       4). quit  
          >   """).lower
   if choice == "1" or choice == "open a new ticket":
      new_ticket(service_tickets)
   elif choice == "2" or choice == "update the status of a existing ticket":
        pass
   elif choice == "3" or choice == "display all ticket(s) of filter by status":
        pass
   else:
     pass
     
    

    




service_tickets()