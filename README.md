# DevOps Tools Python Installer Script

This Python script automates the installation of various DevOps tools, including Docker, Kubernetes (Minikube), Jenkins, Git, Gradle, Apache Maven, and Terraform. It also provides guidance on setting up web services such as Katalon TestOps, Azure DevOps, Jira, Raygun, and Trello, offering a command-line interface for easy selection and installation of these tools on Debian-based systems like Ubuntu.

## Prerequisites

- A Debian-based Linux distribution (e.g., Ubuntu)
- Python 3.x installed
- sudo privileges on the system

## Installation

1. **Check Python 3**: Ensure Python 3 is installed by running `python3 --version`. If it's not installed, use your distribution's package manager to install it:

    ```py
    sudo apt update
    sudo apt install python3
    ```

2. **Download the Script**: Clone this repository or download the `devops_tools_installer.py` script directly to your local machine.

3. **Make Executable**: Change the script's permissions to make it executable:

    ```py
    chmod +x devops_tools_installer.py
    ```

4. **Run the Script**: Execute the script using sudo to ensure it has the necessary permissions to install the tools:

    ```
    sudo ./devops_tools_installer.py
    ```

5. **Follow Prompts**: The script will present an interactive menu. Follow the on-screen prompts to select and install your desired DevOps tools.

## Supported Tools

- **Docker**: A set of platform as a service products that use OS-level virtualization to deliver software in packages called containers.
- **Kubernetes (Minikube)**: A tool that lets you run Kubernetes locally. Minikube runs a single-node Kubernetes cluster on your personal computer.
- **Jenkins**: An open-source automation server that enables developers around the world to reliably build, test, and deploy their software.
- **Git**: A free and open-source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.
- **Gradle**: An open-source build automation tool that is designed to be flexible enough to build almost any type of software.
- **Apache Maven**: A default package manager and build tool for Java projects.
- **Terraform**: An open-source infrastructure as code software tool that provides a consistent CLI workflow to manage hundreds of cloud services.

## Web Services Setup

For setting up web services like Katalon TestOps, Azure DevOps, Jira, Raygun, and Trello, visit their respective websites for account creation and integration instructions.

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Fahmi Fareed - [LinkedIn](https://linkedin.com/in/fahmifareed) | [GitHub](https://github.com/fahmifareed)
