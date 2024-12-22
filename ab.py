# Function to get candidate details
def get_candidate_details():
    name = input("Enter the candidate's name: ")
    age = int(input("Enter the candidate's age: "))
    qualification = input("Enter the candidate's highest qualification: ")
    experience = int(input("Enter the candidate's years of experience: "))
    return name, age, qualification, experience

# Function to check if the candidate is shortlisted
def check_shortlist(age, qualification, experience, min_age, required_qualification, min_experience):
    if age >= min_age and qualification == required_qualification and experience >= min_experience:
        return True
    else:
        return False

# Function to display the summary of shortlisted and rejected candidates
def display_summary(shortlisted, rejected):
    print("\n--- Shortlisted Candidates ---")
    for candidate in shortlisted:
        print(candidate)
    
    print("\n--- Rejected Candidates ---")
    for candidate in rejected:
        print(candidate)

# Main function to run the program
def main():
    # Define job criteria
    min_age = 25
    required_qualification = "B.Tech"
    min_experience = 2

    # Lists to store shortlisted and rejected candidates
    shortlisted = []
    rejected = []

    # Input the number of candidates
    num_candidates = int(input("Enter the number of candidates to evaluate: "))

    # Loop to process each candidate
    for _ in range(num_candidates):
        # Get candidate details
        name, age, qualification, experience = get_candidate_details()

        # Check if the candidate meets the conditions for shortlisting
        if check_shortlist(age, qualification, experience, min_age, required_qualification, min_experience):
            shortlisted.append(name)
        else:
            rejected.append(name)

    # Display the summary of shortlisted and rejected candidates
    display_summary(shortlisted, rejected)

# Run the main function
if __name__ == "__main__":
    main()
