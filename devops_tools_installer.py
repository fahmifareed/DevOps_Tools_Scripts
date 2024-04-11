import subprocess

# Function to run shell commands
def run_command(command):
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Installation functions
def install_docker():
    print("Installing Docker...")
    run_command("curl -fsSL https://get.docker.com -o get-docker.sh && sudo sh get-docker.sh")

def install_kubernetes():
    print("Installing Kubernetes (Minikube)...")
    run_command("curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 && sudo install minikube-linux-amd64 /usr/local/bin/minikube")

def install_jenkins():
    print("Installing Jenkins...")
    run_command("wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add - && sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list' && sudo apt-get update && sudo apt-get install jenkins -y")

def install_git():
    print("Installing Git...")
    run_command("sudo apt-get update && sudo apt-get install git -y")

def install_gradle():
    print("Installing Gradle...")
    run_command("sudo apt-get update && sudo apt-get install gradle -y")

def install_maven():
    print("Installing Apache Maven...")
    run_command("sudo apt-get update && sudo apt-get install maven -y")

def install_terraform():
    print("Installing Terraform...")
    run_command("sudo apt-get update && sudo apt-get install terraform -y")

def setup_web_services():
    print("For Katalon TestOps, Azure DevOps, Jira, Raygun, and Trello, please visit their respective websites for setup instructions.")

# Main menu
def show_menu():
    print("""
Welcome, Fahmi Fareed. Your LinkedIn and GitHub username: fahmifareed
1) Install Docker
2) Install Kubernetes (Minikube)
3) Install Jenkins
4) Install Git
5) Install Gradle
6) Install Apache Maven
7) Install Terraform
8) Setup Web Services (Info)
9) Exit
""")
    choice = input("Enter your choice (1-9): ").strip()
    return choice

def main():
    while True:
        choice = show_menu()
        if choice == '1':
            install_docker()
        elif choice == '2':
            install_kubernetes()
        elif choice == '3':
            install_jenkins()
        elif choice == '4':
            install_git()
        elif choice == '5':
            install_gradle()
        elif choice == '6':
            install_maven()
        elif choice == '7':
            install_terraform()
        elif choice == '8':
            setup_web_services()
        elif choice == '9':
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
        print("\nWhat would you like to do next?")

if __name__ == "__main__":
    main()
