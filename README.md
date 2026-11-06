# 🖥️ Core Monitor - Automated System Process Logger

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Psutil](https://img.shields.io/badge/Psutil-Process_Monitoring-orange)
![Automation](https://img.shields.io/badge/Automation-Process_Logging-green)
![Scheduling](https://img.shields.io/badge/Scheduling-Automated-blueviolet)
![System Monitoring](https://img.shields.io/badge/System-Monitoring-00A98F)
![License](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)

**Ever wondered what's actually running behind the scenes on your computer?**

Your system is constantly running hundreds of processes, some visible and some quietly operating in the background. Keeping track of them manually is not exactly anyone's idea of a productive afternoon.

**Core Monitor** is a Python-based automated system process logging tool that periodically scans running processes and generates detailed, timestamped log reports containing process IDs, process names, associated usernames, and memory information.

Built using Python's `psutil` and `schedule` libraries, Core Monitor automates process information collection and maintains organized log records without requiring manual execution of every scan.

Think of it as a lightweight system activity recorder that keeps track of what's happening behind the scenes. ⚙️

---

## 🚀 Key Features

### 1. 🔍 Process Monitoring
- Fetches information about currently running system processes.
- Retrieves Process IDs (PID), process names, and associated usernames.
- Collects virtual memory usage information for individual processes.
- Uses the `psutil` library for system and process information.

### 2. ⏱️ Automated Process Logging
- Automatically executes process scans at user-defined intervals.
- Uses Python's `schedule` library for recurring task execution.
- Performs an initial process scan immediately after starting.
- Continues generating logs automatically without manual intervention.

### 3. 📁 Automatic Log Management
- Creates the specified log directory if it does not exist.
- Generates separate log files for every execution.
- Uses timestamps to identify individual log reports.
- Stores process information in an organized `.log` format.

### 4. 📊 Detailed Process Reports

Every generated log file contains:

- Process ID (PID).
- Process Name.
- Associated Username.
- Memory Usage in MB.
- Timestamp indicating when the report was generated.

### 5. 🛠️ Command-Line Interface
- Simple command-line execution.
- Configurable logging intervals.
- Custom log storage directory.
- Built-in help and usage instructions.
- Supports `--h`, `-h`, `--u`, and `-u` arguments.

### 6. 🛡️ Exception Handling
- Handles processes that terminate during scanning.
- Handles access-denied situations.
- Skips processes that become unavailable during information collection.

---

## ⚙️ How It Works

Core Monitor follows a simple automated workflow.

### Step 1: Configure the Logger

The user provides two command-line arguments:

- **Time Interval:** Frequency of process logging in minutes.
- **Folder Name:** Directory where generated log files will be stored.

### Step 2: Initialize the System

The application starts the scheduler and prints the configured logging interval and destination directory.

### Step 3: Fetch Running Processes

The application uses:

```python
psutil.process_iter()
```

This allows the system to iterate through currently running processes.

For every accessible process, it retrieves:

```python
{
    'pid': process_id,
    'name': process_name,
    'username': process_username
}
```

It also collects memory information using:

```python
proc.memory_info().vms
```

The memory value is converted from bytes into megabytes.

### Step 4: Generate Process Logs

The collected information is written into a timestamped `.log` file.

Each process is recorded with its PID, name, username, and memory information.

### Step 5: Schedule Automatic Execution

The Schedule library executes the logging function repeatedly at the user-defined interval.

The first execution happens immediately when the application starts. Subsequent executions follow the configured schedule.

### Step 6: Maintain Historical Records

Every execution generates a separate log file, allowing users to maintain historical snapshots of system processes.

---

## 📸 Project Demonstration

Here is Core Monitor in action!

### 1. Terminal Execution

The following screenshot demonstrates the application starting successfully, initializing the scheduler, and generating process logs automatically.

![Core Monitor Execution](screenshots/execution.png)

### 2. Generated Process Log

Each execution produces a timestamped report containing information about running processes, including their PIDs, names, usernames, and memory usage.

![Generated Process Log](screenshots/log-file.png)

---

## 🧰 Technologies & Libraries Used

| Technology / Library | Purpose |
|---|---|
| Python 3 | Core programming language |
| Psutil | Fetching system and process information |
| Schedule | Automating recurring process logging |
| OS | Directory management and file handling |
| Sys | Handling command-line arguments |
| Time | Generating timestamps and controlling execution intervals |

### External Dependencies

The project uses two external Python libraries:

- `psutil`
- `schedule`

Other modules used in the application are included in Python's standard library.

---

## 📂 Project Structure

```text
CoreMonitor/
│
├── CoreMonitor.py          # Main process monitoring script
│
├── requirements.txt        # Project dependencies
│
├── .gitignore              # Git ignored files
│
├── README.md               # Project documentation
│
├── LICENSE                 # MIT License
│
└── screenshots/
    ├── execution.png       # Application execution screenshot
    └── log-file.png        # Generated process log screenshot
```

---

## 💻 Installation & Setup

Want to run Core Monitor on your own machine? Follow these steps.

### Prerequisites

- Python 3.x installed on your system.
- pip package manager.
- Basic knowledge of command-line operations.

### Step 1: Clone the Repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd CoreMonitor
```

### Step 2: Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment.

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### Step 3: Install Dependencies

Install the required libraries:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` contains:

```text
psutil
schedule
```

### Step 4: Run the Application

You're ready to go!

---

## ▶️ Usage

Core Monitor operates through a command-line interface.

### 1. Display Help Information

To view the functionalities supported by the application:

```bash
python CoreMonitor.py --h
```

You can also use:

```bash
python CoreMonitor.py -h
```

### 2. Display Usage Instructions

To understand the required command-line arguments:

```bash
python CoreMonitor.py --u
```

You can also use:

```bash
python CoreMonitor.py -u
```

### 3. Start Automated Process Logging

Use the following command format:

```bash
python CoreMonitor.py <Time_Interval> <Folder_Name>
```

**Example (Windows):**

```bash
python CoreMonitor.py 1 "C:\Users\YourName\Documents\CoreMonitor\logs"
```

This command configures the application to:

- Fetch currently running system processes.
- Generate the first process log immediately.
- Store the generated log file inside the specified directory.
- Repeat the process every 1 minute.
- Continue running until manually interrupted.

To stop the application, press:

```text
Ctrl + C
```

**Important:** The time interval must be a positive integer expressed in minutes. The script must remain running for scheduled logging to continue. If the log directory does not exist, the application creates it, provided its parent directory already exists.

---

## 📄 Understanding the Generated Log Files

Core Monitor generates a separate log file for every execution.

### Example Directory Structure

```text
CoreMonitor/
│
└── logs/
    │
    ├── ProcessLog_2026-11-05_21-50-04.log
    ├── ProcessLog_2026-11-05_21-51-04.log
    ├── ProcessLog_2026-11-05_21-52-04.log
    └── ProcessLog_2026-11-05_21-53-04.log
```

### Sample Log Output

```text
--------------------------------------------------
---- Automated Process Logger System (Core Monitor) ----
Log generated at: 2026-11-05_21-50-04
--------------------------------------------------

PID: 0 | Name: System Idle Process | User: NT AUTHORITY\SYSTEM | RAM: 0.06 MB

PID: 4 | Name: System | User: NT AUTHORITY\SYSTEM | RAM: 0.07 MB

PID: 188 | Name: | User: None | RAM: 0.17 MB

PID: 232 | Name: Registry | User: None | RAM: 7.53 MB

PID: 428 | Name: backgroundTaskHost.exe | User: SYSTEM | RAM: 12.12 MB

--------------------------------------------------
------------------ End of log file ---------------------
```

*The actual output depends on the processes running on the machine during each scan.*

---

## 🧠 Core Python Concepts Implemented

This project demonstrates the practical implementation of several Python programming concepts.

### 1. Process Management Using Psutil

- Fetching running processes.
- Retrieving process information.
- Accessing process memory information.
- Handling unavailable processes.

### 2. System & Directory Management

- Checking whether directories exist.
- Creating directories automatically.
- Managing file paths using the OS module.

### 3. File Handling

- Creating timestamped log files.
- Writing process information into files.
- Maintaining separate records for different executions.

### 4. Task Scheduling

- Scheduling recurring functions.
- Executing tasks at configurable intervals.
- Managing continuous execution using loops.

### 5. Command-Line Argument Handling

- Reading arguments using `sys.argv`.
- Validating the number of supplied arguments.
- Implementing help and usage flags.

### 6. Exception Handling

- Handling processes that no longer exist.
- Managing access-denied exceptions.
- Handling zombie processes.
- Managing directory creation and log-writing errors.

---

## ⚠️ Current Limitations

Core Monitor is designed as a lightweight process logging utility. Its current implementation has the following limitations:

- It generates periodic snapshots rather than continuously monitoring process activity.
- It does not terminate, suspend, or control running processes.
- It does not provide real-time graphical monitoring.
- It does not currently track CPU utilization.
- It does not maintain a database of historical process information.
- Some process details may be unavailable due to operating system permissions.
- Separate log files are generated for every execution, with no automatic log cleanup or retention policy.
- The memory value collected by the current implementation is VMS (Virtual Memory Size), although the log labels it as RAM. It should not be interpreted as physical RAM consumption.

---

## 🔮 Future Enhancements

There is plenty of room to expand Core Monitor into a more comprehensive system monitoring solution.

Some planned improvements include:

- **CPU Usage Monitoring:** Track CPU consumption of individual processes.
- **Memory Analytics:** Add physical memory and RAM utilization statistics.
- **Real-Time Dashboard:** Build an interactive dashboard using Streamlit.
- **Process Alerts:** Generate alerts when processes exceed configurable resource thresholds.
- **Historical Analytics:** Store process information in a database for long-term analysis.
- **Log Management:** Introduce automatic log rotation and cleanup.
- **Process Filtering:** Allow users to monitor specific processes by name or PID.
- **System Health Reports:** Generate periodic summaries of system resource utilization.
- **Data Visualization:** Introduce graphical representations of CPU and memory usage.

---

## 👨‍💻 Author

**Shivam Ramesh Kurlekar**

GitHub: [@bemo-codes](https://github.com/bemo-codes)

---

## 📄 License

This project is licensed under the **MIT License**.

See the [LICENSE](LICENSE) file for more information.

---

<p align="center">
  Built with Python 🐍 | Monitoring the processes behind the scenes ⚙️
</p>

<p align="center">
  ⭐ If you find this project interesting, consider giving the repository a star!
</p>
