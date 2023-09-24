# Sequential Folder Generator

This Python application allows you to create a specified number of consecutive folders with the same name in a chosen destination directory. It also checks for the existence of folders with the same name and starts numbering from the last existing folder.

## Table of Contents

- [Getting Started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Getting Started

### Prerequisites

Before using this application, ensure you have the following prerequisites:

- Python 3.x installed on your system.

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/yourusername/sequential-folder-generator.git
   ```

2.  Navigate to the project directory:
    
    ```bash 
    cd sequential-folder-generator
    ```
    
3.  Run the script:
    
    ```bash
    python main.py
    ``` 
    

## Usage

1.  When you run the script, it will prompt you for the following information:
    
    -   Destination path: The directory where you want to create consecutive folders.
    -   Folder name: The base name for the consecutive folders.
    -   Number of consecutive folders: The number of folders you want to create.
2.  The script will check if the destination path exists and find the last existing folder number (if any) with the same name. It will then create the specified number of consecutive folders starting from the last existing folder number or 1 if no existing folders are found.
    

## Example

Here's an example of how to use the Consecutive Folder Creator:

```bash
$ python main.py
Enter the destination path: /path/to/your/directory
Enter the folder name: folder
Enter the number of consecutive folders: 5
```

This will create five folders named `folder1`, `folder2`, `folder3`, `folder4`, and `folder5` in the specified directory.

## Contributing

Contributions are welcome! If you have ideas for improvements or new features, follow these steps to contribute:

1.  Fork the repository on GitHub.
2.  Clone your forked repository to your local machine.
3.  Make your changes or add new features.
4.  Test your changes thoroughly.
5.  Create a pull request to merge your changes back into the original repository.


## License

This project is open-source and available under the [MIT License](https://en.wikipedia.org/wiki/MIT_License). You are free to use, modify, and distribute this project as you see fit.