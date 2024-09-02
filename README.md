# Emergency Drug Instant Access (EDIA)
#### Video Demo:  <https://youtu.be/4f4_axUu9Lo>
#### Description:
Hello, World! My name is Houman, and I'm an pharmacist with experience in emergency department. I've created EDIA (Emergency Department Information Assistant) to help you quickly recall medication dosages in those hectic emergency situations.

# Introduction
Remembering appropriate drug dosages, especially under pressure, can be challenging. EDIA aims to be a quick and reliable reference tool for emergency medicine professionals. It's a simple Python script that utilizes a CSV file containing a list of common emergency department (ED) diseases and their corresponding medications with dosages.

# Why Use EDIA?
Fast and Efficient: EDIA lets you instantly search for dosages of commonly used medications in the ED. This can save valuable time in critical situations.
Improved Accuracy: By providing a quick reference, EDIA can potentially minimize errors in medication administration.
Customization: The core CSV file can be easily modified to reflect your specific department's protocols and medications.
Knowledge Building Tool: EDIA can be a valuable learning aid for medical students and residents who are still familiarizing themselves with emergency medicine protocols.

# Getting Started with EDIA
# Prerequisites:
Basic understanding of Python programming will be helpful.
Python 3.x installed on your system.
Pandas and Numpy are also needed.

# Installation:
Download this project repository.
Open a terminal window and navigate to the downloaded directory.
There's no separate installation process. You can directly run the script using Python.

# Using EDIA
# Running the Script:
Open your terminal and type the following command, replacing python with your Python interpreter name if it's different:
python EDIA.py
This will launch the EDIA program. You'll be presented with a command prompt.

# Searching for Medication Dosages:

Simply type the name of the medication you're interested in and press Enter. EDIA will search the CSV file and display the corresponding disease(s) and their associated dosages for that medication.

Example:

epinephrine

Disease         | Dose
----------------|--------
Anaphylaxis     | 0.1mg IM q15min (max 0.5mg)

# Updating the CSV File:

The core functionality of EDIA relies on the information stored in the data.csv file. You can freely modify this file to include medications and dosages specific to your department or local practice. The file has three columns:

Disease: Name of the medical condition which include anaphylaxis, bradycardia, cardioversion, cpr, decreased consciousness, hypertension, intubation1, intubation2, seizure, shock, tachycardia, and toxication.
Drugs: Name of the medication used to treat the disease which include adenosine,amiodarone, amrinone, atropine, carbamazepine, deferoxamine, dextrose 50, diazepam, digoxin fab, diltiazem, diphenhydramine, dobutamine, dopamine, enoxaparin, epinephrine, ethanol 43, etomidate, famotidine, fenoldopam, fentanyl, glucagon, heparin, isoproterenol, ketamine, labetalol, lidocaine, lorazepam, methohexital, methylene blue, methylprednisolone, metoprolol, mgso4, midazolam, milrinone, nac, nahco3, naloxone, nicardipine, nitroglycerin, nitroprusside, norepinephrine, octreotide, phenobarbital, phenylephrine, phenytoin, pralidoxime, procainamide, propofol, protamine, pyridoxine, salbutamol, sotalol, thiamin, thiopental, valproate, and vitk.
Dose: Recommended dosage for the specific disease-medication combination.

# Disclaimer:
EDIA is intended as a reference tool only. It should not be used as a substitute for professional medical judgment and knowledge. Always consult established treatment protocols and guidelines before administering any medication.

# Contributing to EDIA
This project is open-source, and we welcome contributions from the medical community. Here's how you can participate:

# Reporting Bugs
If you encounter any issues while using EDIA, please report them through the project's issue tracker on the hosting platform.

# Suggesting Improvements
We appreciate your feedback on how EDIA can be further enhanced. Feel free to suggest new features or functionalities.

# Contributing Code
If you have Python programming experience, you can directly contribute code changes or enhancements to the project repository.

# Conclusion
EDIA aims to be a valuable tool for emergency medicine professionals by providing quick and easy access to medication dosages during critical situations. While it's not a replacement for in-depth medical knowledge, it can serve as a helpful companion when time is of the essence. We encourage you to use, modify, and contribute to this project to make it even more beneficial for the medical community.
