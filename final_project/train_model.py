from neural_network.train import Trainer

def train(loss):
    trainer = Trainer("models/other_optimizer.h5", loss)
    metrics, scores = trainer.train()

    with open("training_results.csv", "a") as f:
        f.write(str(loss) + ", ")
        for i in range(len(scores)):
            f.write( str(scores[i]) )
            if i == len(scores) - 1:
                f.write("\n")
            else:
               f.write(", ")

    # trainer.save()
    # trainer.save_architecture()

loss_functions = [ "mean_squared_error", "mean_absolute_error", "mean_absolute_percentage_error", "mean_squared_logarithmic_error", "squared_hinge",
    "hinge", "categorical_hinge", "logcosh", "categorical_crossentropy", "binary_crossentropy",
    "kullback_leibler_divergence", "poisson", "cosine_proximity"
]

with open("training_results.csv", "w") as f:
    f.write("loss_function, loss_value, categorical_accuracy, top_k_categorical_accuracy\n")

for loss_function in loss_functions:
    train(loss_function)