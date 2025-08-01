# DECISION-TREE-IMPLEMENTATION

COMPANY : CODTECH IT SOLUTIONS

NAME : B.Yaswanth Kumar

INTERN ID : CT06DZ363

DOMAIN : MACHINE LEARNING

DURATION : 6 WEEKS

MENTOR : NEELA SANTHOSH

**The purpose of this task is to implement and visualize a Decision Tree classification model using only core Python-

without using any external packages such as scikit-learn, pandas, numpy, or matplotlib.

The primary goal is to understand the foundational logic and structure of how a decision tree algorithm works, by building it

step-by-step with basic Python constructs. This task provides hands-on insight into one of the most fundamental

supervised machine learning techniques used for classification problems.

Overview : A Decision Tree is a flowchart-like structure in which internal nodes represent tests on attributes, branches represent the outcome of those tests,

and leaf nodes represent class labels. It's a simple yet powerful method that mimics human decision-making and is used widely for both classification and regression tasks.

In this project, we use a manually defined dataset representing weather conditions and whether or not to play a sport (like tennis).

The dataset includes categorical features such as:

1.Outlook (Sunny, Overcast, Rain),

2.Temperature (Hot, Mild, Cool),

3.Humidity (High, Normal), and

4.Wind (Weak, Strong).

Each data point has a label: 'Yes' or 'No', indicating whether to play or not under those weather conditions.

Implementation Details:

The model is constructed manually using core Python features such as lists, dictionaries, and recursion. The tree-building function works recursively by:

1.Checking if all labels are the same in the current subset. If so, it returns that label as a leaf node.

2.If the labels are mixed and no features are left to split on, the function returns the majority class among the labels.

3.Otherwise, it selects the first available feature (for simplicity, without entropy or Gini index calculations), and creates branches for each unique value of that feature.

4.The dataset is split into subsets based on these values, and the function is called recursively for each subset, removing the used feature from the list.

Once the tree is built, a separate function is used to print the tree structure in a readable, indented format. This provides a clear textual visualization

of how decisions are made at each node and how the tree branches based on feature values.

Educational Value:

This project is primarily educational and is designed to give learners a deeper understanding of how decision trees work internally.

By not relying on machine learning libraries, the focus is on the algorithm itself — how data is split, how recursion is used to build the tree, and

how majority voting works at the leaves. Concepts such as feature selection, data partitioning, and recursive tree-building are implemented

explicitly rather than abstracted away by external functions.

The project serves as a stepping stone to more advanced implementations using scikit-learn or other libraries, where entropy or Gini index is used for optimal splitting.

However, the core logic built here mimics the real decision tree learning process and reinforces computational thinking.

Conclusion:

1.By completing this task, one gains:

2.A clear understanding of how decision trees operate.

3.Experience with recursive functions and data handling in core Python.

4.The ability to visualize decision logic through tree structures.

A strong foundation for transitioning to advanced machine learning techniques.

**OUTPUT:**

<img width="1920" height="1020" alt="Image" src="https://github.com/user-attachments/assets/96a4e19b-d479-45c7-b14f-b4a66c2eed0d" />
