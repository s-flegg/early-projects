# for assessing where errors are made
# rows represent the actual classes the outcomes should have been
# columns are our predictions

import matplotlib.pyplot as plt
import numpy
from sklearn import metrics

# gen values
actual = numpy.random.binomial(1, 0.9, size=1000)
predicted = numpy.random.binomial(1, 0.9, size=1000)

# create confusion matrix
confusion_matrix = metrics.confusion_matrix(actual, predicted)

# visual display creation
cm_display = metrics.ConfusionMatrixDisplay(
    confusion_matrix=confusion_matrix, display_labels=[0, 1]
)
# actual display
cm_display.plot()
plt.show()

#  True Negative (Top-Left Quadrant)
# False Positive (Top-Right Quadrant)
# False Negative (Bottom-Left Quadrant)
# True Positive (Bottom-Right Quadrant)
#
# True means that the values were accurately predicted,
# False means that there was an error or wrong prediction.

# Accuracy
# how often the model is correct
# (true pos + true neg) / total predictions
Accuracy = metrics.accuracy_score(actual, predicted)

# Precision
# of positive predicted, what percentage is true
# doesn't eval neg cases
# true pos / ( true pos + false pos)
Precision = metrics.precision_score(actual, predicted)

# Sensitivity (Recall)
# % of predicted positive cases out of all positive
# how good the model is at predicitng positives
# true pos / (true pos + false neg)
Sensitivity_recall = metrics.recall_score(actual, predicted)

# Specificity
# sensitivity but for neg results
# true neg/ (true neg + false pos)
# same functions but with oppositve pos label
Specificity = metrics.recall_score(actual, predicted, pos_label=0)

# F-score
# Harmonic mean of precision and sensitivity
# considers false pos and false neg
# good for imbalanced data sets
# 2 * ((Precision * Sensitivity) / (Precision + Sensitivity))
# doesn't take into account true neg values
F1_score = metrics.f1_score(actual, predicted)

# All metrics in one
print(
    {
        "Accuracy": Accuracy,
        "Precision": Precision,
        "Sensitivity_recall": Sensitivity_recall,
        "Specificity": Specificity,
        "F1_score": F1_score,
    }
)
