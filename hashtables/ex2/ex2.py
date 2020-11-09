#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here
    tickets_HT = {}

    for t in tickets:
        tickets_HT[t.source.upper()] = t.destination

    route = []

    route.append(tickets_HT["NONE"])
    i = 0

    while i < length - 1:
        route.append(tickets_HT[route[i]])
        i += 1


    return route


ticket_1 = Ticket("NONE", "PDX")
ticket_2 = Ticket("PDX", "DCA")
ticket_3 = Ticket("DCA", "NONE")

tickets = [ticket_1, ticket_2, ticket_3]

print(reconstruct_trip(tickets, 3))