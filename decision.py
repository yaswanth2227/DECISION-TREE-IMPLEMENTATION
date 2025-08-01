dataset = [
    (['Sunny', 'Hot', 'High', 'Weak'], 'No'),
    (['Sunny', 'Hot', 'High', 'Strong'], 'No'),
    (['Overcast', 'Hot', 'High', 'Weak'], 'Yes'),
    (['Rain', 'Mild', 'High', 'Weak'], 'Yes'),
    (['Rain', 'Cool', 'Normal', 'Weak'], 'Yes'),
    (['Rain', 'Cool', 'Normal', 'Strong'], 'No'),
    (['Overcast', 'Cool', 'Normal', 'Strong'], 'Yes'),
    (['Sunny', 'Mild', 'High', 'Weak'], 'No'),
    (['Sunny', 'Cool', 'Normal', 'Weak'], 'Yes'),
    (['Rain', 'Mild', 'Normal', 'Weak'], 'Yes'),
    (['Sunny', 'Mild', 'Normal', 'Strong'], 'Yes'),
    (['Overcast', 'Mild', 'High', 'Strong'], 'Yes'),
    (['Overcast', 'Hot', 'Normal', 'Weak'], 'Yes'),
    (['Rain', 'Mild', 'High', 'Strong'], 'No'),
]

# Get the majority class in a list of examples
def majority_class(data):
    from collections import Counter
    labels = [label for features, label in data]
    return Counter(labels).most_common(1)[0][0]

# Build a simple decision tree (ID3-like using first feature)
def build_tree(data, features):
    labels = [label for row, label in data]
    if labels.count(labels[0]) == len(labels):
        return labels[0]
    if len(features) == 0:
        return majority_class(data)

    best_feat = 0  # Always pick first feature for simplicity
    tree = {}
    feat_values = set(row[0] for row, label in data)

    for value in feat_values:
        sub_data = []
        for row, label in data:
            if row[0] == value:
                sub_data.append((row[1:], label))
        subtree = build_tree(sub_data, features[1:])
        tree[f"{features[0]} = {value}"] = subtree
    return tree

# Pretty-print the tree
def print_tree(tree, indent=""):
    if isinstance(tree, dict):
        for key, value in tree.items():
            print(indent + str(key))
            print_tree(value, indent + "  ")
    else:
        print(indent + "=> " + tree)

# Run the example
features = ['Outlook', 'Temperature', 'Humidity', 'Wind']
tree = build_tree(dataset, features)
print("Decision Tree:")
print_tree(tree)
