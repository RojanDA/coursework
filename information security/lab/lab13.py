import os
 
 
# Simulate Malicious Logic: Unauthorized File Modification
def simulate_malicious_logic():
    filename = "sensitive_data.txt"
 
    # Check if the file exists
    if not os.path.exists(filename):
        # Create the file if it does not exist
        with open(filename, "w") as f:
            f.write("This is some sensitive data.\n")
 
    # Display original content
    print("Original Content:")
    with open(filename, "r") as f:
        print(f.read())
 
    # Maliciously modify the file
    with open(filename, "a") as f:
        f.write("This data has been maliciously modified!\n")
 
    # Display modified content
    print("\nModified Content:")
    with open(filename, "r") as f:
        print(f.read())
 
 
# Run the simulation
simulate_malicious_logic()
