# IDS_DDOS 2020-2021

   This workgroup is a project created by 4 students of the University of Visvesvaraya Technological University for the fourth year. 

## Abstract 

The purpose of this project is to develop an artificial intelligence to classify possible DDoS attacks in an SDN network. This will be done by using data collectors such as Telegraf, Mininet to emulate the SDN network, and InfluxDB as a means to store data.

**Keywords**: [`DDoS attacks`](https://www.digitalattackmap.com/); [`SDN network`](https://www.opennetworking.org/sdn-definition/); [`Artificial Intelligence classification`](https://www.sciencedirect.com/science/article/abs/pii/016974399500050X); [`Mininet`](http://mininet.org/)


## CODE EXPLANATION

**[src-> SVM.ipynb]:**
The provided Python code performs a classification task using Support Vector Machine (SVM) on a dataset, and it evaluates the performance of the classifier using various metrics. Below is a summary of the code:

1. Import necessary libraries: `pandas` for data manipulation and analysis, `sklearn` for machine learning tools, and specific functions and classes from `sklearn`.

2. Load the dataset from a CSV file named 'dataset.csv' into a Pandas DataFrame. The dataset contains three columns: 'curr_derivative', 'mean', and 'label'. 'curr_derivative' and 'mean' are the features, and 'label' is the target variable to be predicted.

3. Split the dataset into features (X) and the target variable (y).

4. Split the data into training and testing sets using the `train_test_split` function. It uses 70% of the data for training and 30% for testing.

5. Create a Support Vector Machine (SVM) classifier using `svm.SVC` with a linear kernel.

6. Train the SVM classifier using the training data (features and labels) with the `fit` method.

7. Make predictions on the test data using the trained classifier with the `predict` method.

8. Calculate and print various metrics to evaluate the classifier's performance:

   - Accuracy: The percentage of correctly classified instances in the test set.
   - Precision: The percentage of true positive predictions out of all positive predictions.
   - Recall: The percentage of true positive predictions out of all actual positive instances.
   - Confusion matrix: A matrix showing the number of true positive, true negative, false positive, and false negative predictions.
   - Classification report: A report showing precision, recall, F1-score, and support for each class.
   - Correct predictions percentage: The percentage of correct predictions.
   - Wrong predictions percentage: The percentage of incorrect predictions.

Overall, this code uses SVM to create a classification model based on the provided dataset. It then evaluates the model's performance using various metrics, providing insights into the accuracy and quality of the predictions made by the SVM classifier.


**[src-> data_gathering.py]:**
The provided Python code is a script that queries a time-series database (InfluxDB) to retrieve a set of data points, processes the data, and then saves it to a CSV file. Below is a summary of the code:

1. Import necessary libraries: `influxdb` for interacting with the InfluxDB, and `sys` for system-level operations.

2. Define the `QUERY` string, which contains an InfluxQL query to retrieve data from the 'net' measurement in the database. The query calculates the derivative of the 'icmp_inechos' field and orders the results in descending order, limiting the number of results to 100.

3. Initialize variables `n_samples` and `mean` to keep track of the number of data samples and the running mean, respectively.

4. The code checks the number of command-line arguments provided when executing the script and sets up the InfluxDB connection accordingly. The script accepts 0 to 4 arguments: measurement_class, InfluxDB_IP, InfluxDB_port, and DB_name, and uses default values for missing arguments.

5. Open an output file named "ICMP_data_class_{measurement_class}.csv" in write mode to save the processed data.

6. The code queries the InfluxDB database using the defined `QUERY` and iterates through the retrieved data points for the 'net' measurement.

7. For each data point, it calculates the current derivative ('d_ping') and updates the running mean. The script then writes the data, mean, and measurement_class to the output file in CSV format.

8. After processing all data points, the output file is closed, and a message is printed indicating that the class-specific training dataset has been generated.

In summary, this script serves as a data processing tool that queries a specific InfluxDB database for time-series data, calculates the derivative of a specified field, and computes the running mean of the derivatives. It then saves the processed data along with the mean and measurement class to a CSV file for further analysis or use in machine learning tasks. The script allows for customization of the database connection and the output file's name based on the command-line arguments provided when executing the script.


**[src-> ddos.py]:**
The provided Python code is a simple script for performing a Distributed Denial of Service (DDoS) attack using the hping3 tool. The script takes a single command-line argument, which is the destination IP address that the attack will be launched against. Below is a summary of the code:

1. Import necessary libraries: `os`, `sys`, `time`, and `datetime`.

2. Define various global parameters used throughout the script. These parameters include error messages, informational messages, attack settings (such as packets cadence, packets length, data length, etc.), and initial wait time.

3. Define helper functions:
   - `get_str_time()`: Returns the current time in a specific format.
   - `diff()`: Calculates the time difference between the current time and the time the script was initiated (stored in `time_init`).

4. The script starts by checking the number of command-line arguments provided when executing the script. It expects exactly one argument, which is the destination IP address. If the argument count is incorrect, it prints an error message and exits the script.

5. After verifying the argument, it initializes the `time_init` variable to store the current time when the script starts.

6. The script informs the user that the DDoS attack is starting on the given destination IP address and provides instructions to stop the attack (by pressing CTRL+C). It then pauses for a brief moment using `os.system('sleep ' + str(INIT_WAIT))`.

7. The script uses the `hping3` tool to initiate the DDoS attack. It runs the `hping3` command with the provided destination IP address and specific options (`-V` for verbose, `-1` for ICMP echo request, `-d 1400` for packet data size, and `--faster` to send packets at maximum speed).

8. After the attack is executed, the script shows the attack statistics, including the time elapsed since the attack started and the data sent in MB.

9. The script concludes by printing a message indicating that the attack has completed.

In summary, this script is a simple and potentially harmful tool for launching a DDoS attack using the hping3 tool. DDoS attacks are illegal and unethical, and this script should not be used for any malicious or harmful purposes. It is essential to use programming knowledge responsibly and always adhere to ethical guidelines and legal regulations.
