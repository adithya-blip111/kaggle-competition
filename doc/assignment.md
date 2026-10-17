#### Task 1: Dataset Exploration and Understanding

Students must explore and understand the provided Kaggle dataset before developing their model. Students are required to:

- [ ] Describe the image classification problem and the eight target classes.
- [x] Inspect the structure of the training and test data.
- [x] Report the number of images in each class.
- [x] Discuss whether the dataset is balanced or imbalanced.
- [x] Display representative sample images from each class.
- [x] Identify any data quality issues, such as 
    - [x] inconsistent image sizes, 
    - [x] blurry images, 
    - [x] corrupted files, 
    - [x] duplicate images, 
    - [x] or unclear class boundaries.
- [ ] Explain how the dataset will be used for training, validation, and Kaggle submission.

#### Task 2: Data Preprocessing and Pipeline Preparation

Students must prepare the image data and develop a reproducible preprocessing pipeline. Students are required to:

- [x] Resize images to a suitable input size for the selected model.
- [x] Normalise or rescale pixel values appropriately.
- [x] Encode class labels into a suitable numerical format.
- [x] Split the labelled training data into training and validation sets using a justified strategy.
- [x] Apply appropriate data augmentation techniques where relevant.
- [x] Use suitable data loaders, generators, or dataset objects for efficient training.
- [x] Ensure that preprocessing is applied consistently to training, validation, and test images.
- [x] Avoid data leakage between training, validation, and test data.

#### Task 3: Model Selection and Pipeline Development

Students must design and implement a complete deep learning image classification pipeline. Students are required to:

- [x] Select and justify a suitable deep learning architecture.	
- [x] Use a 
	- [x] custom CNN, 
	- [x] transfer learning model, 
	- [] Vision Transformer, 
	- [] hybrid CNN--Transformer model, or another appropriate deep learning model.	
- [x] Describe the model architecture and its main components.
- [x] Specify the input image size, output layer, activation function, and number of target classes.
- [x] Select and justify the loss function, optimiser, learning rate, batch size, and number of epochs.
- [x] Implement the complete training pipeline in Python.
- [x] Ensure that the pipeline can generate predictions for the Kaggle test set.

#### Task 4: Training Strategy and Overfitting/Underfitting Management

Students must train their model and monitor its learning behaviour. Students are required to:

- [x] Train the selected model using the prepared training data.
- [x] Monitor training and validation accuracy and loss.
- [ ] Identify signs of overfitting or underfitting.
- [ ] Apply appropriate strategies to improve generalisation, such as data augmentation, dropout, weight decay, batch normalisation, early stopping, learning-rate scheduling, transfer learning, fine-tuning, or model adjustment.
- [ ] Present and discuss learning curves for training and validation performance.
- [ ] Justify any changes made to the model or training strategy.  
    

#### Task 5: Model Evaluation and Kaggle Submission

Students must evaluate their model and submit predictions to the Kaggle competition. Students are required to:

- [ ] Evaluate the model on the validation set using suitable classification metrics.
- [ ] Report validation accuracy and loss.
- [ ] Include additional metrics where appropriate, such as precision, recall, F1-score, confusion matrix, or class-level accuracy.
- [ ] Generate predictions for the Kaggle test images.
- [ ] Prepare the submission file in the required Kaggle format.
- [ ] Submit predictions to the Kaggle competition.
- [ ] Report the Kaggle leaderboard score and include evidence of the submission.
- [ ] Compare validation performance with Kaggle leaderboard performance.

#### Task 6: Results Analysis and Improvement Strategies

Students must critically analyse the results and discuss possible improvements. Students are required to:

- [ ] Interpret the model performance using validation results and Kaggle score.
- [ ] Analyse common misclassifications and difficult classes where possible.
- [ ] Discuss possible reasons for performance limitations.
- [ ] Evaluate the effectiveness of preprocessing, augmentation, model choice, and training strategy.
- [ ] Compare attempted model versions or experimental settings where applicable.
- [ ] Propose realistic strategies for improving performance, such as alternative architectures, hyperparameter tuning, improved augmentation, fine-tuning, ensemble methods, or better validation strategies.
- [ ] Reflect on the strengths and weaknesses of the final solution.

#### Task 7: Report Writing and Reproducibility

Students must prepare a clear individual technical report and provide reproducible supporting files. Students are required to:

- [ ] Write a structured final report of 3,000- 3,500 words, describing the complete workflow.
- [ ] Include sufficient detail about the dataset, preprocessing, model, training strategy, evaluation, Kaggle results, analysis, and improvement strategies.
- [ ] Provide source code or a Jupyter Notebook with clear comments and instructions.
- [ ] Include the final Kaggle submission file.
- [ ] Include Kaggle username and leaderboard evidence.
- [ ] Reference all external libraries, models, papers, tutorials, or resources used.
- [ ] Ensure that the work is original and complies with academic integrity requirements.
- [ ] Submit a Turnitin similarity report with a similarity score not exceeding 20%.