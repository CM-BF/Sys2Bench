import wandb
api = wandb.Api()

# run is specified by <entity>/<project>/<run_id>
run = api.run("dive-ci/Sys2Bench/uhe1oh7y")

# save the metrics for the run to a csv file
metrics_dataframe = run.history()
metrics_dataframe.to_csv("qwen1.5b_metrics.csv")