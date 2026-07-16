class Node:
    def __init__(self, patient_id):
        self.patient_id = patient_id
        self.next = None

# Create patients
patient1 = Node(101)
patient2 = Node(102)
patient3 = Node(103)

# Connect them
patient1.next = patient2
patient2.next = patient3

# Print all patient IDs
current = patient1
while current is not None:
    print(current.patient_id)
    current = current.next