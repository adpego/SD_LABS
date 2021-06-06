import grpc
import calculator_pb2
import calculator_pb2_grpc
import sys
import requests
from bs4 import BeautifulSoup

WEB_SERVER="http://localhost:8000/"

def helpMenu():
    print("Command: python3 client.py [OPTION] [PARAM]")
    print("OPTIONS:")
    print("\thelp\t\t- Display help menu")
    print("\tcreateworker\t- Create a worker")
    print("\tdeleteworker\t- Delete a worker, you must specify an id")    
    print("\tlistworkers\t- List workers")
    print("\tlistfiles\t- List files avaliable")
    print("\twordcount\t- Counts the total number of words in different text files or text entries. you must specify a file")
    print("\tcountingwords\t- Counts the number of occurrences of each word in a text file. you must specify a file")
    print()
    print("PARAMS:")
    print("\tid\t\t- Worker identifier, check listworkers option to get this id")
    print("\tfiles\t\t- Filename to do operation, check listfiles option to get the name of files. Can specify more than 1 file separated with ' '. Ex: file1 file2...")




def doConnection():
    channel = grpc.insecure_channel('localhost:50051')
    return calculator_pb2_grpc.CalculatorStub(channel)


def createWorker():
    stub = doConnection()
    response = stub.create_worker(calculator_pb2.Empty()) # Create worker
    if response.value == 0:
        print("Worker created correctly.")
    else:
        print("* Error on creating worker *")

def deleteWorker(id):
    stub = doConnection()
    response = stub.delete_worker(calculator_pb2.Int(value=id))
    if response.value == 0:
        print("Worker deleted correctly.")
    else:
        print("* ERROR: The worker doesn't exist *")

def listWorkers():
    stub = doConnection()
    response = stub.list_workers(calculator_pb2.Empty())
    workers = response.value[1:-1].split(", ")
    for worker in workers:
        print("ID", worker)


def listFiles():
    r = requests.get(WEB_SERVER)
    soup = BeautifulSoup(r.text, 'html.parser')
    for a in soup.find_all('a', href=True):
        print("-", a['href'])

def doOperation(operation, files):
    stub = doConnection()
    urls = [WEB_SERVER+filename for filename in files]
    operation = calculator_pb2.Operation(operation=operation, url=urls)
    response = stub.job_worker(operation)
    print("Result:", response.value)



def main():
    if len(sys.argv) == 1:
        helpMenu()

    elif sys.argv[1] == "help":
        helpMenu()

    elif sys.argv[1] == "createworker":
        print("Create Worker\n")
        createWorker()

    elif sys.argv[1] == "deleteworker":
        if len(sys.argv) == 2:
            print("* Empty id *")
            helpMenu()
        else:
            print("Delete Worker\n")
            deleteWorker(int(sys.argv[2]))

    elif sys.argv[1] == "listworkers":
        print("List Workers\n")
        listWorkers()

    elif sys.argv[1] == "wordcount" or sys.argv[1] == "countingwords":
        if len(sys.argv) == 2:
            print("* Empty url *")
            helpMenu()
        else:
            if sys.argv[1] == "wordcount":
                print("Word Count\n")
            else:
                print("Counting Words\n")

            doOperation(sys.argv[1], sys.argv[2:])

    elif sys.argv[1] == "listfiles":
        print("List Files\n")
        listFiles()

            
    else:
        print("* Incorrect Option *")
        helpMenu()




if __name__ == "__main__":
    main()