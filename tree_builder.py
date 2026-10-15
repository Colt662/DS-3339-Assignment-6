class EmployeeNode:
    '''
    A class to represent a node in the binary tree.
    Attributes:
        name (str): The name of the employee.
        left (EmployeeNode): The left child node, representing the left subordinate.
        right (EmployeeNode): The right child node, representing the right subordinate.
    '''

    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None
    

class TeamTree:
    '''
    A class to represent a binary tree for managing a team structure.
    Attributes:
        root (EmployeeNode): The root node of the tree, representing the team lead.
    Methods:
        insert(manager_name, employee_name, side, current_node=None): Inserts a new employee under the specified manager.
        print_tree(node=None, level=0): Prints the tree structure starting from the given node.

    '''
    
    def __init__(self):
        self.root = None

    def insert(self, manager_name, employee_name, side, current_node=None):
        if self.root == None:
            print("Set team manager to begin adding other employees.")
            return


        if current_node == None:
            current_node = self.root


        if manager_name == current_node.name:
            if side.lower().strip() == "left":
                if current_node.left == None:
                    current_node.left = EmployeeNode(employee_name)
                    print(f'{employee_name} added to the {side.upper()} of {manager_name}.')
                    return True #manager found

                else:
                    print(f'{manager_name} already has an employee on their {side.upper()} side. Try the other side.')
                    return True #manager found


            elif side.lower().strip() == "right":
                if current_node.right == None:
                    current_node.right = EmployeeNode(employee_name)
                    print(f'{employee_name} added to the {side.upper()} of {manager_name}.')
                    return True #manager found

                else:
                    print(f'{manager_name} already has an employee on their {side.upper()} side. Try the other side.')
                    return True #manager found 

            else:
                print("The selected manager already has 2 direct subordinates.")
                return True #manager found



        else:
            if current_node.left != None:
                if self.insert(manager_name, employee_name, side, current_node.left):
                    return True #manager found down this side, no need to keep checking

            
            if current_node.right != None:
                if self.insert(manager_name, employee_name, side, current_node.right):
                    return True #manager found


            if current_node == self.root: #Implied based on the fact a return statment hasn't fired: the manager was not found anywhere in the tree
                print(f'No manager with the name {manager_name} was found. Try checking the spelling.')
                return
            return False #Implied based on the fact a return statment hasn't fired: the manager was not found anywhere in the tree





    def print_tree(self, node=None, level=0):
        if self.root == None:
            print("Tree is empty")
            return


        if node == None and level == 0:
            node = self.root

        print(f'{"":{level*2}}- {node.name}')
        if node.left != None:
            self.print_tree(node.left, level + 1)

        if node.right != None:
            self.print_tree(node.right, level + 1)







# CLI functionality
def company_directory():
    tree = TeamTree()

    choice = ""

    while choice != "4":
        print("\n📋 Team Management Menu")
        print("1. Add Team Lead (root)")
        print("2. Add Employee")
        print("3. Print Team Structure")
        print("4. Exit")
        choice = input("Choose an option (1–4): ")

        if choice == "1":
            if tree.root:
                print("⚠️ Team lead already exists.")
            else:
                name = input("Enter team lead's name: ")
                tree.root = EmployeeNode(name)
                print(f"✅ {name} added as the team lead.")

        elif choice == "2":
            manager = input("Enter the manager's name: ")
            employee = input("Enter the new employee's name: ")
            side = input("Should this employee be on the LEFT or RIGHT of the manager? ")
            side = side.lower()
            tree.insert(manager, employee, side)

        elif choice == "3":
            print("\n🌳  Current Team Structure:")
            tree.print_tree()

        elif choice == "4":
            print("Good Bye!")
            break
        else:
            print("❌ Invalid option. Try again.")

def test_cases():
    company_directory = TeamTree()
    print("Before setting root:")
    company_directory.insert("Jordan", "Taylor", "right")
    company_directory.insert("Jordan", "Riley", "left")
    company_directory.insert("Riley", "Dana", "right")
    company_directory.insert("Riley", "Morgan", "left")
    company_directory.print_tree()

    print("Normal behavior:")
    company_directory.root = EmployeeNode("Jordan")
    company_directory.insert("Jordan", "Taylor", "right")
    company_directory.insert("Jordan", "Riley", "left")
    company_directory.insert("Riley", "Dana", "right")
    company_directory.insert("Riley", "Morgan", "left")
    company_directory.print_tree()

    print("Slots already occupied:")
    company_directory.insert("Jordan", "Taylor", "right")
    company_directory.insert("Jordan", "Riley", "left")
    company_directory.insert("Riley", "Dana", "right")
    company_directory.insert("Riley", "Morgan", "left")
    company_directory.print_tree()

    print("Manager does not exist:")
    company_directory.insert("DNE", "Taylor", "right")
    company_directory.insert("DNE", "Riley", "left")
    company_directory.insert("DNE", "Dana", "right")
    company_directory.insert("DNE", "Morgan", "left")

if __name__ == "__main__":
    #test_cases()
    company_directory()