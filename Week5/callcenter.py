from datetime import datetime

class Call(object):
    unique_id = 0
    def __init__(self, name, phone_number, reason):
        self.time = datetime.now()
        self.name = name
        self.phone_number = phone_number
        self.id = Call.unique_id
        Call.unique_id += 1
        self.reason = reason

    def printInformation(self):
        print "---------------------------"
        print "ID: " + str(self.unique_id)
        print "Caller Name: " + str(self.name)
        print "Caller Phone Number: " + str(self.phone_number)
        print "Time of Call: " + str(self.time)
        print "Reason for Call: " + str(self.reason)
        return self

class CallCenter(object):
    def __init__(self):
        self.calls = []
    def queue_size(self):
        return len(self.calls)
    
    def add(self, Call):
        self.calls.append(Call)
        return self

    # removes the call from the beginning of the list (index 0)
    def remove(self):
        self.calls.pop(0)
        return self

    # prints the namne and phone number for each call in the queue as well as the length of the queue
    def info(self):
        for call in self.calls:
            call.printInformation()


call1 = Call("Robert", "425123456", "Refund")
call2 = Call("Tom", "425456789", "Install")

#call2.printInformation()


callcenter = CallCenter()
callcenter.add(call1).add(call2)

# call2.printInformation()
#print callcenter.queue_size()
#callcenter.remove()
#print callcenter.queue_size()
callcenter.info()




