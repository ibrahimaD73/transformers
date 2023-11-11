import click

@click.command()
@click.pass_context
def features_extraction(ctx:click.core.Context):
    logger.info("features extraction")
    ctx.obj['model_name'] = model_name
    # ctx.obj['cache_folder'] = cache_folder

@click.command()
@click.pass_context
def model(ctx:click.core.Context):
    logger.info("model linear")

@click.command()
@click.pass_context
def predict(ctx:click.core.Context):
    logger.info("prediction of model")
