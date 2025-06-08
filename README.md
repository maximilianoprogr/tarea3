# MongoDB arXiv Project

## Overview
This project aims to investigate and apply the basic concepts of the NoSQL database management system MongoDB. It utilizes Docker for deploying services in a master-slave architecture and employs Python for performing various operations on the database. The project focuses on storing and querying scientific articles from the arXiv repository.

## Project Structure
The project is organized as follows:

```
mongodb-arxiv-project
├── src
│   ├── main.py                  # Main entry point for the application
│   ├── docker
│   │   └── deploy-rol1-rol2.yml # Docker Compose configuration for MongoDB
│   ├── notebooks
│   │   └── pymongo-rol1-rol2.ipynb # Jupyter Notebook for MongoDB operations
│   └── data
│       └── uarxiv-rol1-rol2.json # Final data after operations
├── requirements.txt             # Project dependencies
└── README.md                    # Project documentation
```

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd mongodb-arxiv-project
   ```

2. **Install dependencies**:
   Ensure you have Python and pip installed. Then run:
   ```bash
   pip install -r requirements.txt
   ```

3. **Deploy MongoDB using Docker**:
   Navigate to the `src/docker` directory and run:
   ```bash
   docker-compose -f deploy-rol1-rol2.yml up
   ```

4. **Run the application**:
   Execute the main Python script:
   ```bash
   python src/main.py
   ```

5. **Explore the Jupyter Notebook**:
   Open the Jupyter Notebook located in `src/notebooks/pymongo-rol1-rol2.ipynb` to see the operations performed on the MongoDB database.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.